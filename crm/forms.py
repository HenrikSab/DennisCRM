from django.forms import ModelForm
from .models import Order


class OrderForm(ModelForm):
    class Meta:
        model   = Order # den vi skal arve fra
        fields  = '__all__' # hvis du ikke vil have alle så lave en liste['emne',]

        
