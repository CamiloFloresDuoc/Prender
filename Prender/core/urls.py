from cgi import test
from django.urls import path
from .views import busqueda, carrito, comprador, emprendedor, gestionEmp, index, ingPdcto, login, producto, regCompras, register 

urlpatterns = [
    path('', index,name="index"),
    path('login/', login, name="login"),
    path('register/', register, name="register"),
    path('producto/', producto, name="producto"),
    path('carrito/', carrito, name="carrito"),
    path('emprendedor/', emprendedor, name="emprendedor"),
    path('comprador/', comprador, name="comprador"),
    path('ingPdcto/', ingPdcto, name="ingPdcto"),
    path('gestionEmp/', gestionEmp, name="gestionEmp"),
    path('regCompras', regCompras, name="regCompras"),
    path('busqueda/', busqueda, name="busqueda"),
]