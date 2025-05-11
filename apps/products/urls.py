from django.urls import path
from .views import ProductListAPIView, ProductRetrieveAPIView


urlpatterns = [
    path('products/', ProductListAPIView.as_view(), name='products'),
    path('product/<str:slug>/', ProductRetrieveAPIView.as_view(), name='product'),
]