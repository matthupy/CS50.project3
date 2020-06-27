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

        # Get the user object
        username = request.user.username
        userObject = User.objects.get(username=username)

        # Use the product type to output
        if productType == 'Sub':
            # Sub attributes: Name, Size, Extras, Quantity
            productId = product['name']
            productName = Sub.objects.values_list('name').get(pk=productId)[0]
            productSize = product['size']
            productPrice = Sub.objects.values('price').filter(name=productName).filter(size=productSize).first()
            productPrice = productPrice['price']
            productExtras = SubExtra.objects.filter(id__in=product['extras'])
            productQuantity = product['quantity']

            subObject = Sub.objects.filter(name=productName).filter(size=productSize).first()
            subExtraObjects = SubExtra.objects.filter(id__in=product['extras'])

            # Add the price of the extras
            extras_cost = SubExtra.objects.filter(id__in=product['extras']).aggregate(Sum('price'))
            print(extras_cost)
            print(productPrice)
            productPrice += extras_cost['price__sum']

            subObject = Sub.objects.create(name=productName, size=productSize, price=productPrice)

            print(subExtraObjects)

            subObject.extras.set(subExtraObjects)

            print(subObject.extras.all())

            subExtraCost = 0
            for subExtraObject in subExtraObjects:
                subExtraCost += subExtraObject.price

            totalCost = (subObject.price + subExtraCost) * int(productQuantity)

            # Get the user's cart
            userCart = Cart.objects.filter(username=userObject).first()

            if userCart is None:
                userCart = Cart.objects.create(username=userObject)

            for x in range(int(productQuantity)):
                userCart.subs.add(subObject)
                #userCart.subExtras.add(*subExtraObjects)

        elif productType == 'Pizza':
            productStyle = product['style']
            pizzaType = product['type']
            productExtras = product['extras']
            productSize = product['size']
            productToppings = product['toppings']
            productQuantity = product['quantity']

            pizzaType = ""
            if (len(productToppings) == 0):
                pizzaType = "CH"
            elif (len(productToppings) == 1):
                pizzaType = "1"
            elif (len(productToppings) == 2):
                pizzaType = "2"
            elif (len(productToppings) == 3):
                pizzaType = "3"
            else:
                pizzaType = "SP"

            # Set prices
            pizzaPrice = 0
            if (pizzaType == "CH"):
                if productStyle == "R" and productSize == "S":
                    pizzaPrice = 12.70
                elif productStyle == "R" and productSize == "L":
                    pizzaPrice = 17.95
                elif productStyle == "S" and productSize == "S":
                    pizzaPrice = 24.45
                elif productStyle == "S" and productSize == "L":
                    pizzaPrice = 38.70
                else:
                    raise Exception("Pizza price not found!")
            elif (pizzaType == "1"):
                if productStyle == "R" and productSize == "S":
                    pizzaPrice = 13.70
                elif productStyle == "R" and productSize == "L":
                    pizzaPrice = 19.95
                elif productStyle == "S" and productSize == "S":
                    pizzaPrice = 26.45
                elif productStyle == "S" and productSize == "L":
                    pizzaPrice = 40.70
                else:
                    raise Exception("Pizza price not found!")
            elif (pizzaType == "2"):
                if productStyle == "R" and productSize == "S":
                    pizzaPrice = 15.20
                elif productStyle == "R" and productSize == "L":
                    pizzaPrice = 21.95
                elif productStyle == "S" and productSize == "S":
                    pizzaPrice = 28.45
                elif productStyle == "S" and productSize == "L":
                    pizzaPrice = 42.70
                else:
                    raise Exception("Pizza price not found!")
            elif (pizzaType == "3"):
                if productStyle == "R" and productSize == "S":
                    pizzaPrice = 16.20
                elif productStyle == "R" and productSize == "L":
                    pizzaPrice = 23.95
                elif productStyle == "S" and productSize == "S":
                    pizzaPrice = 29.45
                elif productStyle == "S" and productSize == "L":
                    pizzaPrice = 44.70
                else:
                    raise Exception("Pizza price not found!")
            elif (pizzaType == "SP"):
                if productStyle == "R" and productSize == "S":
                    pizzaPrice = 17.75
                elif productStyle == "R" and productSize == "L":
                    pizzaPrice = 25.95
                elif productStyle == "S" and productSize == "S":
                    pizzaPrice = 30.45
                elif productStyle == "S" and productSize == "L":
                    pizzaPrice = 45.70
                else:
                    raise Exception("Pizza price not found!")

            # Add the price of the toppings
            pizzaPrice += Toppings.objects.filter(id__in=prodcutToppings).aggregate(sum)

            pizza = Pizza.objects.create(style=productStyle, size=productSize, price=pizzaPrice)
            pizza.toppings.set(productToppings)

            # Get the user's cart
            userCart = Cart.objects.filter(username=User.objects.get(username=request.user.username)).first()

            if userCart is None:
                userCart = Cart.objects.create(username=userObject)

            for x in range(int(productQuantity)):
                userCart.pizzas.add(pizza)


        elif productType == 'Dinner Platter':
            productId = product['name']
            productName = DinnerPlatter.objects.values_list('name').get(pk=productId)[0]
            productSize = product['size']
            dinnerPlatterObject = DinnerPlatter.objects.filter(name=productName).filter(size=productSize).first()
            productQuantity = product['quantity']

            # Get the user's cart
            userCart = Cart.objects.filter(username=User.objects.get(username=request.user.username)).first()

            if userCart is None:
                userCart = Cart.objects.create(username=userObject)

            for x in range(int(productQuantity)):
                userCart.dinnerPlatters.add(DinnerPlatter.objects.get(id=dinnerPlatterObject.id))

        elif productType == 'Salad':
            saladObject = Salad.objects.get(pk=product['name'])
            productQuantity = product['quantity']

            # Get the user's cart
            userCart = Cart.objects.filter(username=User.objects.get(username=request.user.username)).first()

            if userCart is None:
                userCart = Cart.objects.create(username=userObject)

            for x in range(int(productQuantity)):
                userCart.salads.add(Salad.objects.get(id=saladObject.id))

        elif productType == 'Pasta':
            pastaObject = Pasta.objects.get(pk=product['name'])
            productQuantity = product['quantity']

            # Get the user's cart
            userObject = User.objects.get(username=request.user.username)
            userCart = Cart.objects.filter(username=userObject).first()

            if userCart is None:
                userCart = Cart.objects.create(username=userObject)

            pastaObject = Pasta.objects.get(id=pastaObject.id)
            userCart.pastas.add(pastaObject)

        else:
            print('ToDo')

    else:
        #Only accept POST requests here, otherwise redirect back to the home page
        return redirect('index')

    messages.success(request, 'Item added to cart!')
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

        if cart is not None:
            context = {
                'dinnerPlatters': cart.dinnerPlatters.all(),
                'salads': cart.salads.all(),
                'subs': cart.subs.all(),
                'pastas': cart.pastas.all(),
                'pizzas': cart.pizzas.all()
            }

            return render(request, "orders/checkout.html", context)
        else:
            return redirect('index')
    else:
        return render(request, "orders/checkout.html")

@login_required(login_url='/login/')
def placeOrder(request):
    if request.method == 'POST':
        try:
            # Remove all items from the cart
            userObject = User.objects.get(username=request.user.username)
            userCart = Cart.objects.filter(username=userObject).first()

            if userCart is not None:
                userCart.delete()

            # At the end, redirect to the Order Confirmation page
            return redirect('index')
        except:
            messages.error(request, 'Oops! Something went wrong, please try again.')
            return redirect('index')
    else:
        return redirect('index')

@login_required(login_url='/login/')
def clearCart(request):
    if request.method == 'POST':
        try:
            # Remove all items from the cart
            userObject = User.objects.get(username=request.user.username)
            userCart = Cart.objects.filter(username=userObject).first()

            if userCart is not None:
                userCart.delete()

            # At the end, redirect to the Order Confirmation page
            #messages.success(request, 'Success, cart cleared!')
            return redirect('index')
        except:
            messages.error(request, 'Oops! Something went wrong, please try again.')
            return redirect('index')
    else:
        redirect('index')

@login_required(login_url='/login/')
def cart(request):
    if request.method == 'GET':
        # Get the logged in user
        username = request.user.username

        # Get the user's cart
        userCart = Cart.objects.filter(username=User.objects.get(username=username)).first()

        if userCart is not None:
            # Count the number of objects in the cart
            numDinnerPlatters = userCart.dinnerPlatters.all().count()
            numSalads = userCart.salads.all().count()
            numSubs = userCart.subs.all().count()
            numPastas = userCart.pastas.all().count()
            numPizzas = userCart.pizzas.all().count()

            # Sum up the number of objects
            total = numDinnerPlatters + numSalads + numSubs + numPastas + numPizzas
        else:
            total = 0 # Default the cart indicator

        return HttpResponse(total)
    else:
        return redirect('index')

@login_required(login_url='/login/')
def orderSuccess(request):
    return render(request, "orders/order_success.html")