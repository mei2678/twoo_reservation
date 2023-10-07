from rest_framework import serializers
from .models import Menus, Cautions
from auth_management.serializers import CustomUserSerializer


class CautionsSerializer(serializers.ModelSerializer):
    created_by = CustomUserSerializer(read_only=True)
    updated_by = CustomUserSerializer(read_only=True)

    class Meta:
        model = Cautions
        fields = '__all__'


class MenusSerializer(serializers.ModelSerializer):
    created_by = CustomUserSerializer(read_only=True)
    updated_by = CustomUserSerializer(read_only=True)
    caution = CautionsSerializer(read_only=True)

    class Meta:
        model = Menus
        fields = '__all__'