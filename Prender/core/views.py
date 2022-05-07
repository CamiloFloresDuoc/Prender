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

def busqueda(request):
    return render(request, 'core/busqueda.html')

def empPublico(request):
    return render(request, 'core/empPublico.html')

def adminPdcto(request):
    return render(request, 'core/adminPdcto.html')

def editarPdcto(request):
    return render(request, 'core/editarPdcto.html')

def eliminarPdcto(request, pdcto_id):
    producto = Producto.objects.get(pdcto_id=pdcto_id)
    producto.delete()
    messages.success(request, "Producto eliminado Exitosamente!")
    return redirect(to="adminPdcto")

