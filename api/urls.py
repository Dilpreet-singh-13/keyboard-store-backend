from django.urls import path
from . import views


urlpatterns = [
    path("switch/", views.SwitchListCreateView.as_view(), name="switch-list"),
    path("switch/<int:pk>/", views.SwitchDetailView.as_view() ,name="switch-detail"),
    path("keyboard/", views.KeyboardListCreateView.as_view(), name="keyboard-list"),
    path("keyboard/<int:pk>/", views.KeyboardDetailView.as_view(), name="keyboard-detail"),
]