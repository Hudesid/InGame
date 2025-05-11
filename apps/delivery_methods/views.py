from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import DeliveryMethod, DeliveryMethodSerializer
from apps.users.custom_response_decorator import custom_response
from .versioning import CustomHeaderVersioning
from .paginations import CustomPageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


@custom_response('delivery_method_list')
class DeliveryMethodListAPIView(ListAPIView):
    queryset = DeliveryMethod.objects.all()
    serializer_class = DeliveryMethodSerializer
    versioning_class = CustomHeaderVersioning
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name_uz', 'name_ru']
    ordering_fields = ['created_at', 'updated_at']
    filterset_fields = ['price', 'estimated_delivery_time', 'created_at', 'updated_at']


@custom_response('delivery_method_detail')
class DeliveryMethodRetrieveAPIView(RetrieveAPIView):
    queryset = DeliveryMethod.objects.all()
    serializer_class = DeliveryMethodSerializer
    versioning_class = CustomHeaderVersioning
