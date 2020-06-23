from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("addToCart", views.addToCart, name="addToCart"),
    path("checkout", views.checkout, name="checkout"),
    path("cart", views.cart, name="cart")
]
