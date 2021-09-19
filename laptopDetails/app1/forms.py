
from .models import Laptop
from django import forms

class laptopModelForm(forms.ModelForm):
    class Meta:
        model = Laptop
        fields ='__all__'
        labels = {
            'company_name': 'Company Name',
            'model_name': 'Model Name',
            'rom': 'Rom',


        }