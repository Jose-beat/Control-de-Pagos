from django import forms
from django.forms import widgets
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Requerido. 254 carácteres como máximo y debe ser válido.")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El email ya está registrado, prueba con otro.")
        return email


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'link', 'telefono', 'nombre', 'apellidos', 'clave','domicilio']
        labels = {
            'avatar': 'Imagen de Perfil',
            'bio': 'Puesto',
            'link': 'Red Social',
            'clave': 'ID',

        }
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class':'form-control-file', 'id':'id_imagen_perfil'}),
            'bio': widgets.Input(attrs={}),
            'link': widgets.URLInput(attrs={'class':'form-control', 'placeholder':'Enlace'}),
            'telefono': widgets.Input(attrs={'class':'form-control', 'rows':1, 'placeholder':'telefono'}),
            'nombre': widgets.Input(attrs={'class':'form-control ', 'rows':1, 'placeholder':'nombre'}),
            'apellidos': widgets.Input(attrs={'class':'form-control ', 'rows':1, 'placeholder':'apellidos'}),
            'clave': widgets.PasswordInput(attrs={'class':'form-control', 'rows':1, 'placeholder':'ID'}),
            'domicilio': widgets.Input(attrs={'class':'form-control', 'rows':1, 'placeholder':'Domicilio'}),

        }


class EmailForm(forms.ModelForm):
    email = forms.EmailField(required=True, help_text="Requerido. 254 carácteres como máximo y debe ser válido.")

    class Meta:
        model = User
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if 'email' in self.changed_data:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("El email ya está registrado, prueba con otro.")
        return email