from django import forms

class CheckoutForm(forms.Form):
    nombre = forms.CharField(max_length=225)
    apellido = forms.CharField(max_length=225)
    email = forms.EmailField(max_length=225)
    numero_telefono = forms.CharField(max_length=225)
    direccion = forms.CharField(max_length=225)
    comuna = forms.CharField(max_length=225)
    stripe_token = forms.CharField(max_length=225)
