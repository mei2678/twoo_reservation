from django.urls import path
from .views import MenuListView, MenuCreateView, create_done


app_name = "menus"

urlpatterns = [
    path('', MenuListView.as_view(), name="menu_list"),
    path('create/', MenuCreateView.as_view(), name="menu_create"),
    path('create_done/', create_done, name="menu_create_done")
]