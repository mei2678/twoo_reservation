from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu_management/', include('menu_management.urls')),
    path('booking_management/', include('booking_management.urls')),
    path('visit_history/', include('visit_history.urls'))
]
