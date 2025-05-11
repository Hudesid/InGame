from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from . import serializers, versioning, paginations
from apps.users.custom_response_decorator import custom_response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter


@custom_response('comment_list_create')
class CommentListCreateAPIView(ListCreateAPIView):
    queryset = serializers.Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    versioning_class = versioning.CustomHeaderVersioning
    pagination_class = paginations.CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['username', 'comment_uz', 'comment_ru', 'description_uz', 'description_ru']
    ordering_fields = ['created_at', 'updated_at']
    filterset_fields = ['created_at', 'updated_at']


@custom_response("comment_detail")
class CommentRetrieveAPIView(RetrieveAPIView):
    queryset = serializers.Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    versioning_class = versioning.CustomHeaderVersioning


@custom_response('product_comment_list_create')
class ProductCommentListCreateAPIView(ListCreateAPIView):
    queryset = serializers.ProductComment.objects.all()
    serializer_class = serializers.ProductCommentSerializer
    versioning_class = versioning.CustomHeaderVersioning
    pagination_class = paginations.CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['username', 'comment']
    ordering_fields = ['created_at', 'updated_at']
    filterset_fields = ['created_at', 'updated_at', 'rating', 'product']


@custom_response('desktop_comment_list_create')
class DesktopCommentListCreateAPIView(ListCreateAPIView):
    queryset = serializers.DesktopComment.objects.all()
    serializer_class = serializers.DesktopCommentSerializer
    versioning_class = versioning.CustomHeaderVersioning
    pagination_class = paginations.CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['username', 'comment']
    ordering_fields = ['created_at', 'updated_at']
    filterset_fields = ['created_at', 'updated_at', 'rating', 'desktop']