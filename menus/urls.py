from django.urls import path
from .views import MenuCreateView, create_done


app_name = "menus"

urlpatterns = [
    path('create/', MenuCreateView.as_view(), name="create"),
    path('create_done/', create_done, name="create_done")
]