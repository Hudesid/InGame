from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import serializers
from .versioning import CustomHeaderVersioning
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .paginations import CustomPageNumberPagination
from apps.users.custom_response_decorator import custom_response


@custom_response("login")
class LoginAPIView(TokenObtainPairView):
    serializer_class = serializers.CustomTokenObtainSerializer
    versioning_class = CustomHeaderVersioning

    def post(self, request, *args, **kwargs):
        version = self.request.version
        if version == '1.0':
            return super().post(request, *args, **kwargs)


@custom_response("refresh")
class TokenRefreshAPIView(TokenRefreshView):
    versioning_class = CustomHeaderVersioning


@custom_response("user")
class UserModelViewSet(ModelViewSet):
    queryset = serializers.User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]
    versioning_class = CustomHeaderVersioning
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['first_name', 'last_name', 'email', 'phone']
    ordering_fields = ['date_joined', 'updated_at', 'is_active']
    filterset_fields = ['date_joined', 'updated_at', 'role', 'phone', 'is_active', 'is_staff', 'is_superuser']


@custom_response("attribute")
class AttributeModelViewSet(ModelViewSet):
    queryset = serializers.Attribute.objects.all()
    serializer_class = serializers.AttributeSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]
    versioning_class = CustomHeaderVersioning
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['type_uz', 'type_ru']
    ordering_fields = ['category', 'updated_at', 'created_at', 'value']
    filterset_fields = ['created_at', 'updated_at', 'value', 'category']


@custom_response("role")
class RoleModelViewSet(ModelViewSet):
    queryset = serializers.Role.objects.all()
    serializer_class = serializers.RoleSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]
    versioning_class = CustomHeaderVersioning
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['created_at', 'updated_at']
    filterset_fields = ['created_at', 'updated_at']


@custom_response("credit")
class CreditModelViewSet(ModelViewSet):
    queryset = serializers.Credit.objects.all()
    serializer_class = serializers.CreditSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]
    versioning_class = CustomHeaderVersioning
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['created_at', 'updated_at', 'months']
    filterset_fields = ['months', 'bank_credit']


@custom_response("product")
class ProductModelViewSet(ModelViewSet):
    queryset = serializers.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]
    versioning_class = CustomHeaderVersioning
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name_uz', 'name_ru', 'description_uz', 'description_ru']
    ordering_fields = ['created_at', 'updated_at', 'statuses']
    filterset_fields = ['price', 'category', 'brand', 'discount', 'attributes', 'statuses', 'type']


@custom_response("product_type")
class ProductTypeModelViewSet(ModelViewSet):
    queryset = serializers.ProductType.objects.all()
    serializer_class = serializers.ProductTypeSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]
    versioning_class = CustomHeaderVersioning
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['created_at', 'updated_at']
    filterset_fields = ['created_at', 'updated_at']


@custom_response("category")
class CategoryModelViewSet(ModelViewSet):
    queryset = serializers.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [IsAdminUser, IsAuthenticated]
    versioning_class = CustomHeaderVersioning
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name_uz', 'name_ru', 'description_uz', 'description_ru']
    ordering_fields = ['created_at', 'updated_at']
    filterset_fields = ['created_at', 'updated_at']


@custom_response("desktop")
class DesktopModelViewSet(ModelViewSet):
    queryset = serializers.Desktop.objects.all()
    serializer_class = serializers.DesktopSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]
    versioning_class = CustomHeaderVersioning
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name_uz', 'name_ru', 'description_uz', 'description_ru']
    ordering_fields = ['created_at', 'updated_at']
    filterset_fields = ['created_at', 'updated_at', 'type', 'desktop_types', 'attributes', 'price', 'products', 'statuses']


@custom_response("desktop_image")
class DesktopImageModelViewSet(ModelViewSet):
    queryset = serializers.DesktopImage.objects.all()
    serializer_class = serializers.DesktopImageSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]
    versioning_class = CustomHeaderVersioning
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['created_at', 'updated_at']
    filterset_fields = ['created_at', 'updated_at', 'desktop']


@custom_response("product_image")
class ProductImageModelViewSet(ModelViewSet):
    queryset = serializers.ProductImage.objects.all()
    serializer_class = serializers.ProductImageSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]
    versioning_class = CustomHeaderVersioning
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['created_at', 'updated_at']
    filterset_fields = ['created_at', 'updated_at', 'product']


@custom_response("game")
class GameModelViewSet(ModelViewSet):
    queryset = serializers.Game.objects.all()
    serializer_class = serializers.GameSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]
    versioning_class = CustomHeaderVersioning
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['game_name']
    ordering_fields = ['created_at', 'updated_at']
    filterset_fields = ['created_at', 'updated_at']


@custom_response("fps")
class FpsModelViewSet(ModelViewSet):
    queryset = serializers.Fps.objects.all()
    serializer_class = serializers.FpsSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]
    versioning_class = CustomHeaderVersioning
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['created_at', 'updated_at', 'game_fps']
    filterset_fields = ['created_at', 'updated_at', 'game', 'desktop', 'game_fps']


@custom_response("desktop_type")
class DesktopTypeModelViewSet(ModelViewSet):
    queryset = serializers.DesktopType.objects.all()
    serializer_class = serializers.DesktopTypeSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]
    versioning_class = CustomHeaderVersioning
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['created_at', 'updated_at']
    filterset_fields = ['created_at', 'updated_at']


@custom_response("order")
class OrderModelViewSet(ModelViewSet):
    queryset = serializers.Order.objects.all()
    serializer_class = serializers.OrderSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]
    versioning_class = CustomHeaderVersioning
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['customer_name', 'customer_phone', 'address', 'comment']
    ordering_fields = ['created_at', 'updated_at', 'status']
    filterset_fields = ['created_at', 'updated_at', 'status', 'address', 'customer_phone', 'delivery_method', 'total_price']


@custom_response("order_desktop")
class OrderDesktopItemModelViewSet(ModelViewSet):
    queryset = serializers.OrderDesktopItem.objects.all()
    serializer_class = serializers.OrderDesktopItemSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]
    versioning_class = CustomHeaderVersioning
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['created_at', 'updated_at', 'status']
    filterset_fields = ['created_at', 'updated_at', 'desktop', 'order', 'quantity', 'credit', 'credit_term', 'edit_product']


@custom_response("order_product")
class OrderProductItemModelViewSet(ModelViewSet):
    queryset = serializers.OrderProductItem.objects.all()
    serializer_class = serializers.OrderProductItemSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]
    versioning_class = CustomHeaderVersioning
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['created_at', 'updated_at', 'status']
    filterset_fields = ['created_at', 'updated_at', 'product', 'order', 'quantity', 'credit', 'credit_term']


@custom_response("delivery_method")
class DeliveryMethodModelViewSet(ModelViewSet):
    queryset = serializers.DeliveryMethod.objects.all()
    serializer_class = serializers.DeliveryMethodSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]
    versioning_class = CustomHeaderVersioning
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name_uz', 'name_ru']
    ordering_fields = ['created_at', 'updated_at']
    filterset_fields = ['created_at', 'updated_at', 'price', 'estimated_delivery_time']


@custom_response("payment_type")
class PaymentTypeModelViewSet(ModelViewSet):
    queryset = serializers.PaymentType.objects.all()
    serializer_class = serializers.PaymentTypeSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]
    versioning_class = CustomHeaderVersioning
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['created_at', 'updated_at']
    filterset_fields = ['created_at', 'updated_at']


@custom_response("banner")
class BannerModelViewSet(ModelViewSet):
    queryset = serializers.Banner.objects.all()
    serializer_class = serializers.BannerSerializer
    versioning_class = CustomHeaderVersioning
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name_uz', 'name_ru', 'description_uz', 'description_ru']
    ordering_fields = ['created_at', 'updated_at']
    filterset_fields = ['created_at', 'updated_at', 'url']


@custom_response("comment")
class CommentModelViewSet(ModelViewSet):
    queryset = serializers.Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    versioning_class = CustomHeaderVersioning
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['username', 'comment_uz', 'comment_ru', 'description_uz', 'description_ru']
    ordering_fields = ['created_at', 'updated_at']
    filterset_fields = ['created_at', 'updated_at']


@custom_response("product_comment")
class ProductCommentModelViewSet(ModelViewSet):
    queryset = serializers.ProductComment.objects.all()
    serializer_class = serializers.ProductCommentSerializer
    versioning_class = CustomHeaderVersioning
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['username', 'comment']
    ordering_fields = ['created_at', 'updated_at']
    filterset_fields = ['created_at', 'updated_at', 'rating', 'product']


@custom_response("desktop_comment")
class DesktopCommentModelViewSet(ModelViewSet):
    queryset = serializers.DesktopComment.objects.all()
    serializer_class = serializers.DesktopCommentSerializer
    versioning_class = CustomHeaderVersioning
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['username', 'comment']
    ordering_fields = ['created_at', 'updated_at']
    filterset_fields = ['created_at', 'updated_at', 'rating', 'desktop']


@custom_response("status")
class StatusModelViewSet(ModelViewSet):
    queryset = serializers.Status.objects.all()
    serializer_class = serializers.StatusSerializer
    versioning_class = CustomHeaderVersioning
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['created_at', 'updated_at']
    filterset_fields = ['created_at', 'updated_at']


@custom_response("service")
class ServiceModelViewSet(ModelViewSet):
    queryset = serializers.Service.objects.all()
    serializer_class = serializers.ServiceSerializer
    versioning_class = CustomHeaderVersioning
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name', 'phone']
    ordering_fields = ['created_at', 'updated_at']
    filterset_fields = ['created_at', 'updated_at', 'status', 'price', 'other_services', 'type']


@custom_response("service_name")
class ServiceNameModelViewSet(ModelViewSet):
    queryset = serializers.ServiceName.objects.all()
    serializer_class = serializers.ServiceNameSerializer
    versioning_class = CustomHeaderVersioning
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['created_at', 'updated_at']
    filterset_fields = ['created_at', 'updated_at', 'service']


@custom_response("brand")
class BrandModelViewSet(ModelViewSet):
    queryset = serializers.Brand.objects.all()
    serializer_class = serializers.BrandSerializer
    versioning_class = CustomHeaderVersioning
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['created_at', 'updated_at']
    filterset_fields = ['created_at', 'updated_at']


@custom_response("new")
class NewModelViewSet(ModelViewSet):
    queryset = serializers.New.objects.all()
    serializer_class = serializers.NewSerializer
    versioning_class = CustomHeaderVersioning
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['title_uz', 'title_ru', 'description_uz', 'description_ru', 'youtube_url']
    ordering_fields = ['created_at', 'updated_at']
    filterset_fields = ['created_at', 'updated_at']


@custom_response("trade_in")
class TradeInModelViewSet(ModelViewSet):
    queryset = serializers.TradeIn.objects.all()
    serializer_class = serializers.TradeInSerializer
    versioning_class = CustomHeaderVersioning
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name', 'phone', 'telegram_nik']
    ordering_fields = ['created_at', 'updated_at', 'status']
    filterset_fields = ['created_at', 'updated_at', 'status', 'config']


@custom_response("catalog")
class CatalogModelViewSet(ModelViewSet):
    queryset = serializers.Catalog.objects.all()
    serializer_class = serializers.CatalogSerializer
    versioning_class = CustomHeaderVersioning
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name_uz', 'name_ru']
    ordering_fields = ['created_at', 'updated_at']
    filterset_fields = ['created_at', 'updated_at', 'type']


@custom_response("leave_request")
class LeaveRequestModelViewSet(ModelViewSet):
    queryset = serializers.LeaveRequest.objects.all()
    serializer_class = serializers.LeaveRequestSerializer
    versioning_class = CustomHeaderVersioning
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name', 'phone', 'operator_commit']
    ordering_fields = ['created_at', 'updated_at', 'status']
    filterset_fields = ['created_at', 'updated_at', 'status']