from django.db import models
from menus.models import Menus


class Reservations(models.Model):
    class Meta:
        db_table = "reservations"
        verbose_name = "予約"
        verbose_name_plural = "予約"

    # user = models.ForeignKey(
        # settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    menu = models.ForeignKey(
        Menus, null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(verbose_name="作成日時", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="更新日時", auto_now=True)
