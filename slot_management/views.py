from rest_framework import viewsets, permissions
from .models import Slots
from .serializers import SlotsSerializer


class SlotsViewSet(viewsets.ModelViewSet):
    """
    予約枠の一覧取得・編集を行うエンドポイント
    """
    queryset = Slots.objects.all().order_by('start_time')
    serializer_class = SlotsSerializer
    permission_classes = [permissions.IsAdminUser]