from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),

    path('participants/', participants),
    path('workouts/', workouts),
    path('stats/', stats),
    path('participant_form/', participant_form),
    path('workout/add/', workout_form),
    path('workout/edit/<int:workout_id>', workout_form),
    path('workout/save', save_workout),
]
