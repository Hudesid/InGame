from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import Credit, CreditSerializer
from .paginations import CustomPageNumberPagination
from .versioning import CustomHeaderVersioning
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from apps.users.custom_response_decorator import custom_response


@custom_response('credit_list')
class CreditListAPIView(ListAPIView):
    queryset = Credit.objects.all()
    serializer_class = CreditSerializer
    pagination_class = CustomPageNumberPagination
    versioning_class = CustomHeaderVersioning
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['created_at', 'updated_at', 'months']
    filterset_fields = ['months', 'bank_credit']


@custom_response('credit_detail')
class CreditRetrieveAPIView(RetrieveAPIView):
    queryset = Credit.objects.all()
    serializer_class = CreditSerializer
    versioning_class = CustomHeaderVersioning



