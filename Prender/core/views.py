from ast import Lambda
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import CreateView
from .models import Categoria, Contacto, Inventario, Producto, Receta, User, Perfil, Emprendedor
from .forms import CompradorRegister, ContactoForm, Crear_perfil_form, EmprendedorRegister, InventarioForm, Perfil_mod_form, ProductoForm, RecetaForm
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

    #[:12] para cargar los ultimos 12
    productos = Producto.objects.all()[:12]
    categorias = Categoria.objects.all()

    datos = {
        'form' : ContactoForm(),
        'productos' : productos,
        'categorias' : categorias
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

def producto(request, id):

    prod = Producto.objects.get(id=id).user_id
    tienda = Perfil.objects.get(id=prod)
    producto = Producto.objects.filter(id=id)

    datos = {
        'producto': producto,
        'id' : id,
        'tienda': tienda
    }
    return render(request, 'core/producto.html', datos)



def carrito(request):
    return render(request, 'core/carrito.html')

def emprendedor(request):
    perfil = Perfil.objects.all()
    perfil_actual = Perfil.objects.get(user_id=request.user.id).id 
    productos = Producto.objects.all().filter(user_id = perfil_actual)
    #array de solo categorias que existan en los productos del perfil
    categorias_id = set(map( lambda p : p.categoria_id ,productos))
    categorias =  Categoria.objects.filter(id__in= categorias_id)
    
    datos = {
        'perfil': perfil,
        'productos' : productos,
        'categorias' : categorias
    }
    

    return render(request, 'core/emprendedor.html',datos)

def comprador(request):
    return render(request, 'core/comprador.html')

def aTienda(request, id):

    perfil = Perfil.objects.get(id=id)
    tienda = Perfil.objects.filter(id=id)
    productos = Producto.objects.all().filter(user_id = id)
    categorias_id = set(map( lambda p : p.categoria_id ,productos))
    categorias =  Categoria.objects.filter(id__in= categorias_id)

    datos = {
        'tienda' : tienda,
        'id': id,
        'productos': productos,
        'categorias': categorias,
        'perfil': perfil
    }

    return render(request, 'core/aTienda.html', datos)

def ingPdcto(request):

    perfil = Perfil.objects.get(user_id=request.user.id).id 
    #perfil especifico logeado que quedara como clave foranea del producto

    datos = {
        'form' : ProductoForm()
    }
    producto = None
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, request.FILES)

        if formulario.is_valid():
            producto = formulario.save(commit=False)
            producto.user_id = perfil
            producto.save()
            datos['mensaje'] = "Producto creado correctamenta"
            return redirect(to="adminPdcto")

    return render(request, 'core/ingPdcto.html', datos)

def gestionEmp(request):
    return render(request, 'core/gestionEmp.html')

def regCompras(request):
    return render(request, 'core/regCompras.html')

def busqueda(request):
    return render(request, 'core/busqueda.html')

def empPublico(request):
    return render(request, 'core/empPublico.html')

def adminPdcto(request):

    perfil = Perfil.objects.get(user_id=request.user.id).id 
    productos = Producto.objects.all().filter(user_id = perfil)

    datos ={
        'productos' : productos
    }

    return render(request, 'core/adminPdcto.html', datos)

def editarPdcto(request, id):

    productos = get_object_or_404(Producto, id=id)

    datos = {
        'form' : ProductoForm(instance=productos)
    }
    
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, instance=productos, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['form'] = formulario
            return redirect(to="adminPdcto")

    return render(request, 'core/editarPdcto.html', datos)

def eliminarPdcto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    return redirect(to="adminPdcto")

def eliminarDelInventario(request, id):
    inventario = Inventario.objects.get(id=id)
    inventario.delete()
    return redirect(to="inventario")

def eliminarReceta(request, id):
    receta = Receta.objects.get(id=id)
    receta.delete()
    return redirect(to="recetas")

def inventario(request):

    perfil = Perfil.objects.get(user_id=request.user.id).id 
    inventario = Inventario.objects.all().filter(user_id= perfil)

    datos = {
        'inventario': inventario
    }

    return render(request, 'core/inventario.html', datos)

def agInventario(request):

    perfil = Perfil.objects.get(user_id=request.user.id).id 

    datos = {
        'form' : InventarioForm()
    }
    inventario = None
    if request.method == 'POST':
        formulario = InventarioForm(request.POST, request.FILES)

        if formulario.is_valid():
            inventario = formulario.save(commit=False)
            inventario.user_id = perfil
            inventario.save()
            datos['mensaje'] = "Producto creado correctamenta"
            return redirect(to="inventario")

    return render(request, 'core/agInventario.html', datos)

def editInventario(request,id):

    inventario = get_object_or_404(Inventario, id=id)

    datos = {
        'form' : InventarioForm(instance=inventario)
    }

    if request.method == 'POST':
        formulario = InventarioForm(request.POST, instance=inventario)
        if formulario.is_valid():
            formulario.save()
            datos['form'] = formulario
            return redirect(to="inventario")

    return render(request, 'core/editInventario.html', datos)

def recetas(request):

    perfil = Perfil.objects.get(user_id=request.user.id).id 
    receta = Receta.objects.all().filter(user_id= perfil)

    datos = {
        'receta': receta
    }

    return render(request, 'core/recetas.html', datos)

def agReceta(request):

    perfil = Perfil.objects.get(user_id=request.user.id).id 

    datos = {
        'form' : RecetaForm()
    }
    receta = None
    if request.method == 'POST':
        formulario = RecetaForm(request.POST, request.FILES)

        if formulario.is_valid():
            receta = formulario.save(commit=False)
            receta.user_id = perfil
            receta.save()
            datos['mensaje'] = "Receta creada correctamenta"
            return redirect(to="recetas")
    return render(request, 'core/agReceta.html', datos)

def verReceta(request, id):

    rece = Receta.objects.get(id=id).user_id
    tienda = Perfil.objects.get(id=rece)
    receta = Receta.objects.filter(id=id)

    datos = {
        'receta': receta,
        'id' : id,
        'tienda': tienda
    }
    return render(request, 'core/verReceta.html', datos)

def editarReceta(request, id):

    recetas = get_object_or_404(Receta, id=id)

    datos = {
        'form' : RecetaForm(instance=recetas)
    }

    if request.method == 'POST':
        formulario = RecetaForm(request.POST, instance=recetas)
        if formulario.is_valid():
            formulario.save()
            datos['form'] = formulario
            return redirect(to="recetas")
    return render(request, 'core/editarReceta.html',datos)