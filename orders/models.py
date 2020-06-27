import django.core.validators
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django import forms

# Validations
def validate_price(price):
    """ Valid Prices should be positive decimal values with 2 decimal places """
    if (price is None or price <= 0):
        raise ValidationError(
            ('%(price)s must be a positive, 2 decimal value'),
            params={'price': price},
    )

# Create your models here.
SIZES = (
    ("S", "Small"),
    ("L", "Large")
)

STYLES = (
    ('R', 'Regular'),
    ('S', 'Sicilian')
)


class Pasta(models.Model):
    name = models.CharField(max_length=40)
    price = models.DecimalField(help_text="Price in USD",max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.name} - $ {self.price}"

class Salad(models.Model):
    name = models.CharField(max_length=40)
    price = models.DecimalField(help_text="Price in USD",max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.name} - $ {self.price}"

class DinnerPlatter(models.Model):
    name = models.CharField(max_length=40)
    size = models.CharField(max_length=10, choices= SIZES)
    price = models.DecimalField(help_text="Price in USD", max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.get_size_display()} - $ {self.price}"

class SubExtra(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(help_text="Price in USD", max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.name}"

class Sub(models.Model):
    name = models.CharField(max_length=40)
    size = models.CharField(max_length=10, choices=SIZES)
    price = models.DecimalField(help_text="Price in USD", max_digits=6, decimal_places=2)
    extras = models.ManyToManyField(SubExtra, blank=True)

    def __str__(self):
        return f"{self.name} - {self.get_size_display()} - $ {self.price}"

class Topping(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name}"

class Pizza(models.Model):
    style = models.CharField(max_length=10, choices=STYLES)
    size = models.CharField(max_length=10, choices=SIZES)
    price = models.DecimalField(help_text="Price in USD", max_digits=6, decimal_places=2)
    toppings = models.ManyToManyField(Topping)

    def __str__(self):
        return f"{self.get_style_display()} - {self.get_size_display()} - {self.price} - Toppings: {self.toppings.in_bulk()}"

class Cart(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    pastas = models.ManyToManyField(Pasta, blank=True)
    pizzas = models.ManyToManyField(Pizza, blank=True)
    subs = models.ManyToManyField(Sub, blank=True)
    subExtras = models.ManyToManyField(SubExtra, blank=True)
    salads = models.ManyToManyField(Salad, blank=True)
    toppings = models.ManyToManyField(Topping, blank=True)
    dinnerPlatters = models.ManyToManyField(DinnerPlatter, blank=True)
    total = models.DecimalField(help_text="Price in USD", max_digits=6, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.username.username}"

class PizzaOrder(Pizza):
    CHOICES = (
        ('CH', 'Cheese'),
        ('1', '1 Topping'),
        ('2', '2 Toppings'),
        ('3', '3 Toppings'),
        ('SP', 'Special')
    )

    style = Pizza.style
    size = Pizza.size
    extras = models.CharField(max_length=15 ,choices=CHOICES, default='CH')
    toppings = Pizza.toppings

    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.get_style_display()} - {self.get_size_display()}"

class SubOrder(Sub):
    name = forms.ModelChoiceField(queryset=Sub.objects.all(), empty_label="(Select a Sub)")
    size = Sub.size
    extras = Sub.extras

    quantity = models.IntegerField(default=1)

    def __str__(self):
        if self.extras.count() == 0:
            return f"{self.get_size_display()} {self.name} - No Extras"
        else:
            return f"{self.get_size_display()} {self.name} - Extras: {self.extras.in_bulk()}"

class DinnerPlatterOrder(DinnerPlatter):
    name = forms.ModelChoiceField(queryset=DinnerPlatter.objects.all(), empty_label="(Select a Dinner Platter)")
    size = DinnerPlatter.size

    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.get_size_display()} {self.name}"

class PastaOrder(Pasta):
    name = Pasta.name

    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.name}"

class SaladOrder(Salad):
    id = Salad.id
    name = Salad.name

    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.name}"