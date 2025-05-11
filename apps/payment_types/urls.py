from django.urls import path
from .views import PaymentTypeListAPIView, PaymentTypeRetrieveAPIView


urlpatterns = [
    path('payments/', PaymentTypeListAPIView.as_view(), name='payments'),
    path('payment/<int:pk>/', PaymentTypeRetrieveAPIView.as_view(), name='payment'),
]