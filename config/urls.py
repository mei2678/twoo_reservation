from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu_management/', include('menu_management.urls')),
    path('booking_management/', include('booking_management.urls')),
    path('slot_management/', include('slot_management.urls')),
    path('visit_history/', include('visit_history.urls')),
    path('account_management/', include('account_management.urls')),
    path('auth_management/', include('auth_management.urls'))
]
