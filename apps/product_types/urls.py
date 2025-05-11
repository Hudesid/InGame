from django.urls import path
from .views import ProductTypeListAPIView, ProductTypeRetrieveAPIView


urlpatterns = [
    path('product-types/', ProductTypeListAPIView.as_view(), name='product_types'),
    path('product-type/<int:pk>/', ProductTypeRetrieveAPIView.as_view(), name='product_type'),
]