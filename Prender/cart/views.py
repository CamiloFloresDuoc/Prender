import stripe
import traceback

from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect

from .cart import Cart
from .forms import CheckoutForm

from core.utilities import checkout

def cart_detalle(request):

    cart = Cart(request)

    if request.method == 'POST':
        form = CheckoutForm(request.POST)

        if form.is_valid():
            stripe.api_key = settings.STRIPE_SECRET_KEY

            stripe_token = form.cleaned_data['stripe_token']

            try:
                charge = stripe.Charge.create(
                    amount = int(cart.get_total_cost()),
                    currency = 'USD',
                    description = 'pago app Prender',
                    source = stripe_token
                )

                nombre = form.cleaned_data['nombre']
                apellido = form.cleaned_data['apellido']
                email = form.cleaned_data['email']
                numero_telefono = form.cleaned_data['numero_telefono']
                direccion = form.cleaned_data['direccion']
                comuna = form.cleaned_data['comuna']    

                order = checkout(request, nombre, apellido, email, numero_telefono, direccion, comuna, cart.get_total_cost())
                cart.clear()

                return redirect('success')
            except Exception:
                traceback.print_exc()
                messages.error(request, 'Algo fallo con el pago')

    else: 
        form = CheckoutForm()


    remove_from_cart = request.GET.get('remove_from_cart', '')
    change_quantity = request.GET.get('change_quantity','')
    quantity = request.GET.get('quantity', 0)

    if remove_from_cart:
        cart.remove(remove_from_cart)
        return redirect('cart')
    
    if change_quantity:
        cart.add(change_quantity, quantity, True)
        return redirect('cart')

    return render (request, 'cart/carrito.html',{'form': form, 'stripe_pub_key':settings.STRIPE_PUB_KEY })

def success(request):
    query = request.GET.get('query', '')
    return render (request, 'cart/success.html',{'query':query})  


