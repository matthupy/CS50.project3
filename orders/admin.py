from django.contrib import admin

from .models import Pasta, Platter, Pizza, PizzaType, Sub, Salad, Topping

# Register your models here.
admin.site.register(Pasta)
admin.site.register(Platter)
admin.site.register(Pizza)
admin.site.register(PizzaType)
admin.site.register(Sub)
admin.site.register(Salad)
admin.site.register(Topping)