from django.urls import path
from .views import BrandListAPIView, BrandRetrieveAPIView


urlpatterns = [
    path('brands/', BrandListAPIView.as_view(), name='brands'),
    path('brand/<int:pk>/', BrandRetrieveAPIView.as_view(), name='brand')
]