from django.shortcuts import render, redirect
from api.models import Participant, Workout, ParticipantWorkout
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST, require_GET

from api.views import get_workout_scores


@require_GET
def index(request):
    """
    This function is called when the user navigates to the root URL of the website.
    :param request:
    :return:
    """
    # Load Participant Workouts from Database
    participants = Participant.objects.all()
    workouts = Workout.objects.all()

    def get_random_rgb():
        """
        This function returns a random RGB value.
        :return:
        """
        import random
        return 'rgba(' + str(random.randint(0, 255)) + ',' + str(random.randint(0, 255)) + ',' + str(
            random.randint(0, 255)) + ', 0.8)'

    participant_workout_chart_data = []
    for participant in participants:
        rgb = get_random_rgb()
        data = {
            'label': participant.name + ' ' + participant.surname,
            'standing': 0,  # Participants Total Rank (where 1 is the best)
            'data': [
                0 for workout in workouts
            ],
            'backgroundColor': rgb,
            'borderColor': rgb,
        }

        participant_workout_chart_data.append(data)

    # Load ParticipantWorkout from Database
    for participant_workout in ParticipantWorkout.objects.all():
        participant_workout_chart_data[participant_workout.participant_id - 1]['data'][
            participant_workout.workout_id - 1] = participant_workout.score

    




    return render(request, 'index.html', {
        'participant_workout_chart_data': participant_workout_chart_data,
        'workouts': [workout.name for workout in workouts]
    })


@require_GET
def participants(request):
    """
    This function is called when the user navigates to the /participants/ URL of the website.
    :param request:
    :return:
    """
    # Load Participants from Database
    participants = Participant.objects.all()

    return render(request, 'participants.html', {
        'participants': participants
    })


@require_GET
def workouts(request):
    """
    This function is called when the user navigates to the /workouts/ URL of the website.
    :param request:
    :return:
    """
    # Load Workouts from Database
    workouts = Workout.objects.all()

    return render(request, 'workouts.html', {
        'workouts': workouts
    })


@require_GET
def scores(request):
    """
    This function is called when the user navigates to the /stats/ URL of the website.
    :param request:
    :return:
    """

    return render(request, 'scores.html', {
        'participant_workouts': get_workout_scores(),
        'workouts': Workout.objects.all()
    })


@require_POST
def save_score(request):
    """
    This function is called when the user submits the score form.
    :param request:
    :return:
    """

    # Get input data
    participant_id = request.POST.get('participant_id', None)
    workout_id = request.POST.get('workout_id', None)
    score = request.POST.get('score', None)

    # Validate input data
    if not participant_id or not workout_id or not score:
        return JsonResponse({'status': 400, 'message': 'Invalid input data'})

    # Validate score
    try:
        score = float(score)

        # Score must be a positive number
        if score < 0:
            return JsonResponse({'status': 400, 'message': 'Invalid score'})

        # Decimal part of the score must be less than 60
        if score % 1 >= 60:
            return JsonResponse({'status': 400, 'message': 'Invalid score'})

    except ValueError:
        return JsonResponse({'status': 400, 'message': 'Invalid score'})

    # Create ParticipantWorkout if it does not exist
    participant_workout_query = ParticipantWorkout.objects.filter(participant_id=participant_id, workout_id=workout_id)
    if not participant_workout_query.exists():
        participant_workout = ParticipantWorkout(participant_id=participant_id, workout_id=workout_id,
                                                 score=float(score))
        participant_workout.save()
    else:
        participant_workout = participant_workout_query.get()
        # Save score value as MM:SS

        participant_workout.save()

    return JsonResponse({'status': 200, 'message': 'Score saved successfully'})


@require_GET
def participant_form(request, participant_id=None):
    """
    This function is called when the user navigates to the /participant_form/ URL of the website.
    :param request:
    :return:
    """
    participant = None
    if participant_id:
        participant = Participant.objects.get(id=participant_id)

    return render(request, 'participant_form.html', {
        'participant': participant
    })


@require_GET
def workout_form(request, workout_id=None):
    """
    This function is called when the user navigates to the /workout_form/ URL of the website.
    :param request:
    :param workout_id:
    :return:
    """
    # Get Workout from Database
    workout = None
    if workout_id:
        workout = Workout.objects.get(id=workout_id)

    return render(request, 'workout_form.html', {
        'workout': workout
    })


@require_POST
def save_workout(request):
    """
    This function is called when the user submits the workout form.
    :param request:
    :return:
    """
    # Get input data
    workout_id = request.POST.get('workout_id', None)
    workout_name = request.POST.get('workout_name', None)
    workout_description = request.POST.get('workout_description', None)

    # Validate input data
    if not workout_name or not workout_description:
        return HttpResponse("Invalid input data")

    # Validate length of workout_name and workout_description
    if len(workout_name) > 100 or len(workout_description) > 5000:
        return HttpResponse("Character limit exceeded")

    # Save Workout to Database
    if workout_id:
        workout = Workout.objects.get(id=workout_id)
        workout.name = workout_name
        workout.description = workout_description
        workout.save()
    else:
        workout = Workout(name=workout_name, description=workout_description)
        workout.save()

    return redirect('/workouts/')


@require_POST
def save_participant(request):
    """
    This function is called when the user submits the participant form.
    :param request:
    :return:
    """

    # Get input data
    participant_id = request.POST.get('participant_id', None)
    participant_name = request.POST.get('participant_name', None)
    participant_surname = request.POST.get('participant_surname', None)
    participant_email = request.POST.get('participant_email', None)
    participant_phone = request.POST.get('participant_phone', None)

    # Validate input data
    if not participant_name or not participant_surname or not participant_email or not participant_phone:
        return HttpResponse("Invalid input data")

    # Validate length of participant_name and participant_surname
    if len(participant_name) > 100 or len(participant_surname) > 100 or len(participant_email) > 100 or len(
            participant_phone) > 20:
        return HttpResponse("Character limit exceeded")

    # Save Participant to Database
    if participant_id:
        participant = Participant.objects.get(id=participant_id)
        participant.name = participant_name
        participant.surname = participant_surname
        participant.email = participant_email
        participant.phone = participant_phone
        participant.save()
    else:
        participant = Participant(name=participant_name, surname=participant_surname, email=participant_email,
                                  phone=participant_phone)
        participant.save()

    return redirect('/participants/')
