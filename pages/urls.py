from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('sulaymaniyah/', views.sulaymaniyah, name='sulaymaniyah'),
    path('hawler/', views.hawler, name='hawler'),
    path('dohuk/', views.dohuk, name='Duhok'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.contact, name='about'),
    path('index/', views.contact, name='index'),
]
