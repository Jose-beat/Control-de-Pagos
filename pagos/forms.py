from django import forms


class PayForm(forms.Form):
    name = forms.CharField(label="Nombre del Pago", required=True)
    content = forms.CharField(label="Contenido", required=True, widget=forms.Textarea)
    amount = forms.DecimalField(label="Monto a Pagar", required=True)
    grant = forms.BooleanField(label="Beca", required=True)
    created = forms.DateTimeField(label="Fecha de registro de pago", required=True)
    classification = forms.CharField(label="Clasificacion", required=True)
  