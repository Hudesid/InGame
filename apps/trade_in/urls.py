from django.urls import path
from .views import TradeInCreateAPIView


urlpatterns = [
    path('tradeIn/', TradeInCreateAPIView.as_view(), name='trade_in_create'),
]