from django.urls import path
from .views import GameListAPIView, GameRetrieveAPIView


urlpatterns = [
    path('games/', GameListAPIView.as_view(), name='games'),
    path('game/<int:pk>/', GameRetrieveAPIView.as_view(), name='game'),
]