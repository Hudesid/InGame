from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import DesktopSerializer, Desktop
from apps.users.custom_response_decorator import custom_response
from .versioning import CustomHeaderVersioning
from .paginations import CustomPageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


@custom_response('desktop_list')
class DesktopListAPIView(ListAPIView):
    queryset = Desktop.objects.all()
    serializer_class = DesktopSerializer
    versioning_class = CustomHeaderVersioning
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name_uz', 'name_ru', 'description_uz', 'description_ru']
    ordering_fields = ['created_at', 'updated_at']
    filterset_fields = ['created_at', 'updated_at', 'type', 'desktop_types', 'attributes', 'price', 'products', 'statuses']


@custom_response('desktop_detail')
class DesktopRetrieveAPIView(RetrieveAPIView):
    queryset = Desktop.objects.all()
    serializer_class = DesktopSerializer
    versioning_class = CustomHeaderVersioning