from .models import CustomUser
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "username", "email", "password", "user_role"]
        extra_kwargs = {
            "password": {"write_only": True},
            "user_role": {"read_only": True},
        }
    
    def create(self, validated_data):
        if not CustomUser.objects.filter(user_role="admin").exists():
            validated_data["user_role"] = "admin"

        password = validated_data.pop("password", None)
        user = CustomUser(**validated_data)

        if password:
            user.set_password(password)
        user.save()
        return user