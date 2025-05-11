from rest_framework.generics import CreateAPIView
from .serializers import ServiceSerializer, Service
from .versioning import CustomHeaderVersioning
from apps.users.custom_response_decorator import custom_response


@custom_response('service_create')
class ServiceCreateAPIView(CreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    versioning_class = CustomHeaderVersioning
