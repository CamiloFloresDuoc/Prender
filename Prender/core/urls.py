from ast import Index
from cgi import test
from django.urls import path
from .views import (adminPdcto, busqueda, carrito, comprador, comprador_register, crearPerfil, 
emprendedor_register, editarPdcto, eliminarPdcto, emprendedor, empPublico, gestionEmp, 
Index, ingPdcto, login_request, logout_view, producto, regCompras, register,
editarPerfilEmp
)

urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('login/', login_request, name="login"),
    path('logout/', logout_view, name='logout'),
    path('register/', register, name="register"),
    path('comprador_register/', comprador_register.as_view(), name="comprador_register"),
    path('emprendedor_register/', emprendedor_register.as_view(), name="emprendedor_register"),
    path('producto/', producto, name="producto"),
    path('carrito/', carrito, name="carrito"),
    path('emprendedor/', emprendedor, name="emprendedor"),
    path('comprador/', comprador, name="comprador"),
    path('ingPdcto/', ingPdcto, name="ingPdcto"),
    path('gestionEmp/', gestionEmp, name="gestionEmp"),
    path('regCompras', regCompras, name="regCompras"),
    path('busqueda/', busqueda, name="busqueda"),
    path('empPublico/', empPublico, name="empPublico"),
    path('adminPdcto/', adminPdcto, name="adminPdcto"),
    path('editarPdcto/', editarPdcto, name="editarPdcto"),
    path('eliminarPdcto/', eliminarPdcto, name="eliminarPdcto"),
    path('editarPerfilEmp/', editarPerfilEmp, name="editarPerfilEmp"),
    path('crearPerfil/', crearPerfil, name="crearPerfil"),
]