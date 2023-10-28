from rest_framework import serializers
from .models import Slots
from booking_management.serializers import ReservationsSerializer


class SlotsSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(source='user.username', read_only=True)
    updated_by = serializers.CharField(source='user.username', read_only=True)
    reservation = ReservationsSerializer(read_only=True)

    class Meta:
        model = Slots
        fields = '__all__'