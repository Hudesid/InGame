from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import Category, CategorySerializer
from .paginations import CustomPageNumberPagination
from .versioning import CustomHeaderVersioning
from apps.users.custom_response_decorator import custom_response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


@custom_response('category_list')
class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CustomPageNumberPagination
    versioning_class = CustomHeaderVersioning
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name_uz', 'name_ru', 'description_uz', 'description_ru']
    ordering_fields = ['created_at', 'updated_at']
    filterset_fields = ['created_at', 'updated_at']


@custom_response('category_detail')
class CategoryRetrieveAPIView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    versioning_class = CustomHeaderVersioning