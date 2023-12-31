from rest_framework import serializers
from .models import Reservations, Slots
from menu_management.serializers import MenusSerializer


class ReservationsSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(source='user.username', read_only=True)
    updated_by = serializers.CharField(source='user.username', read_only=True)
    user = serializers.CharField(source='user.username', read_only=True)
    menu = MenusSerializer
    menu_name = serializers.CharField(source='menu.name', read_only=True)
    slot_time = serializers.SerializerMethodField()

    class Meta:
        model = Reservations
        fields = '__all__'
        
    def get_slot_time(self, obj):
        return obj.slot.start_time if obj.slot else None