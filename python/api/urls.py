from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from rest_framework import routers
from . import viewsets
from . import views
from .schema import schema

router = routers.DefaultRouter()
router.register(r'participants', viewsets.ParticipantViewSet)
router.register(r'workouts', viewsets.WorkoutViewSet)
router.register(r'participant_workouts', viewsets.ParticipantWorkoutViewSet)
router.register(r'scores', viewsets.ScoreViewSet, basename='score')

urlpatterns = [
    path('docs', views.index, name='docs'),
    path('', include(router.urls)),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
]
