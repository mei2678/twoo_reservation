from django import forms
from .models import Menus


class MenuForm(forms.ModelForm):
    """
    新規メニュー登録画面
    """
    class Meta:
        model = Menus
        fields = ["name", "description", "price", "duration",
                 "caution", "is_option"]