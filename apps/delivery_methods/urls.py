from django.urls import path
from .views import DeliveryMethodListAPIView, DeliveryMethodRetrieveAPIView


urlpatterns = [
    path('delivery-methods/', DeliveryMethodListAPIView.as_view(), name='delivery_methods'),
    path('delivery-method/<int:pk>/', DeliveryMethodRetrieveAPIView.as_view(), name='delivery_method'),
]