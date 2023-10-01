from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('menu_management/', include('menu_management.urls')),
    path('admin/', admin.site.urls)
]
