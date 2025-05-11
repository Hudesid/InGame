from rest_framework.routers import DefaultRouter
from . import views
from django.urls import path, include

router = DefaultRouter()

router.register(r"users", views.UserModelViewSet, basename="user")
router.register(r"roles", views.RoleModelViewSet, basename="role")
router.register(r"attributes", views.AttributeModelViewSet, basename="attribute")
router.register(r"credits", views.CreditModelViewSet, basename="credit")
router.register(r"products", views.ProductModelViewSet, basename="product")
router.register(r"product-types", views.ProductTypeModelViewSet, basename="product-type")
router.register(r"categories", views.CategoryModelViewSet, basename="category")
router.register(r"desktops", views.DesktopModelViewSet, basename="desktop")
router.register(r"desktop-images", views.DesktopImageModelViewSet, basename="desktop-image")
router.register(r"product-images", views.ProductImageModelViewSet, basename="product-image")
router.register(r"games", views.GameModelViewSet, basename="game")
router.register(r"desktop-fps", views.FpsModelViewSet, basename="game-fps")
router.register(r"desktop-types", views.DesktopTypeModelViewSet, basename="desktop-type")
router.register(r"orders", views.OrderModelViewSet, basename="order")
router.register(r"order-desktop-items", views.OrderDesktopItemModelViewSet, basename="order-desktop-item")
router.register(r"order-product-items", views.OrderProductItemModelViewSet, basename="order-product-item")
router.register(r"delivery-methods", views.DeliveryMethodModelViewSet, basename="delivery-method")
router.register(r"payment-types", views.PaymentTypeModelViewSet, basename="payment-type")
router.register(r"banners", views.BannerModelViewSet, basename="banner")
router.register(r"comments", views.CommentModelViewSet, basename="comment")
router.register(r"product-comments", views.ProductCommentModelViewSet, basename="product-comment")
router.register(r"desktop-comments", views.DesktopCommentModelViewSet, basename="desktop-comment")
router.register(r"statuses", views.StatusModelViewSet, basename="status")
router.register(r"services", views.ServiceModelViewSet, basename="service")
router.register(r"service-names", views.ServiceNameModelViewSet, basename="service-name")
router.register(r"brands", views.BrandModelViewSet, basename="brand")
router.register(r"news", views.NewModelViewSet, basename="new")
router.register(r"tradeIn", views.TradeInModelViewSet, basename="tradeIn")
router.register(r"catalogs", views.CatalogModelViewSet, basename="catalog")
router.register(r"leave-requests", views.LeaveRequestModelViewSet, basename="leave-request")


urlpatterns = [
    path('dashboard/login/', views.LoginAPIView.as_view(), name="login"),
    path('dashboard/refresh/', views.TokenRefreshAPIView.as_view(), name="refresh"),
    path('dashboard/', include(router.urls)),]