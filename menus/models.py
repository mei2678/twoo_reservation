from django.db import models


class Menu(models.Model):
    class Meta:
        db_table = "menus"
        verbose_name = "メニュー"
        verbose_name_plural = "メニュー"

    name = models.CharField(verbose_name='メニュー名', max_length=200, default='',
                            unique=True)
    description = models.TextField(verbose_name='説明', null=True, blank=True)
    price = models.IntegerField(verbose_name='価格', default=0)
    duration = models.IntegerField(verbose_name='所要時間(分)', default=0)
    # 要追記: 注意事項フィールド
    is_option = models.BooleanField(verbose_name='オプション', default=False)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    def __str__(self):
        return self.name