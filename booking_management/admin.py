from django.contrib import admin
from .models import Reservations, Slots


class ReservationsAdmin(admin.ModelAdmin):
    list_display = ['id', 'slot']


class SlotsAdmin(admin.ModelAdmin):
    list_display = ['id', 'start_time', 'end_time', 'is_available']


admin.site.register(Reservations, ReservationsAdmin)
admin.site.register(Slots, SlotsAdmin)
