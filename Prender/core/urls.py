from ast import Index
from cgi import test
from django.urls import path
from .views import (aTienda, adminPdcto, agInventario, agReceta, busqueda, carrito, comprador, comprador_register, crearPerfil, editInventario, editarReceta, eliminarDelInventario, eliminarReceta, 
emprendedor_register, editarPdcto, eliminarPdcto, emprendedor, empPublico, gestionEmp, 
index, ingPdcto, inventario, login_request, logout_view, producto, recetas, regCompras, register,
editarPerfilEmp, verReceta
)

urlpatterns = [
    path('', index, name="index"),
    # path('', Index.as_view(), name="index"),
    path('login/', login_request, name="login"),
    path('logout/', logout_view, name='logout'),
    path('register/', register, name="register"),
    path('comprador_register/', comprador_register.as_view(), name="comprador_register"),
    path('emprendedor_register/', emprendedor_register.as_view(), name="emprendedor_register"),
    path('producto/<id>/', producto, name="producto"),
    path('carrito/', carrito, name="carrito"),
    path('emprendedor/', emprendedor, name="emprendedor"),
    path('comprador/', comprador, name="comprador"),
    path('ingPdcto/', ingPdcto, name="ingPdcto"),
    path('gestionEmp/', gestionEmp, name="gestionEmp"),
    path('regCompras', regCompras, name="regCompras"),
    path('busqueda/', busqueda, name="busqueda"),
    path('empPublico/', empPublico, name="empPublico"),
    path('adminPdcto/', adminPdcto, name="adminPdcto"),
    path('editarPdcto/<id>/', editarPdcto, name="editarPdcto"),
    path('eliminarPdcto/<id>/', eliminarPdcto, name="eliminarPdcto"),
    path('eliminarDelInventario/<id>/', eliminarDelInventario, name="eliminarDelInventario"),
    path('eliminarReceta/<id>/', eliminarReceta, name="eliminarReceta"),
    path('editarPerfilEmp/<id>/', editarPerfilEmp, name="editarPerfilEmp"),
    path('crearPerfil/', crearPerfil, name="crearPerfil"),
    path('aTienda/<id>/', aTienda, name="aTienda"),
    path('inventario/', inventario, name="inventario"),
    path('agInventario/', agInventario, name="agInventario"),
    path('editInventario/<id>/', editInventario, name="editInventario"),
    path('recetas/', recetas, name="recetas"),
    path('agReceta/', agReceta, name="agReceta"),
    path('verReceta/<id>/', verReceta, name="verReceta"),
    path('editarReceta/<id>/', editarReceta, name="editarReceta"),
]