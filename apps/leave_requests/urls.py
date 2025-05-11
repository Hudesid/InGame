from django.urls import path
from .views import LeaveRequestCreateAPIView


urlpatterns = [path('leave-a-request/', LeaveRequestCreateAPIView.as_view(), name='leave_request')]