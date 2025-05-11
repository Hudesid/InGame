from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import Catalog, CatalogSerializer
from .versioning import CustomHeaderVersioning
from .paginations import CustomPageNumberPagination
from apps.users.custom_response_decorator import custom_response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


@custom_response('catalog_list')
class CatalogListAPIView(ListAPIView):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer
    versioning_class = CustomHeaderVersioning
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name_uz', 'name_ru']
    ordering_fields = ['created_at', 'updated_at']
    filterset_fields = ['created_at', 'updated_at', 'type']


@custom_response('catalog_detail')
class CatalogRetrieveAPIView(RetrieveAPIView):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer
    versioning_class = CustomHeaderVersioning