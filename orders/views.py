from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth.decorators import login_required

from orders.forms import DinnerPlatterForm, PastaForm, PizzaForm, SaladForm, SubForm
from orders.models import (DinnerPlatter, Pasta, Pizza, Salad, Sub, SubExtra,
                           Topping)

# Create your views here.
def index(request):
    """ Homepage where users can view the menu and add items to a virtual cart """

    dinnerPlatterForm = DinnerPlatterForm()
    pastaForm = PastaForm()
    pizzaForm = PizzaForm()
    saladForm = SaladForm()
    subForm = SubForm()

    context = {
        "pizzas": Pizza.objects.all(),
        "toppings": Topping.objects.all(),
        "subs": Sub.objects.all(),
        "subExtras": SubExtra.objects.all(),

        "pastas": Pasta.objects.all(),
        "platters": DinnerPlatter.objects.all(),
        "salads": Salad.objects.all(),
        "dinnerPlatterForm": dinnerPlatterForm,
        "pastaForm": pastaForm,
        "pizzaForm": pizzaForm,
        "saladForm": saladForm,
        "subForm": subForm
    }

    return render(request, "orders/index.html", context)

def cart(request):
    """ Here the user should see the items added with his price, quantity
    and detail, and then proceed to checkout.
    https://stackoverflow.com/questions/2827764/ecommerceshopping-cartwhere-should-i-store-shopping-cart-data-in-session-or#40130593"""

    if request.method == 'POST':
        pass
    else:
        return render(request, "orders/cart.html")

@login_required(login_url='/login/')
def checkout(request):
    """ Login Page """

    if request.method == 'POST':

        form = PizzaForm(request.POST)

        if form.is_valid():
            #form.save()
            messages.success(request, f'Your order was placed!')
            return redirect('index')
    else:
        return render(request, "orders/checkout.html")

def pizza(request):
    """ Pizza Ordering Page """

    form = PizzaForm()

    context = {
        "toppings": Topping.objects.all(),
        "form": form
    }

    return render(request, "orders/pizza.html", context)

def pasta(request, pasta_id):
    return HttpResponse("Pasta Detail: TODO")

def sub(request, sub_id, sub_size):
    return HttpResponse("Sub Detail: TODO")

def salad(request, salad_id):
    return HttpResponse("Salad Detail: TODO")

def platter(request, platter_id, platter_size):
    return HttpResponse("Platter Detail: TODO")