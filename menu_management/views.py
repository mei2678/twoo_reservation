from rest_framework import viewsets, permissions
from .models import Menus, Cautions
from .serializers import MenusSerializer, CautionsSerializer


class MenusViewSet(viewsets.ModelViewSet):
    """
    メニューの一覧取得・編集を行うエンドポイント
    """
    queryset = Menus.objects.all().order_by('name')
    serializer_class = MenusSerializer
    permission_classes = [permissions.IsAuthenticated]


class CautionsViewSet(viewsets.ModelViewSet):
    """
    メニューの一覧取得・編集を行うエンドポイント
    """
    queryset = Cautions.objects.all()
    serializer_class = CautionsSerializer
    permission_classes = [permissions.IsAuthenticated]