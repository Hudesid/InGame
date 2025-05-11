from rest_framework.generics import CreateAPIView
from .serializers import TradeIn, TradeInSerializer
from apps.users.custom_response_decorator import custom_response
from .versioning import CustomHeaderVersioning


@custom_response('trade_in_create')
class TradeInCreateAPIView(CreateAPIView):
    queryset = TradeIn.objects.all()
    serializer_class = TradeInSerializer
    versioning_class = CustomHeaderVersioning