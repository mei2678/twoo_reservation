from django.db import models
from django_currentuser.db.models import CurrentUserField
from menu_management.models import Menus
# from datetime import timedelta


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
    
    # def save(self, *args, **kwargs):
    #     # start_timeが設定されていてend_timeが入力されていない場合
    #     if self.start_time and not self.end_time:
    #         self.end_time = self.start_time + timedelta(minutes=15)
            
    #         super(Slots, self).save(*args, **kwargs)


class Reservations(models.Model):
    RESERVATION_STATUS = [
        ('not_confirmed', '確認前'),
        ('confirmed', '確認済'),
        ('completed', '来店済'),
        ('canceled', 'キャンセル済'),
        ('others', 'その他')
    ]

    class Meta:
        db_table = 'reservations'

    user = CurrentUserField(verbose_name='予約者', null=True, blank=True,
                                         on_delete=models.SET_NULL, related_name='reservated_by')
    slot = models.ForeignKey(Slots, verbose_name='予約枠', null=True, blank=True, on_delete=models.SET_NULL)
    menu = models.ForeignKey(Menus, verbose_name='メニュー', null=True, blank=True, on_delete=models.SET_NULL, related_name='reservations_meuns')
    is_confirmed = models.BooleanField(verbose_name='対応済', null=True, blank=True)
    status = models.CharField(verbose_name='ステータス', max_length=50, choices=RESERVATION_STATUS, default='not_confirmed')
    created_by = CurrentUserField(verbose_name='作成者', null=True, blank=True, editable=False, on_delete=models.SET_NULL, related_name='reservations_created_by')
    updated_by = CurrentUserField(verbose_name='更新者', null=True, blank=True,
                                         on_delete=models.SET_NULL, related_name='reservations_updated_by')
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    def __str__(self):
        return str(self.id)