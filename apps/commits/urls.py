from django.urls import path
from .views import CommentListCreateAPIView, CommentRetrieveAPIView,DesktopCommentListCreateAPIView, ProductCommentListCreateAPIView


urlpatterns = [
    path('commit-from-clients/', CommentListCreateAPIView.as_view(), name='comments'),
    path('commit-from-clients/<int:pk>/', CommentRetrieveAPIView.as_view(), name='comment_detail'),
    path('desktop-comments/', DesktopCommentListCreateAPIView.as_view(), name='desktop_comments'),
    path('product-comments/', ProductCommentListCreateAPIView.as_view(), name='product_comments'),
]