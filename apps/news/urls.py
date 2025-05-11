from django.urls import path
from .views import NewListAPIView, NewRetrieveAPIView


urlpatterns = [
    path('news/', NewListAPIView.as_view(), name='news'),
    path('new/<int:pk>/', NewRetrieveAPIView.as_view(), name='new'),
]