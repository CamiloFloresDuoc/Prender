from django.contrib import admin
from .models import User, Comprador, Emprendedor, Administrador, Contacto, Order, OrderItem


# Register your models here. todos!



admin.site.register(User)
admin.site.register(Comprador)
admin.site.register(Emprendedor)
admin.site.register(Administrador)
admin.site.register(Contacto)
admin.site.register(Order)
admin.site.register(OrderItem)
