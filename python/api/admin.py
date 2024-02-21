from django.contrib import admin
from .models import *


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at', 'age', 'gender', 'height', 'weight', 'bmi')


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')


@admin.register(ParticipantWorkout)
class ParticipantWorkoutAdmin(admin.ModelAdmin):
    list_display = ('workout', 'participant', 'score', 'created_at')

