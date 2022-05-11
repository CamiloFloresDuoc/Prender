from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, DateTimeField, IntegerField
from django.db.models.fields.files import ImageField
from django.contrib.auth.models import AbstractUser

# Modelo tipos usuario para login

class User(AbstractUser):
    is_admin = models.BooleanField('es admin', default=False)
    is_comprador = models.BooleanField('es comprador', default=False)
    is_emprendedor = models.BooleanField('es emprendedor', default=False)
    nombre = models.CharField(max_length=50, default=True)
    apellido = models.CharField(max_length=50, default=True)
    email = models.EmailField()

class Administrador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key = True)

class Comprador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key = True)
    numero_telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=100)

class Emprendedor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key = True)
    numero_telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=100)


#modelo formulario de contacto
class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    asunto = models.CharField(max_length=50)
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre