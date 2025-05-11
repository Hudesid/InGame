from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import ProductTypeSerializer, ProductType
from apps.users.custom_response_decorator import custom_response
from .versioning import CustomHeaderVersioning
from .paginations import CustomPageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


@custom_response('product_type_list')
class ProductTypeListAPIView(ListAPIView):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
    versioning_class = CustomHeaderVersioning
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['created_at', 'updated_at']
    filterset_fields = ['created_at', 'updated_at']


@custom_response('product_type_detail')
class ProductTypeRetrieveAPIView(RetrieveAPIView):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
    versioning_class = CustomHeaderVersioning