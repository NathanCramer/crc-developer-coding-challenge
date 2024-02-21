# app_name/schema.py
import graphene
from graphene_django import DjangoObjectType
from .models import *


# Types
class ParticipantType(DjangoObjectType):
    class Meta:
        model = Participant
        fields = '__all__'


class WorkoutType(DjangoObjectType):
    class Meta:
        model = Workout
        fields = '__all__'


class ParticipantWorkoutType(DjangoObjectType):
    class Meta:
        model = ParticipantWorkout
        fields = '__all__'


# Queries
class Query(graphene.ObjectType):
    participants = graphene.List(ParticipantType)
    workouts = graphene.List(WorkoutType)
    participant_workouts = graphene.List(ParticipantWorkoutType)

    def resolve_participants(root, info, **kwargs):
        return Participant.objects.all()

    def resolve_workouts(root, info, **kwargs):
        return Workout.objects.all()

    def resolve_participant_workouts(root, info, **kwargs):
        return ParticipantWorkout.objects.all()


schema = graphene.Schema(query=Query)
