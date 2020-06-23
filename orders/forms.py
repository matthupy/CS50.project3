from django import forms
from django.forms import ModelForm
from orders.models import DinnerPlatterOrder, PastaOrder, PizzaOrder, SaladOrder, SubOrder, Pasta, Salad, Sub, DinnerPlatter

class PizzaForm(ModelForm):
    class Meta:
        model = PizzaOrder
        fields = ['style', 'size', 'extras', 'toppings', 'quantity']

class SubForm(ModelForm):
    class Meta:
        model = SubOrder
        fields = ['name', 'size', 'extras', 'quantity']
        widgets = {
            'name': forms.Select(choices=Sub.objects.filter(size='S').values_list('id','name')) # Filter to size = 'Small' to get the distinct sub values
        }

class PastaForm(ModelForm):
    name = forms.ChoiceField(choices=Pasta.objects.values_list('id','name').all())

    class Meta:
        model = PastaOrder
        fields = ['name', 'quantity']

class SaladForm(ModelForm):
    class Meta:
        model = SaladOrder
        fields = ['name', 'quantity']
        widgets = {
            'name': forms.Select(choices=Salad.objects.values_list('id','name').all())
        }

class DinnerPlatterForm(ModelForm):
    class Meta:
        model = DinnerPlatterOrder
        fields = ['name', 'size', 'quantity']
        widgets = {
            'name': forms.Select(choices=DinnerPlatter.objects.filter(size='S').values_list('id','name')) # Filter to size = 'Small' to get the distinct sub values
        }