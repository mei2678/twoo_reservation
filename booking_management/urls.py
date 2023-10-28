from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReservationsViewSet

router = DefaultRouter()
router.register('reservations', ReservationsViewSet)

urlpatterns = [
    path('', include(router.urls))
]