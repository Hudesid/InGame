from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import Brand, BrandSerializer
from .versioning import CustomHeaderVersioning
from .paginations import CustomPageNumberPagination
from apps.users.custom_response_decorator import custom_response
from rest_framework.filters import SearchFilter, OrderingFilter


@custom_response('brand_list')
class BrandListAPIView(ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    versioning_class = CustomHeaderVersioning
    pagination_class = CustomPageNumberPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['created_at', 'updated_at']


@custom_response('brand_detail')
class BrandRetrieveAPIView(RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    versioning_class = CustomHeaderVersioning


