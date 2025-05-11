from rest_framework.generics import CreateAPIView
from .serializers import OrderSerializer, Order
from apps.users.custom_response_decorator import custom_response
from .versioning import CustomHeaderVersioning


@custom_response('order_create')
class OrderCreateAPIView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    versioning_class = CustomHeaderVersioning



