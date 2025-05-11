from django.urls import path
from .views import DesktopListAPIView, DesktopRetrieveAPIView


urlpatterns = [
    path('desktops/', DesktopListAPIView.as_view(), name='desktops'),
    path('desktop/<int:pk>/', DesktopRetrieveAPIView.as_view(), name='desktop'),
]