from django import forms
from . import models
from django.forms import modelformset_factory


class ProductForm(forms.ModelForm):

    class Meta:
        model = models.Product
        fields = ('__all__')

class StockForm(forms.ModelForm):

    class Meta:
        model = models.StockHistory
        fields = ['quantity',  'entered_at', 'leaved_at', 'product']