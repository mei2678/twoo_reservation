from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReservationsViewSet, SlotsViewSet

router = DefaultRouter()
router.register('reservations', ReservationsViewSet)
router.register('slots', SlotsViewSet)

urlpatterns = [
    path('', include(router.urls))
]