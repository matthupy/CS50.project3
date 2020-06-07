from django.http import HttpResponse
from django.shortcuts import render

from .models import Pizza, PizzaPrice, Sub, Salad, DinnerPlatter, Topping

# Create your views here.
def index(request):
    context = {
        "pizzas": PizzaPrice.objects.all(),
        "subs": Sub.objects.all(),
        "salads": Salad.objects.all(),
        "platters": DinnerPlatter.objects.all(),
        "toppings": Topping.objects.all()
    }

    return render(request, "orders/index.html", context)
