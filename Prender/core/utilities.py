from itertools import product
from cart.cart import Cart
from .models import Comprador, Order, OrderItem


def checkout (request, nombre, apellido, email, numero_telefono, direccion, comuna, total):
    comprador = Comprador.objects.get(user_id=request.user.id)
    order = Order.objects.create(nombre= nombre, apellido=apellido, email=email, numero_telefono=numero_telefono,
    direccion=direccion, comuna=comuna, total=total, comprador=comprador)

    for item in Cart(request):
        OrderItem.objects.create(order=order, producto = item['product'],vendedor=item['product'].user.user,
        precio=item['product'].valor_prod, cantidad = item['quantity']  )

        order.vendedor.add(item['product'].user.user)
    
    return order