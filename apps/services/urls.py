from django.urls import path
from .views import ServiceCreateAPIView


urlpatterns = [
    path('service/', ServiceCreateAPIView.as_view(), name='service_create'),
]