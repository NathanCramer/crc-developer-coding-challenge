from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),

    path('scores/', scores),
    path('update_score/', save_score),

    # Participants
    path('participants/', participants),
    path('participant/add/', participant_form),
    path('participant/edit/<int:participant_id>', participant_form),
    path('participant/save', save_participant),

    # Workouts
    path('workouts/', workouts),
    path('workout/add/', workout_form),
    path('workout/edit/<int:workout_id>', workout_form),
    path('workout/save', save_workout),

    # API
    path('api/', include('api.urls')),
]
