from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import CreateView
from .models import Contacto, Producto, User, Perfil, Emprendedor
from .forms import CompradorRegister, ContactoForm, Crear_perfil_form, EmprendedorRegister, Perfil_mod_form
from django.views.generic import TemplateView




# Create your views here.

# def _get_form(request, formcls, prefix):
#         data = request.POST if prefix in request.POST else None
#         return formcls(data, prefix=prefix)

# class Index(TemplateView):
#     template_name = 'core/index.html'

#     def get(self, request, *args, **kwargs):
#         return self.render_to_response({'contactoform': ContactoForm(prefix='cform_pre')})

#     def post(self, request, *args, **kwargs):
#         contactoform = _get_form(request, ContactoForm, 'cform_pre')
#         if contactoform.is_bound and contactoform.is_valid():
#             # Process contactoform and render response
#             contactoform.save()
#             return self.render_to_response({'contactoform': contactoform})

def index(request):

    productos = Producto.objects.all()

    datos = {
        'form' : ContactoForm(),
        'productos' : productos
    }
    
    if request.method =='POST':
        formulario = ContactoForm(request.POST)
        
        if formulario.is_valid():
            formulario.save()

    return render(request, 'core/index.html', datos)

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
        return redirect('../crearPerfil/')



def crearPerfil(request):
    datos = {
        'form': Crear_perfil_form()
    }
    perfil = None
    if request.method == 'POST':
        formulario = Crear_perfil_form(request.POST, request.FILES)        
        if formulario.is_valid:
            perfil = formulario.save(commit=False)
            perfil.user_id = request.user.id
            perfil.save()
            return redirect('/')

    return render(request, 'core/crearPerfil.html', datos)

def editarPerfilEmp(request, id):

    perfil = get_object_or_404(Perfil, user_id=id)

    datos = {
        'perfil': perfil,
        'form': Perfil_mod_form(instance=perfil)
    }

    if request.method == 'POST':
        formulario = Perfil_mod_form(request.POST, instance=perfil, files=request.FILES)

        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Modificado correctamenta"

        datos["form"] = formulario

    return render(request, 'core/editarPerfilEmp.html', datos)

def producto(request):
    return render(request, 'core/producto.html')

def carrito(request):
    return render(request, 'core/carrito.html')

def emprendedor(request):
    perfil = Perfil.objects.all()

    datos = {
        'perfil': perfil
    }
    

    return render(request, 'core/emprendedor.html',datos)

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

