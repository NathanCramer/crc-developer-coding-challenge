from django.shortcuts import render, redirect
from api.models import Participant, Workout, ParticipantWorkout
from django.http.response import HttpResponse
from django.views.decorators.http import require_POST, require_GET


@require_GET
def index(request):
    """
    This function is called when the user navigates to the root URL of the website.
    :param request:
    :return:
    """
    return render(request, 'index.html', {})


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
def stats(request):
    """
    This function is called when the user navigates to the /stats/ URL of the website.
    :param request:
    :return:
    """
    # Load Participant Workouts from Database
    participant_workouts = ParticipantWorkout.objects.all()

    return render(request, 'stats.html', {
        'participant_workouts': participant_workouts
    })


@require_GET
def participant_form(request):
    """
    This function is called when the user navigates to the /participant_form/ URL of the website.
    :param request:
    :return:
    """
    return render(request, 'participant_form.html', {})


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
