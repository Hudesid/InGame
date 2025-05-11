from django.urls import path
from .views import DesktopListAPIView, DesktopRetrieveAPIView


urlpatterns = [
    path('desktops/', DesktopListAPIView.as_view(), name='desktops'),
    path('desktop/<str:slug>/', DesktopRetrieveAPIView.as_view(), name='desktop'),
]