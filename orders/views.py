import json
from django.http import HttpResponse, JsonResponse
import django.http.request
from django.shortcuts import render, redirect
from django.db.models import Sum

from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from orders.forms import DinnerPlatterForm, PastaForm, PizzaForm, SaladForm, SubForm
from orders.models import (Cart, DinnerPlatter, Pasta, Pizza, Salad, Sub, SubExtra,
                           Topping)

# Create your views here.
def index(request):
    """ Homepage where users can view the menu and add items to a virtual cart """

    dinnerPlatterForm = DinnerPlatterForm(auto_id="platter_%s")
    pastaForm = PastaForm(auto_id="pasta_%s")
    pizzaForm = PizzaForm(auto_id="pizza_%s")
    saladForm = SaladForm(auto_id="salad_%s")
    subForm = SubForm(auto_id="sub_%s")

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
def addToCart(request):
    """ Adds the passed in item to the cart """

    if request.method == 'POST':
        # ToDo: Add post logic
        product = request.POST.get('product')
        product = eval(product)

        # Initialize Variables
        productType = ''
        productId = ''
        productName = ''
        productStyle = ''
        productSize = ''
        productExtras = []
        productToppings = []
        productQuantity = -1

        # Get the product type
        productType = product['type']

        # Use the product type to output
        if productType == 'Sub':
            # Sub attributes: Name, Size, Extras, Quantity
            productId = product['name']
            productName = Sub.objects.values_list('name').get(pk=productId)[0]
            productSize = product['size']
            productExtras = SubExtra.objects.filter(id__in=product['extras'])
            productQuantity = product['quantity']

            subObject = Sub.objects.filter(name=productName).filter(size=productSize).first()
            subExtraObjects = SubExtra.objects.filter(id__in=product['extras'])

            subExtraCost = 0
            for subExtraObject in subExtraObjects:
                subExtraCost += subExtraObject.price

            totalCost = (subObject.price + subExtraCost) * int(productQuantity)

            # Get the user's cart
            username = request.user.username
            userObject = User.objects.get(username=username)
            userCart = Cart.objects.filter(username=userObject).first()

            if userCart is None:
                userCart = Cart.objects.create(username=userObject)

            subObjectCheck = Sub.objects.get(pk=subObject.id)

            print(int(productQuantity))
            for x in range(int(productQuantity)):
                userCart.subs.add(Sub.objects.get(id=subObject.id))
                userCart.subExtras.add(*subExtraObjects)

        else:
            print('ToDo')

    else:
        #Only accept POST requests here, otherwise redirect back to the home page
        return redirect('index')

    return redirect('index')

@login_required(login_url='/login/')
def checkout(request):
    """ Login Page """

    if request.method == 'POST':

        form = PizzaForm(request.POST)

        if form.is_valid():
            messages.success(request, f'Your order was placed!')
            return redirect('index')
    elif request.method == 'GET':
        # Get the user's cart
        cart = Cart.objects.filter(username=User.objects.get(username=request.user.username)).first()

        context = {
            'subs': cart.subs.all()
        }

        return render(request, "orders/checkout.html", context)
    else:


        return render(request, "orders/checkout.html")

@login_required(login_url='/login/')
def cart(request):
    if request.method == 'GET':
        # Get the logged in user
        username = request.user.username

        # Get the user's cart
        userCart = Cart.objects.filter(username=User.objects.get(username=username)).first()

        # Count the number of objects in the cart
        numSubs = userCart.subs.all().count()

        # Sum up the number of objects
        total = numSubs

        # Return the number of objects to be displayed on the page
        data = total

        return HttpResponse(total)
    else:
        return redirect('index')
