from django.urls import path
from .views import CreateUserView, MakeStaffView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("register/", CreateUserView.as_view(), name="register"),
    path("token/", TokenObtainPairView.as_view(), name="get-token"),
    path("token/refresh/", TokenRefreshView.as_view(), name="refresh-token"),
    path("make-staff/", MakeStaffView.as_view(), name="make-staff")
]