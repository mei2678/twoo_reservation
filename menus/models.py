from django.db import models


class Cautions(models.Model):
    class Meta:
        db_table = "cautions"
        verbose_name = "注意事項"
        verbose_name_plural = "注意事項"

    title = models.CharField(verbose_name="タイトル", max_length=100, unique=True)
    content = models.TextField(verbose_name="内容", null=True, blank=True)
    created_at = models.DateTimeField(verbose_name="作成日時", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="更新日時", auto_now=True)

    def __str__(self):
        return self.title


class Menus(models.Model):
    class Meta:
        db_table = "menus"
        verbose_name = "メニュー"
        verbose_name_plural = "メニュー"

    name = models.CharField(verbose_name="メニュー", max_length=200, unique=True)
    description = models.TextField(verbose_name="説明", null=True, blank=True)
    price = models.IntegerField(verbose_name="価格")
    duration = models.IntegerField(verbose_name="所要時間(分)")
    caution = models.ForeignKey(Cautions, null=True, blank=True,
                                on_delete=models.SET_NULL)
    is_option = models.BooleanField(verbose_name="オプション", default=False)
    created_at = models.DateTimeField(verbose_name="作成日時", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="更新日時", auto_now=True)

    def __str__(self):
        return self.name
