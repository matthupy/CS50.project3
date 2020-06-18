import django.core.validators
from django.db import models
from django.core.exceptions import ValidationError

# Validations
def validate_price(price):
    """ Valid Prices should be positive decimal values with 2 decimal places """
    if (price is None or price <= 0):
        raise ValidationError(
            _('%(price)s must be a positive, 2 decimal value'),
            params={'price': price},
    )

# Create your models here.
class PizzaType(models.Model):
    code = models.CharField(max_length=3, primary_key=True)
    description = models.CharField(max_length=64)

    def __str__(self):
        return self.description

class Pasta(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

class Pizza(models.Model):
    type = models.ForeignKey(PizzaType, on_delete=models.PROTECT)
    name = models.CharField(max_length=64)
    numToppings = models.IntegerField()
    smallPrice = models.DecimalField(max_digits=6, decimal_places=2, validators=[validate_price])
    largePrice = models.DecimalField(max_digits=6, decimal_places=2, validators=[validate_price])

    def __str__(self):
        return(f"{self.type} - {self.name}")

class Platter(models.Model):
    name = models.CharField(max_length=64)
    smallPrice = models.DecimalField(max_digits=6, decimal_places=2)
    largePrice = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return(f"{self.name}")

class Sub(models.Model):
    name = models.CharField(max_length=64)
    smallPrice = models.DecimalField(max_digits=6, decimal_places=2)
    largePrice = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return(f"{self.name}")

class Salad(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name


class Topping(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


