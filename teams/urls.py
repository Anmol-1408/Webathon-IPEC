from django.urls import path
from .views import TeamListAPIView, TeamCreateAPIView, TeamRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('get/achievements/', TeamListAPIView.as_view(), name='team-list'),
    path('post/achievements/', TeamCreateAPIView.as_view(), name='team-create'),
    path('put/achievements/<int:pk>/', TeamRetrieveUpdateDestroyAPIView.as_view(), name='team-retrieve-update-destroy'),
]
