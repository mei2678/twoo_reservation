from rest_framework import serializers
from .models import Reservations, Slots
from auth_management.serializers import CustomUserSerializer
from menu_management.serializers import MenusSerializer


class ReservationsSerializer(serializers.ModelSerializer):
    created_by = CustomUserSerializer(read_only=True)
    updated_by = CustomUserSerializer(read_only=True)
    user = CustomUserSerializer(read_only=True)
    menu = MenusSerializer

    class Meta:
        model = Reservations
        fields = '__all__'


class SlotsSerializer(serializers.ModelSerializer):
    created_by = CustomUserSerializer(read_only=True)
    updated_by = CustomUserSerializer(read_only=True)
    reservation = ReservationsSerializer

    class Meta:
        model = Slots
        fields = '__all__'

