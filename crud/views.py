from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Empleados,Puestos,Departamentos
from .forms import EmpleadosForm


class EmpleadosList(ListView):
    model = Empleados
    template_name = 'crud/empleados_list.html'
    context_object_name = 'empleados'

    queryset = Empleados.objects.values('id_empleado', 'nombre', 'apellido','salario', 'email' ,)


def home(request):
    nombre = request.GET.get('nombre', '')
    apellido = request.GET.get('apellido', '')

    #David: Hace que Django obtenga los datos del puesto y departamento de cada empleado en una sola consulta a la base de datos
    empleados = Empleados.objects.select_related('id_puesto','id_departamento').all()

    if nombre: 
        empleados = empleados.filter(nombre__icontains=nombre)
    if apellido:
        empleados = empleados.filter(apellido__icontains=apellido)
    
    return render(request, 'home.html', {
        'empleados': empleados,
        'nombre': nombre,
        'apellido': apellido,
        
    })

# Aqui se veran las funciones del CRUD de empleados

class EmpleadosCreate(CreateView):
    model = Empleados
    form_class = EmpleadosForm
    template_name = 'crud/empleados_form.html'
    success_url = reverse_lazy('home')

class EmpleadosUpdate(UpdateView):
    model = Empleados
    form_class = EmpleadosForm
    template_name = 'crud/empleados_form.html'
    success_url = reverse_lazy('home')

class EmpleadosDelete(DeleteView):
    model = Empleados
    template_name = 'crud/empleados_confirm_delete.html'
    success_url = reverse_lazy('home')