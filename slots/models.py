from django.db import models


class Slots(models.Model):
    class Meta:
        db_table = "slots"
        verbose_name = "予約枠"
        verbose_name_plural = "予約枠"

    start = models.DateTimeField(verbose_name="開始日時", null=True, blank=True)
    end = models.DateTimeField(verbose_name="終了日時", null=True, blank=True)
    created_at = models.DateTimeField(verbose_name="作成日時", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="更新日時", auto_now=True)
