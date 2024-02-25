from django.urls import path
from .views import TeamListAPIView, TeamCreateAPIView, TeamUpdateAPIView, DestroyAPIView
from . import views

urlpatterns = [
    path('get/achievements/', TeamListAPIView.as_view(), name='team-list'),
    path('post/achievements/', TeamCreateAPIView.as_view(), name='team-create'),
    path('put/achievements/<id>/', TeamUpdateAPIView.as_view(), name='team-update'),
    path('delete/achievements/<id>/', DestroyAPIView.as_view(), name='team-destroy'),
]
