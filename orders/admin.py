from django.contrib import admin

from .models import DinnerPlatter, Pizza, PizzaPrice, PizzaType, Size, Sub, Salad, Topping

# Register your models here.
admin.site.register(DinnerPlatter)
admin.site.register(Pizza)
admin.site.register(PizzaPrice)
admin.site.register(PizzaType)
admin.site.register(Size)
admin.site.register(Sub)
admin.site.register(Salad)
admin.site.register(Topping)