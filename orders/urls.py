from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("addToCart", views.addToCart, name="addToCart"),
    path("clearCart", views.clearCart, name="clearCart"),
    path("placeOrder", views.placeOrder, name="placeOrder"),
    path("checkout", views.checkout, name="checkout"),
    path("cart", views.cart, name="cart"),
    path("orderSuccess", views.orderSuccess, name="orderSuccess")
]
