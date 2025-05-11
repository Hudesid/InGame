from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import GameSerializer, Game
from .paginations import CustomPageNumberPagination
from .versioning import CustomHeaderVersioning
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from apps.users.custom_response_decorator import custom_response


@custom_response('game_list')
class GameListAPIView(ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    pagination_class = CustomPageNumberPagination
    versioning_class = CustomHeaderVersioning
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['game_name']
    ordering_fields = ['created_at', 'updated_at']
    filterset_fields = ['created_at', 'updated_at', 'fps']


@custom_response('game_detail')
class GameRetrieveAPIView(RetrieveAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    versioning_class = CustomHeaderVersioning