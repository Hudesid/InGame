from django.urls import path
from .views import BannerListAPIView, BannerRetrieveAPIView


urlpatterns = [
    path('banners/', BannerListAPIView.as_view(), name='banners'),
    path('banner/<int:pk>/', BannerRetrieveAPIView.as_view(), name='banner')
]