from django.urls import path
from .views import CreditListAPIView, CreditRetrieveAPIView


urlpatterns = [
    path('credits/', CreditListAPIView.as_view(), name='credits'),
    path('credit/<int:pk>/', CreditRetrieveAPIView.as_view(), name='credit'),
]