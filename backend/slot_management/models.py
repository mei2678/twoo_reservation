from django.db import models
from django_currentuser.db.models import CurrentUserField


class Slots(models.Model):

    class Meta:
        db_table = 'slots'

    is_available = models.BooleanField(verbose_name='予約可能', default=True)
    start_time = models.DateTimeField(verbose_name='開始日時', unique=True)
    end_time = models.DateTimeField(verbose_name='終了日時', blank=True)
    created_by = CurrentUserField(
        verbose_name='作成者', null=True, blank=True, editable=False,
        on_delete=models.SET_NULL, related_name='slots_created_by')
    updated_by = CurrentUserField(
        verbose_name='更新者', null=True, blank=True, on_delete=models.SET_NULL,
        related_name='slots_updated_by')
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    def __str__(self):
        return f'開始: {str(self.start_time.strftime("%Y/%m/%d %H:%M:%S"))} - 終了: {str(self.end_time.strftime("%Y/%m/%d %H:%M:%S"))}'