from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import ProductSerializer, Product
from .versioning import CustomHeaderVersioning
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .paginations import CustomPageNumberPagination
from apps.users.custom_response_decorator import custom_response


@custom_response('product_list')
class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    versioning_class = CustomHeaderVersioning
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name_uz', 'name_ru', 'description_uz', 'description_ru']
    ordering_fields = ['created_at', 'updated_at', 'statuses']
    filterset_fields = ['price', 'category', 'brand', 'discount', 'attributes', 'statuses', 'type']



@custom_response('product_detail')
class ProductRetrieveAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    versioning_class = CustomHeaderVersioning
