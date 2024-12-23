from rest_framework import serializers
from . import models


# custom switch field to control the name convertion to object
class SwitchField(serializers.RelatedField):
    def to_representation(self, value):
        return value.name

    def to_internal_value(self, data):
        try:
            if type(data) is int:
                return models.Switch.objects.get(id=data)
            elif isinstance(data, str) and data.isdigit():
                return models.Switch.objects.get(id=data)
            else:
                return models.Switch.objects.get(name=data)
        except models.Switch.DoesNotExist:
            raise serializers.ValidationError(
                f"Switch with ID or Name = '{data}' does not exist."
            )


class KeyboardSerializer(serializers.ModelSerializer):
    switch = SwitchField(
        queryset=models.Switch.objects.all(), required=False, allow_null=True
    )

    class Meta:
        model = models.Keyboard
        fields = [
            "id",
            "name",
            "price",
            "description",
            "keyboard_type",
            "weight",
            "connectivity_options",
            "switch",
        ]

    def validate(self, data):
        """
        Ensures that any membrane keyboard isn't linekd with a switch, if one is provided its smiply set to NULL.

        Also ensures a switch is provided for mechanical type keyboard. The switch name or ID can be used.
        """

        if data.get("keyboard_type") not in ["mechanical", "membrane"]:
            raise serializers.ValidationError(
                "Keyboard type must be mechanical or membrane."
            )

        if data.get("keyboard_type") == "membrane" and data.get("switch") is not None:
            data["switch"] = models.Switch.objects.none() # empty object of switch model
        elif data.get("keyboard_type") == "mechanical" and data.get("switch") is None:
            raise serializers.ValidationError(
                "Switch muse be provided for mechanical keyboards."
            )

        return data

    def create(self, validated_data):
        if validated_data.get("switch") is not None:
            switch_instance = validated_data.pop("switch")
            return models.Keyboard.objects.create(
                switch=switch_instance, **validated_data
            )
        else:
            return models.Keyboard.objects.create(**validated_data)

    def partial_update(self, instance, validated_data):
        if "switch" in validated_data and validated_data.get("switch") is not None:
            instance.switch = validated_data.pop("switch")
        return super().update(instance, validated_data)
    
    def update(self, instance, validated_data):
        if "switch" in validated_data and validated_data.get("switch") is not None:
            instance.switch = validated_data.pop("switch")
        return super().update(instance, validated_data)


class SwitchSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Switch
        fields = ["id", "name", "description", "switch_type", "price"]

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
