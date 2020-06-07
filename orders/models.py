from django.db import models

# Create your models here.
class PizzaType(models.Model):
    code = models.CharField(max_length=3, primary_key=True)
    description = models.CharField(max_length=64)

    def __str__(self):
        return self.description

class Size(models.Model):
    code = models.CharField(max_length=3, primary_key=True)
    description = models.CharField(max_length=64)

    def __str__(self):
        return self.description

class Topping(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class PizzaPrice(models.Model):
    toppings = models.IntegerField(default=0)
    size = models.ForeignKey(Size, on_delete=models.PROTECT)
    type = models.ForeignKey(PizzaType, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return(f"{self.size.description} {self.type.description} - {self.toppings} Toppings")

class Pizza(models.Model):
    type = models.ForeignKey(PizzaType, on_delete=models.PROTECT)
    size = models.ForeignKey(Size, on_delete=models.PROTECT)
    toppings = models.ManyToManyField(Topping, blank=True)

class Sub(models.Model):
    name = models.CharField(max_length=64)
    size = models.ForeignKey(Size, on_delete=models.PROTECT)
    toppings = models.ManyToManyField(Topping, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return(f"{self.size.description} {self.name}")

class Salad(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

class DinnerPlatter(models.Model):
    name = models.CharField(max_length=64)
    size = models.ForeignKey(Size, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return(f"{self.size.description} {self.name}")

