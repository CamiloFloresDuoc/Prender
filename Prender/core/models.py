from pyexpat import model
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, DateTimeField, IntegerField
from django.db.models.fields.files import ImageField
from django.contrib.auth.models import AbstractUser

# region comuna
class Region(models.Model):
    nom_region = models.CharField(max_length=40)

    def __str__(self):
        return self.nom_region

class Comuna(models.Model):
    nom_comuna = models.CharField(max_length=40)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom_comuna

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
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, default=False)

class Emprendedor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key = True)
    numero_telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=100)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, default=False)
    

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
    nom_tienda = models.CharField(max_length=50)
    desc_tienda = models.TextField()
    foto_perf = models.ImageField(upload_to="images")
    user = models.ForeignKey(Emprendedor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom_tienda

#categorias productos
class Categoria(models.Model):
    nom_categoria = models.CharField(max_length=30)

    def __str__(self):
        return self.nom_categoria

class Producto(models.Model):
    nom_prod = models.CharField(max_length=50)
    desc_prod = models.TextField()
    valor_prod = models.IntegerField()
    cantidad = models.IntegerField()
    user = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom_prod

#herramientas gestion
class Inventario(models.Model):
    nom_ingred = models.CharField(max_length= 30)
    cant_ingre = models.IntegerField()
    valor_ingre = models.IntegerField()
    user = models.ForeignKey(Perfil, on_delete= models.CASCADE)

    def __str__(self):
        return self.nom_ingred

class Receta(models.Model):
    nom_receta = models.CharField(max_length = 50)
    desc_receta = models.TextField()
    user = models.ForeignKey(Perfil, on_delete= models.CASCADE)

    def __str__(self):
        return self.nom_receta

class Balance(models.Model):
    cant_ventas = models.IntegerField() 
    total = models.IntegerField()
    fecha = models.DateField()
    user = models.ForeignKey(Perfil, on_delete= models.CASCADE)

#parte del comprador

class Carrito(models.Model):
    fecha_carro = models.DateField()
    user = models.ForeignKey(Comprador, on_delete= models.CASCADE)
    producto = models.ManyToManyField(Producto, through='Detalle_carro')

class Detalle_carro(models.Model):
    cantidad = models.IntegerField()
    cod_prod = models.ForeignKey(Producto, on_delete= models.CASCADE)
    carro = models.ForeignKey(Carrito, on_delete= models.CASCADE)

class Pedido(models.Model):
    fecha_pedido = models.DateField()
    carro = models.ForeignKey(Carrito, on_delete= models.CASCADE)

class MedioPago(models.Model):
    desc = models.CharField(max_length=50)
    costo = models.IntegerField()

    def __str__(self):
        return self.desc

class Boleta(models.Model):
    fecha_emision = models.DateField()
    valor_neto = models.IntegerField()
    iva = models.IntegerField()
    total = models.IntegerField()
    medio_pago = models.ForeignKey(MedioPago, on_delete= models.CASCADE)

#registro compras
class RegCompra(models.Model):
    fechaCompra = models.DateField()
    neto = models.IntegerField()
    iva = models.IntegerField()
    total = models.IntegerField()
    user = models.ForeignKey(Comprador, on_delete= models.CASCADE)








