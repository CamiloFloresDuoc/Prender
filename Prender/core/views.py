from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import CreateView
from .models import User
from .forms import CompradorRegister, ContactoForm, EmprendedorRegister




# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def indexUser(request):
    return render(request, 'core/indexUser.html')

def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                return redirect('/')
            else:
                messages.error(request,"Nombre usuario o contraseña invalidos")
        else:
                messages.error(request,"Nombre usuario o contraseña invalidos")
    return render(request, 'core/login.html',
    context={'form':AuthenticationForm()})

def logout_view(request):
     logout(request)
     return redirect('/')

def register(request):
    return render(request, 'core/register.html')

class comprador_register(CreateView):
    model = User
    form_class = CompradorRegister 
    template_name = 'core/comprador_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

class emprendedor_register(CreateView):
    model = User
    form_class = EmprendedorRegister 
    template_name = 'core/emprendedor_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')


    

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

