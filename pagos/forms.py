from django import forms
from .models import Pago



class PagoForm(forms.ModelForm):


    class Meta:

        model=Pago
        fields = '__all__'

        widgets = {
            "fecha": forms.NumberInput(attrs={'type': 'date'})
        }