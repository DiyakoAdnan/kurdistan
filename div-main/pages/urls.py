from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path("about/", views.about, name="about"),
    path("sulaymaniyah/", views.sulaymaniyah, name="sulaymaniyah"),
    path("hawler/", views.hawler, name="hawler"),
    path("dohuk/", views.dohuk, name="Duhok"),  # case-sensitive!
    path("contact/", views.contact, name="contact"),
]
