from .models import *
from rest_framework import serializers


# Participant serializer
class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = '__all__'


# Workout serializer
class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = '__all__'


# ParticipantWorkout serializer
class ParticipantWorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParticipantWorkout
        fields = '__all__'
