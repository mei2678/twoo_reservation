from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from social_django.views import auth
from . import views

urlpatterns = [
    path('', include('social_django.urls', namespace='social')),
    path('login', auth, name='line-login', kwargs={'backend': 'line'}),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('complete/line', views.complete_line, name='complete_line')
]