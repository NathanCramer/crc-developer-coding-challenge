from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import *
from .models import *
from .views import get_workout_scores


# Participant View Set
class ParticipantViewSet(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer


# Workout View Set
class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer


# ParticipantWorkout View Set
class ParticipantWorkoutViewSet(viewsets.ModelViewSet):
    queryset = ParticipantWorkout.objects.all()
    serializer_class = ParticipantWorkoutSerializer


class ScoreViewSet(viewsets.ViewSet):
    def list(self, request):
        return Response(get_workout_scores())
