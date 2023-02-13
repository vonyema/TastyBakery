from django.forms import ModelForm
from .models import Ingredient


class OrderForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = ('serving_size', 'filling','frosting','addons','additional')