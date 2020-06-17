from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("pizza/<int:pizza_id>/<str:pizza_size>", views.pizza, name="pizza"),
    path("pasta/<int:pasta_id>", views.pasta, name="pasta"),
    path("sub/<int:sub_id>", views.sub, name="sub"),
    path("salad/<int:salad_id>", views.salad, name="salad"),
    path("platter/<int:platter_id>", views.platter, name="platter")
]
