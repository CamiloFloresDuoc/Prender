from itertools import product
from cart.cart import Cart
from .models import Comprador, Order, OrderItem
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def checkout (request, nombre, apellido, email, numero_telefono, direccion, comuna, total):
    comprador = Comprador.objects.get(user_id=request.user.id)
    order = Order.objects.create(nombre= nombre, apellido=apellido, email=email, numero_telefono=numero_telefono,
    direccion=direccion, comuna=comuna, total=total, comprador=comprador)

    for item in Cart(request):
        OrderItem.objects.create(order=order, producto = item['product'],vendedor=item['product'].user.user,
        precio=item['product'].valor_prod, cantidad = item['quantity']  )

        order.vendedor.add(item['product'].user.user)
    
    return order

def notify_vendor(order):
    from_email = settings.DEFAULT_EMAIL_FROM

    for vendor in order.vendedor.all():
        to_email = vendor.user.email
        subject = 'Nuevo Pedido'
        text_content = 'Realizaron un pedido!'
        html_content = render_to_string('core/notificar_vendedor.html', {'order': order, 'vendor': vendor})

        msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
        msg.attach_alternative(html_content, 'text/html')
        msg.send()

def notify_customer(order):
    from_email = settings.DEFAULT_EMAIL_FROM

    to_email = order.email
    subject = 'Confirmación pedido'
    text_content = 'Gracias por realizar tu pedido!'
    html_content = render_to_string('core/notificar_comprador.html', {'order': order})

    msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()