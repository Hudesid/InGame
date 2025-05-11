from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import Banner, BannerSerializer
from apps.users.custom_response_decorator import custom_response
from .paginations import CustomPageNumberPagination
from .versioning import CustomHeaderVersioning
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


@custom_response('banner_list')
class BannerListAPIView(ListAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
    versioning_class = CustomHeaderVersioning
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name_uz', 'name_ru', 'description_uz', 'description_ru']
    ordering_fields = ['created_at', 'updated_at']
    filterset_fields = ['created_at', 'updated_at', 'url']


@custom_response('banner_detail')
class BannerRetrieveAPIView(RetrieveAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
    versioning_class = CustomHeaderVersioning