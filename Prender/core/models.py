from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, DateTimeField, IntegerField
from django.db.models.fields.files import ImageField
from django.contrib.auth.models import AbstractUser

# region comuna
class Region(models.Model):
    nom_region = models.CharField(max_length=40)

class Comuna(models.Model):
    nom_comuna = models.CharField(max_length=40)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

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
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)

class Emprendedor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key = True)
    numero_telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=100)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    


#modelo formulario de contacto
class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    asunto = models.CharField(max_length=50)
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre

#modelo tienda/perfil emprendedor
class Perfil(models.Model):
    user = models.OneToOneField(Emprendedor, on_delete=models.CASCADE, primary_key= True)
    nom_tienda = models.CharField(max_length=50)
    desc_tienda = models.TextField()
    foto_perf = models.ImageField(upload_to="images")

#categorias productos
class Categoria(models.Model):
    nom_categoria = models.CharField(max_length=30)

class Producto(models.Model):
    nom_prod = models.CharField(max_length=50)
    desc_prod = models.TextField()
    valor_prod = models.IntegerField()
    cantidad = models.IntegerField()
    user = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

#herramientas gestion
class Inventario(models.Model):
    nom_ingred = models.CharField(max_length= 30)
    cant_ingre = models.IntegerField()
    valor_ingre = models.IntegerField()
    user = models.ForeignKey(Perfil, on_delete= models.CASCADE)

class Receta(models.Model):
    nom_receta = models.CharField(max_length = 50)
    desc_receta = models.TextField()
    user = models.ForeignKey(Perfil, on_delete= models.CASCADE)

class Balance(models.Model):
    cant_ventas = models.IntegerField() 
    total = models.IntegerField()
    fecha = models.DateField()
    user = models.ForeignKey(Perfil, on_delete= models.CASCADE)

# class Carrito(models.Model):






