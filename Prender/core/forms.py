from django import forms
from django.forms import ModelForm
from django.db import transaction
from django.db.models import fields
from django.contrib.auth.forms import UserCreationForm
from .models import Inventario, Perfil, Producto, Receta, User, Comprador, Emprendedor, Contacto, Comuna



class CompradorRegister(UserCreationForm):
    nombre = forms.CharField(required=True)
    apellido = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    numero_telefono = forms.CharField(required=True)
    direccion = forms.CharField(required=True)
    comuna = forms.ModelChoiceField(queryset = Comuna.objects.all())

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
        comprador.comuna = self.cleaned_data.get('comuna')
        comprador.save()
        return user

class EmprendedorRegister(UserCreationForm):
    nombre = forms.CharField(required=True)
    apellido = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    numero_telefono = forms.CharField(required=True)
    direccion = forms.CharField(required=True)
    comuna = forms.ModelChoiceField(queryset = Comuna.objects.all())

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
        emprendedor.comuna = self.cleaned_data.get('comuna')
        emprendedor.save()
        return user

#creacion perfil post registro
class Crear_perfil_form(forms.ModelForm):
    class Meta:
        model = Perfil
        exclude = ('user',)
        fields = ['nom_tienda', 'desc_tienda', 'foto_perf']

#para contacto
class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre','correo','asunto','mensaje']

#edicion perfil
class Perfil_mod_form(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['nom_tienda', 'desc_tienda','foto_perf']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nom_prod', 'desc_prod', 'valor_prod', 'cantidad', 'categoria', 'imagen']
#carrito

class AgregarCarritoForm(forms.Form):
    quantity = forms.IntegerField()

class InventarioForm(forms.ModelForm):
    class Meta:
        model = Inventario
        fields = ['nom_ingred', 'cant_ingre','valor_ingre']

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ['nom_receta','desc_receta']

