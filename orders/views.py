from django.http import HttpResponse
from django.shortcuts import render

from .models import Pasta, Pizza, PizzaType, Sub, Salad, Platter, Topping

# Create your views here.
def index(request):
    context = {
        "regularPizzas": Pizza.objects.all().filter(type=PizzaType.objects.get(pk="REG")).order_by('numToppings'),
        "sicilianPizzas": Pizza.objects.all().filter(type=PizzaType.objects.get(pk="REG")),
        "pastas": Pasta.objects.all(),
        "subs": Sub.objects.all(),
        "salads": Salad.objects.all(),
        "platters": Platter.objects.all(),
        "toppings": Topping.objects.all()
    }

    return render(request, "orders/index.html", context)

def pizza(request, pizza_id, pizza_size):
    """ Pizza Ordering Page """
    # Get the pizza details
    try:
        pizza = Pizza.objects.get(pk=pizza_id)
    except KeyError:
        # ToDo: Add logic for exceptions
        return HttpResponse("KeyError")
    
    context = {
        "pizza": pizza,
        "pizza_size": pizza_size,
        "toppings": Topping.objects.all()
    }

    return render(request, "orders/pizza.html", context)

def pasta(request, pasta_id):
    return HttpResponse("Pasta Detail: TODO")

def sub(request, sub_id):
    return HttpResponse("Sub Detail: TODO")

def salad(request, salad_id):
    return HttpResponse("Salad Detail: TODO")

def platter(request, platter_id):
    return HttpResponse("Platter Detail: TODO")