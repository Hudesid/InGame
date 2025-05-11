from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import New, NewSerializer
from apps.users.custom_response_decorator import custom_response
from .versioning import CustomHeaderVersioning
from .paginations import CustomPageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


@custom_response('new_list')
class NewListAPIView(ListAPIView):
    queryset = New.objects.all()
    serializer_class = NewSerializer
    versioning_class = CustomHeaderVersioning
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['title_uz', 'title_ru', 'description_uz', 'description_ru', 'youtube_url']
    ordering_fields = ['created_at', 'updated_at']
    filterset_fields = ['created_at', 'updated_at']


@custom_response('new_detail')
class NewRetrieveAPIView(RetrieveAPIView):
    queryset = New.objects.all()
    serializer_class = NewSerializer
    versioning_class = CustomHeaderVersioning