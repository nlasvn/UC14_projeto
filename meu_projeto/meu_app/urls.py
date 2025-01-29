from django.urls import path
from . import views

urlpatterns = [
    path("", views.minha_view, name="minha_view"),
    path("oi", views.oi, name="oi"),
]
