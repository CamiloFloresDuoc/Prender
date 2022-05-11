from django import forms
from django.forms import ModelForm
from django.db import transaction
from django.db.models import fields
from django.contrib.auth.forms import UserCreationForm
from .models import User, Comprador, Emprendedor, Contacto



class CompradorRegister(UserCreationForm):
    nombre = forms.CharField(required=True)
    apellido = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    numero_telefono = forms.CharField(required=True)
    direccion = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)   
        user.is_comprador = True    
        user.nombre = self.cleaned_data.get('nombre')
        user.apellido = self.cleaned_data.get('apellido')
        user.email = self.cleaned_data.get('email')
        user.save() 
        comprador = Comprador.objects.create(user=user)
        comprador.numero_telefono = self.cleaned_data.get('numero_telefono')
        comprador.direccion = self.cleaned_data.get('direccion')
        comprador.save()
        return user

class EmprendedorRegister(UserCreationForm):
    nombre = forms.CharField(required=True)
    apellido = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    numero_telefono = forms.CharField(required=True)
    direccion = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)  
        user.is_emprendedor = True     
        user.nombre = self.cleaned_data.get('nombre')
        user.apellido = self.cleaned_data.get('apellido')
        user.email = self.cleaned_data.get('email')
        user.save() 
        emprendedor = Emprendedor.objects.create(user=user)
        emprendedor.numero_telefono = self.cleaned_data.get('numero_telefono')
        emprendedor.direccion = self.cleaned_data.get('direccion')
        emprendedor.save()
        return user



#para contacto
class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre','correo','asunto','mensaje']