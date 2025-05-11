from rest_framework.generics import CreateAPIView
from .serializers import LeaveRequest, LeaveRequestSerializer
from apps.users.custom_response_decorator import custom_response
from .versioning import CustomHeaderVersioning


@custom_response('leave_request_create')
class LeaveRequestCreateAPIView(CreateAPIView):
    queryset = LeaveRequest.objects.all()
    serializer_class = LeaveRequestSerializer
    versioning_class = CustomHeaderVersioning

