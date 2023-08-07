from django.shortcuts import render, redirect
from .models import*
from .forms import LaboratorioForm
from django.http import HttpResponse, HttpResponseRedirect


# Función página de inicio:
def inicio(request):
    return render(request, 'index.html')


# Función Mostrar Laboratorios:
def mostrar_labs(request):
   laboratorios = Laboratorio.objects.all()
   directores_generales = DirectorGeneral.objects.all()
   context = {
    'laboratorios':laboratorios,
    'directores_generales': directores_generales,
    }
   return render(request,'mostrar.html', context)


# Función Agregar Laboratorios:
def agregar_labs(request):
    if request.method == 'POST':
        form = LaboratorioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/mostrar/')
    else:
        form = LaboratorioForm()
    
    context = {
        'form': form
    }
    return render(request, 'insertar.html', context)


# Función Eliminar Laboratorios:
def eliminar_labs(request,pk): 
    laboratorio = Laboratorio.objects.get(id=pk)
    
    if request.method == 'POST':
        laboratorio.delete() 
        return redirect('/mostrar')

    context = {
        'laboratorio': laboratorio,
    }

    return render(request, 'eliminar.html', context)


# Editar Laboratorios:
def editar_labs(request,pk):
   laboratorio = Laboratorio.objects.get(id=pk)

   context = {
       'laboratorio': laboratorio,
   }
   return render(request, 'editar.html', context)


# Actualiza Laboratorios:
def actualizar_labs(request, id):
    nombre = request.POST['nombre']
    ciudad = request.POST['ciudad']
    pais = request.POST['pais']

    laboratorio = Laboratorio.objects.get(id=id)
    laboratorio.nombre = nombre
    laboratorio.ciudad = ciudad
    laboratorio.pais = pais
    laboratorio.save()

    return redirect ('/mostrar/')


