from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import PaymentType, PaymentTypesSerializer
from .versioning import CustomHeaderVersioning
from .paginations import CustomPageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from apps.users.custom_response_decorator import custom_response


@custom_response('payment_type_list')
class PaymentTypeListAPIView(ListAPIView):
    queryset = PaymentType.objects.all()
    serializer_class = PaymentTypesSerializer
    versioning_class = CustomHeaderVersioning
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['created_at', 'updated_at']
    filterset_fields = ['created_at', 'updated_at']


@custom_response('payment_type_detail')
class PaymentTypeRetrieveAPIView(RetrieveAPIView):
    queryset = PaymentType.objects.all()
    serializer_class = PaymentTypesSerializer
    versioning_class = CustomHeaderVersioning
