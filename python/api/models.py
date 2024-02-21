from django.db import models


class Participant(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ParticipantWorkout(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE, related_name='workouts')
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name='participants')
    created_at = models.DateTimeField(auto_now_add=True)
    score = models.FloatField()

    def __str__(self):
        return f'{self.participant.name} - {self.workout.name}'
