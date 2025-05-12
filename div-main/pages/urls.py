from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path('', views.index, name='index'),  # This is the fix
    path('about/', views.about, name='about'),
    path('sulaymaniyah/', views.sulaymaniyah, name='sulaymaniyah'),
    path('hawler/', views.hawler, name='hawler'),
    path('contact/', views.contact, name='contact'),
]
