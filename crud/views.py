from django.shortcuts import render
from .models import Empleados

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Empleados
from .forms import EmpleadosForm


class EmpleadosList(ListView):
    model = Empleados
    template_name = 'crud/empleados_list.html'
    context_object_name = 'empleados'

    queryset = Empleados.objects.values('id_empleado', 'nombre', 'apellido','salario', 'email' ,)


def home(request):
    nombre = request.GET.get('nombre', '')
    apellido = request.GET.get('apellido', '')

    empleados = Empleados.objects.all()

    if nombre: 
        empleados = empleados.filter(nombre__icontains=nombre)
    if apellido:
        empleados = empleados.filter(apellido__icontains=apellido)
    
    return render (request, 'home.html', {
        'empleados': empleados,
        'nombre': nombre,
        'apellido': apellido
    })
