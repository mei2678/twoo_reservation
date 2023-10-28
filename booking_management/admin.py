from django.contrib import admin
from .models import Reservations


class ReservationsAdmin(admin.ModelAdmin):
    list_display = ['id', 'slot']
    

admin.site.register(Reservations, ReservationsAdmin)
