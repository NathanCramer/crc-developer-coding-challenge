from django.shortcuts import render

from api.models import Participant, Workout, ParticipantWorkout


def index(request):
    return render(request, 'api_index.html')


def get_workout_scores():
    """
    This function calculates the standings for each participant in each workout.
    :return: [
        {
            'id': 1,
            'participant': 'John Doe',
            'standing': 1,
            'workout_scores': [
                {
                    'id': 1,
                    'workout_id': 1,
                    'workout_name': 'Workout 1',
                    'score': 100,
                    'standing': 1
                },
                {
                    'id': 2,
                    'workout_id': 2,
                    'workout_name': 'Workout 2',
                    'score': 200,
                    'standing': 2
                }
            ],
            'total_points': 3
        },
    ]
    """
    participants = Participant.objects.all()
    workouts = Workout.objects.all()

    participant_workouts = [
        {
            'id': participant.id,
            'participant': participant.name + ' ' + participant.surname,
            'standing': 0,  # Participants Total Rank (where 1 is the best)
            'workout_scores': [
                {
                    'id': 0,
                    'workout_id': workout.id,
                    'workout_name': workout.name,
                    'score': -1,
                    'read_score': "No Score",
                    'standing': 0,  # Participants Rank in this workout (where 1 is the best)
                } for workout in workouts
            ],
            'total_points': 0,  # Sum of Standings

        } for participant in participants
    ]

    # Load ParticipantWorkout from Database
    for participant_workout in ParticipantWorkout.objects.all():
        participant_workouts[participant_workout.participant_id - 1]['workout_scores'][
            participant_workout.workout_id - 1]['id'] = participant_workout.id
        participant_workouts[participant_workout.participant_id - 1]['workout_scores'][
            participant_workout.workout_id - 1]['score'] = participant_workout.score

    # Calculate standings per workout.
    for participant_workout in participant_workouts:
        for workout_score in participant_workout['workout_scores']:
            if workout_score['score'] == -1:
                workout_score['standing'] = len(participant_workouts)
            else:
                # Calculate standing for workout versus other participants
                workout_score['standing'] = sum(
                    1 for participant in participant_workouts if participant['workout_scores'][
                        workout_score['workout_id'] - 1]['score'] != -1 and participant['workout_scores'][
                        workout_score['workout_id'] - 1]['score'] < workout_score['score']) + 1

    # For events where scores are tied. Fix standings for following participants.
    # Eg if 2 people are tied for 1st place, the next person should be in 2nd place.
    for participant_workout in participant_workouts:
        for workout_score in participant_workout['workout_scores']:
            if workout_score['score'] != -1:
                for other_participant_workout in participant_workouts:
                    if other_participant_workout['workout_scores'][workout_score['workout_id'] - 1]['score'] == \
                            workout_score['score']:
                        other_participant_workout['workout_scores'][workout_score['workout_id'] - 1]['standing'] = \
                            workout_score['standing']

    # Calculate total points
    for participant_workout in participant_workouts:
        participant_workout['total_points'] = sum(
            workout_score['standing'] for workout_score in participant_workout['workout_scores'])

    # Calculate standings per participant
    for participant_workout in participant_workouts:
        participant_workout['standing'] = sum(
            1 for participant in participant_workouts if
            participant['total_points'] < participant_workout['total_points']) + 1

    # Ensure standings follow a logical order even in the event of tied scores
    participant_workouts = sorted(participant_workouts, key=lambda x: x['total_points'])
    for i in range(len(participant_workouts)):
        if i > 0:
            current_standing = participant_workouts[i]['standing']
            previous_standing = participant_workouts[i - 1]['standing']

            if current_standing - previous_standing > 1:
                participant_workouts[i]['standing'] = previous_standing + 1

    # Change -1 to "no score" for better readability
    for participant_workout in participant_workouts:
        for workout_score in participant_workout['workout_scores']:
            if workout_score['score'] == -1:
                workout_score['score'] = "No Score"

    # Replace , with : in the read-score and ensure it is in the format 00:00
    for participant_workout in participant_workouts:
        for workout_score in participant_workout['workout_scores']:
            if workout_score['score'] != "No Score":
                workout_score['read_score'] = str(workout_score['score']).replace(".", ":")

                for i in range(2 - len(workout_score['read_score'].split(":")[0])):
                    workout_score['read_score'] = "0" + workout_score['read_score']

                for i in range(2 - len(workout_score['read_score'].split(":")[1])):
                    workout_score['read_score'] = workout_score['read_score'] + "0"



    return participant_workouts
