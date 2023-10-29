from booking_management.models import Reservations
from rest_framework import serializers


class VisitHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservations
        fields = '__all__'