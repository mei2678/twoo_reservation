from rest_framework import viewsets, permissions
from .models import Reservations, Slots
from .serializers import ReservationsSerializer, SlotsSerializer


class ReservationsViewSet(viewsets.ModelViewSet):
    """
    予約の一覧取得・編集を行うエンドポイント
    """
    queryset = Reservations.objects.all().order_by('updated_at')
    serializer_class = ReservationsSerializer
    permission_classes = [permissions.IsAuthenticated]


class SlotsViewSet(viewsets.ModelViewSet):
    """
    予約枠の一覧取得・編集を行うエンドポイント
    """
    queryset = Slots.objects.all().order_by('start_time')
    serializer_class = SlotsSerializer
    permission_classes = [permissions.IsAdminUser]