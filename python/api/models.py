from django.db import models


class Participant(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    # Metadata
    age = models.IntegerField()
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        # ('O', 'Other'), # Jk... No helicopters here
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    bmi = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name


class Workout(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ParticipantWorkout(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE, related_name='workouts')
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name='participants')
    created_at = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField()

    def __str__(self):
        return f'{self.participant.name} - {self.workout.name}'
