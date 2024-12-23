from rest_framework import generics
from .serializers import KeyboardSerializer, SwitchSerializer
from .models import Keyboard, Switch
from accounts.permissions import FullCRUDPermission


# if method = get, it lists all the keyboards
# if method = put, it creates a keyboard
class KeyboardListCreateView(generics.ListCreateAPIView):
    serializer_class = KeyboardSerializer
    permission_classes = [FullCRUDPermission]

    def get_queryset(self):
        return Keyboard.objects.all()


class KeyboardDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = KeyboardSerializer
    permission_classes = [FullCRUDPermission]

    def get_queryset(self):
        return Keyboard.objects.all()


class SwitchListCreateView(generics.ListCreateAPIView):
    serializer_class = SwitchSerializer
    permission_classes = [FullCRUDPermission]

    def get_queryset(self):
        return Switch.objects.all()


class SwitchDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SwitchSerializer
    permission_classes = [FullCRUDPermission]

    def get_queryset(self):
        return Switch.objects.all()
