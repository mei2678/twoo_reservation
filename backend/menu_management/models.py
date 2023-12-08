from django.db import models
from django_currentuser.db.models import CurrentUserField


class Cautions(models.Model):
    class Meta:
        db_table = 'cautions'

    title = models.CharField(verbose_name='タイトル', max_length=100, unique=True)
    content = models.TextField(verbose_name='内容', null=True, blank=True)
    created_by = CurrentUserField(verbose_name='作成者', null=True, blank=True,
                                         on_delete=models.SET_NULL, related_name='cautions_created_by')
    updated_by = CurrentUserField(verbose_name='更新者', null=True, blank=True,
                                         on_delete=models.SET_NULL, related_name='cautions_updated_by')
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    def __str__(self):
        return self.title


class Menus(models.Model):
    class Meta:
        db_table = 'menus'

    name = models.CharField(verbose_name='メニュー名', max_length=200, unique=True)
    description = models.TextField(verbose_name='説明', null=True, blank=True)
    price = models.IntegerField(verbose_name='価格', null=True, blank=True)
    duration = models.IntegerField(verbose_name='所要時間', null=True, blank=True)
    caution = models.ForeignKey(Cautions, verbose_name='注意事項', null=True, blank=True, on_delete=models.SET_NULL, related_name='menus_cautions')
    is_option = models.BooleanField(verbose_name='オプション', null=True, blank=True)
    created_by = CurrentUserField(verbose_name='作成者', null=True, blank=True, editable=False, on_delete=models.SET_NULL, related_name='menus_created_by')
    updated_by = CurrentUserField(verbose_name='更新者', null=True, blank=True, editable=False, on_delete=models.SET_NULL, related_name='menus_updated_by')
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    def __str__(self):
        return self.name
