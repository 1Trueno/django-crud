from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Empleados,Puestos,Departamentos
from .forms import EmpleadosForm,DepartamentosForm
from django.shortcuts import redirect
from django.http import JsonResponse


class EmpleadosList(ListView):
    model = Empleados
    template_name = 'crud/empleados_list.html'
    context_object_name = 'empleados'

    queryset = Empleados.objects.values('id_empleado', 'nombre', 'apellido','salario', 'email',)

def home(request):
    nombre = request.GET.get('nombre', '')
    apellido = request.GET.get('apellido', '')

    # David: Hace que Django obtenga los datos del puesto y departamento de cada empleado en una sola consulta a la base de datos
    empleados = Empleados.objects.select_related('id_puesto','id_departamento').all()

    if nombre: 
        empleados = empleados.filter(nombre__icontains=nombre)
    if apellido:
        empleados = empleados.filter(apellido__icontains=apellido)
    
    # AGREGAR ESTAS LÍNEAS PARA OBTENER TODOS LOS DEPARTAMENTOS Y PUESTOS
    departamentos = Departamentos.objects.all()
    puestos = Puestos.objects.all()
    
    return render(request, 'home.html', {
        'empleados': empleados,
        'departamentos': departamentos,  # NUEVO - para los selects
        'puestos': puestos,  # NUEVO - para los selects  
        'nombre': nombre,
        'apellido': apellido,
    })

# Aqui se veran las funciones del CRUD de empleados


class EmpleadosUpdate(UpdateView):
    model = Empleados
    form_class = EmpleadosForm
    success_url = reverse_lazy('home')
    

    def form_valid(self, form):
        form.save()
        return redirect(self.success_url)
    

    def form_invalid (self,form):
        print ("Errores del formulario:", form.errors)
        return redirect(self.success_url)
    

class EmpleadosDelete(DeleteView):
    model = Empleados
    success_url = reverse_lazy('home')
    
#Departamento
class DepartamentoList(ListView):
    model = Departamentos
    template_name = 'crud/departamento_list.html'
    context_object_name = 'departamentos'

    queryset = Departamentos.objects.values('id_departamento', 'nombre_departamento', 'id_supervisor', 'id_locacion' ,)

def departamento_home(request):
    nombre_dep = request.GET.get('nombre_dep')
    
    departamentos = Departamentos.objects.all()
    
    if nombre_dep:
        departamentos = Departamentos.objects.filter(nombre_departamento__icontains=nombre_dep)
    
    return render(request, 'departamento.html', {
        'departamentos': departamentos,
        'nombre_dep': nombre_dep,
    })

#crear empleado

def crear_empleado (request):
    if request.method == 'POST':
        form = EmpleadosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print(form.errors)
    return redirect('home')


class DepartamentosUpdate(UpdateView):
    model = Departamentos
    form_class = DepartamentosForm
    template_name = 'crud/departamentos_form.html'
    success_url = reverse_lazy('home')  

class DepartamentosDelete(DeleteView):
    model = Departamentos
    template_name = 'crud/departamentos_confirm_delete.html'
    success_url = reverse_lazy('home')  # Cambia aquí