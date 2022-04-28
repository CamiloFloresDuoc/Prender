from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def login(request):
    return render(request, 'core/login.html')

def register(request):
    return render(request, 'core/register.html')

def producto(request):
    return render(request, 'core/producto.html')

def carrito(request):
    return render(request, 'core/carrito.html')

def emprendedor(request):
    return render(request, 'core/emprendedor.html')

def comprador(request):
    return render(request, 'core/comprador.html')

def ingPdcto(request):
    return render(request, 'core/ingPdcto.html')

def gestionEmp(request):
    return render(request, 'core/gestionEmp.html')

def regCompras(request):
    return render(request, 'core/regCompras.html')