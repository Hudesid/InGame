from django.urls import path
from .views import CatalogListAPIView, CatalogRetrieveAPIView


urlpatterns = [
    path('catalogs/', CatalogListAPIView.as_view(), name='catalogs'),
    path('catalog/<int:pk>/', CatalogRetrieveAPIView.as_view(), name='catalog')
]