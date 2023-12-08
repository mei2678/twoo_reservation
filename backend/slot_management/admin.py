from django.contrib import admin
from .models import Slots


class SlotsAdmin(admin.ModelAdmin):
    list_display = ['id', 'start_time', 'end_time', 'is_available']


admin.site.register(Slots, SlotsAdmin)
