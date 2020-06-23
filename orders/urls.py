from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("pizza", views.pizza, name="pizza"),
    path("checkout", views.checkout, name="checkout")
]
