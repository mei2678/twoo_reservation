from rest_framework import viewsets, permissions
from django.db.models import Q
from django.db import transaction
from menu_management.models import Menus
from .models import Reservations, Slots
from .serializers import ReservationsSerializer
from datetime import timedelta
import pytz


class ReservationsViewSet(viewsets.ModelViewSet):
    """
    予約の一覧取得・編集を行うエンドポイント
    """
    queryset = Reservations.objects.all().order_by('updated_at')
    serializer_class = ReservationsSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    @transaction.atomic
    def handle_reservation(self, request):
        reservation_data = request.data
        menu_id = reservation_data['menu']
        selected_menu = Menus.objects.get(id=menu_id)
        selected_slot_id = reservation_data['slot']
        selected_slot = Slots.objects.get(id=selected_slot_id)
        
        start_time_utc = selected_slot.start_time
        end_time_utc = start_time_utc + timedelta(minutes=selected_menu.duration)

        matching_slots = Slots.objects.filter(
            Q(id=selected_slot_id) |
            Q(start_time__gte=start_time_utc, start_time__lt=end_time_utc) |
            Q(end_time__gt=start_time_utc, end_time__lte=end_time_utc)
        ).filter(
            is_available=True
        )
        
        for slot in matching_slots:
            slot.is_available = 0
            print(f"Updating slot with ID {slot.id}, is_available: {slot.is_available}")
            try:
                slot.save()
            except Exception as e:
                print(f"An error occurred: {e}")
        
    def create(self, request, *args, **kwargs):
        self.handle_reservation(request)
        return super().create(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        data = Slots.objects.get(id=1)
        data.is_available = 1
        self.handle_reservation(request)
        return super().update(request, *args, **kwargs)