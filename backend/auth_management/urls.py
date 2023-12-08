from django.urls import path
from .views import CustomUserView

urlpatterns = [
    path('current-user/', CustomUserView.as_view(), name='current-user')
]