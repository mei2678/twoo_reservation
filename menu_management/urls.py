from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenusViewSet, CautionsViewSet

router = DefaultRouter()
router.register('menus', MenusViewSet)
router.register('cautions', CautionsViewSet)

urlpatterns = [
    path('', include(router.urls))
]