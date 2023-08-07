# Para gestión de permisos
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

# Django
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, HttpResponseRedirect

# Django Local
from .forms import RegistroUsuarioForm, Form_ingreso_vehiculo
from .models import Vehiculo
from django.db import connection
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required


# ==== Página de inicio (index.html)
@login_required(login_url = '/login')
def index(request):
    return render(request, 'index.html')

# ==== Agregar nuevos vehículos a "Catálogo de vehículos"

@permission_required('vehiculo.add_vehiculo', login_url="/")
def agregar_vehiculo(request):
    if request.method == 'POST':
        form = Form_ingreso_vehiculo(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect ("/vehiculo/list/")
    else:
        form = Form_ingreso_vehiculo()
    context = {
            'forms':form
            }
    return render (request, 'agregar_vehiculo.html', context)

# ==== Categoría de precio (alto, medio o bajo)
def obtener_condicion_precio(precio):
    if precio <= 10000:
        categoria = 'Bajo'
    elif precio > 30000:
        categoria = 'Alto'
    else:
        categoria = 'Medio'
    return categoria

# ==== Catálogo de vehículos ingresados ====
@permission_required('vehiculo.view_vehiculo', login_url='/')
def listar_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    lista_vehiculos = []
    for vehiculo in vehiculos:
        condicion_precio = obtener_condicion_precio(vehiculo.precio)
        lista_vehiculos.append({
            'marca': vehiculo.marca,
            'modelo': vehiculo.modelo,
            'serial_carroceria': vehiculo.serial_carroceria,
            'serial_motor': vehiculo.serial_motor,
            'categoria': vehiculo.categoria,
            'precio': vehiculo.precio,
            'condicion_precio': condicion_precio,
        })
    context = {'vehiculos': lista_vehiculos}
    return render(request, 'listar_vehiculos.html', context)


# ================ FUNCIONES DE AUTENTICACIÓN ================

# ==== Iniciar sesión usuario ====
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Iniciaste sesion como: {username}")
                return HttpResponseRedirect("/")
            else:
                messages.error(request, "Username o password inválido")
                return HttpResponseRedirect("/")
    else:
        messages.error(request, "Username o password inválido")
        form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})

# ==== Crear nuevos usuarios ====
def registra_usuario(request):
    if request.method == "POST":

        form = RegistroUsuarioForm(request.POST)
        print(f'form es valido: {form.is_valid()}')
        if form.is_valid():
            # obtenemos el content type del modelo
            content_type = ContentType.objects.get_for_model(Vehiculo) # NUEVO
            
            # obtenemos el permiso a asignar
            visualizar_catalogo = Permission.objects.get(codename='visualizar_catalogo', content_type=content_type) # NUEVO
            view_vehiculo = Permission.objects.get(codename='view_vehiculo', content_type=content_type) # NUEVO*
            user = form.save()
            print(f"request: {request}")
            print(f"user: {user}")

            # Agregamos el permiso al usuario el momento de registrarse
            user.user_permissions.add(visualizar_catalogo, view_vehiculo)
            login(request, user)
            messages.success(request, "Registrado Satisfactoriamente.")
            return HttpResponseRedirect("/")


        else:
            messages.error(request, "Registro invalido. Algunos datos ingresados no son correctos")
            print('FALLO POST')
    else:
        form = RegistroUsuarioForm()
    return render(request=request, template_name="registro.html", context={"register_form": form})

# ==== Cerrar sesión usuario ====
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')



