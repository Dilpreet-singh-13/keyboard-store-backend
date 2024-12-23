from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('id', 'username', 'email', 'user_role', 'is_staff', 'is_active')
    list_filter = ('user_role', 'is_staff', 'is_active')
    fieldsets = (
        (None, {"fields": ("username", "email", "password")}),
        (
            "Permissions",
            {"fields": ("is_staff", "is_active", "groups", "user_permissions")},
        ),
        ("User Role", {"fields": ("user_role",)}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "password1",
                    "password2",
                    "user_role",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )
    search_fields = ("username", "email")
    ordering = ("id",)