from django.urls import path
from rest_producto.views import detalle_producto, lista_productos

urlpatterns = [
    path('lista_productos', lista_productos, name="lista_productos"),
    path('detalle_producto/<id>', detalle_producto, name="detalle_producto"),
]