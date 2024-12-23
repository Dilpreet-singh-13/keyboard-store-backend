from .models import CustomUser
from .serializers import UserSerializer
from rest_framework import generics, status, serializers
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from . permissions import AdminPermissions
from rest_framework.exceptions import NotFound

class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return CustomUser.objects.all()

class MakeStaffView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AdminPermissions]
    lookup_field = "username"
    
    def get_queryset(self):
        return CustomUser.objects.filter(user_role="customer")
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        
        if instance.user_role != "customer":
            return Response(
                {"detail": "Only customers can be promoted to staff."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        instance.user_role = "staff"
        instance.save()
        
        return Response(
            {
                "detail": f"User {instance.username} promoted to staff."
            },
            status=status.HTTP_200_OK,
        )
    
    def get_object(self):
        username = self.request.data.get("username")
        if not username:
            raise serializers.ValidationError({"detail": "Username is required."})
        
        try:
            return CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist:
            raise NotFound({"detail": "Customer with given username does not exist."})