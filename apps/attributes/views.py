from django.db.models import Q
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.users.custom_response_decorator import custom_response
from .serializers import SearchSerializer
from .versioning import CustomHeaderVersioning
from .paginations import CustomPageNumberPagination
from apps.products.serializers import Product, ProductSerializer
from apps.desktops.serializers import Desktop, DesktopSerializer
from apps.brands.serializers import Brand, BrandSerializer
from apps.banners.serializers import Banner, BannerSerializer
from apps.desktops_fps.serializers import Game, GameSerializer
from apps.news.serializers import New, NewSerializer
from apps.credits.serializers import Credit, CreditSerializer


@custom_response("search")
class SearchAPIView(APIView):
    versioning_class = CustomHeaderVersioning
    pagination_class = CustomPageNumberPagination

    def get(self, request, *args, **kwargs):
        version = self.request.version
        if version == '1.0':
            serializer = SearchSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            search_query = serializer.validated_data['q']

            products = Product.objects.filter(
                Q(name_uz__icontains=search_query) |
                Q(name_ru__icontains=search_query) |
                Q(description_uz__icontains=search_query) |
                Q(description_ru__icontains=search_query)
            )

            desktops = Desktop.objects.filter(
                Q(name_uz__icontains=search_query) |
                Q(name_ru__icontains=search_query) |
                Q(description_uz__icontains=search_query) |
                Q(description_ru__icontains=search_query)
            )

            brands = Brand.objects.filter(name__icontains=search_query)
            banners = Banner.objects.filter(
                Q(name_uz__icontains=search_query) |
                Q(name_ru__icontains=search_query) |
                Q(description_uz__icontains=search_query) |
                Q(description_ru__icontains=search_query)
            )
            games = Game.objects.filter(game_name__icontains=search_query)
            news = New.objects.filter(
                Q(title_uz__icontains=search_query) |
                Q(title_ru__icontains=search_query) |
                Q(description_uz__icontains=search_query) |
                Q(description_ru__icontains=search_query)
            )
            credits = Credit.objects.filter(name__icontains=search_query)

            response_data = {
                "products": ProductSerializer(products, many=True).data,
                "desktops": DesktopSerializer(desktops, many=True).data,
                "brands": BrandSerializer(brands, many=True).data,
                "banners": BannerSerializer(banners, many=True).data,
                "games": GameSerializer(games, many=True).data,
                "news": NewSerializer(news, many=True).data,
                "credits": CreditSerializer(credits, many=True).data
            }

            return Response(response_data, status=status.HTTP_200_OK)
