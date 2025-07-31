from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Empleados,Puestos,Departamentos,Locaciones
from .forms import EmpleadosForm,DepartamentosForm
from django.shortcuts import redirect
from django.http import JsonResponse

# __________ Apartado de las funciones de Empleados __________
def home(request):
    nombre = request.GET.get('nombre', '')
    apellido = request.GET.get('apellido', '')

    # David: Hace que Django obtenga los datos del puesto y departamento de cada empleado en una sola consulta a la base de datos
    empleados = Empleados.objects.select_related('id_puesto','id_departamento',).all()

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

class EmpleadosList(ListView):
    model = Empleados
    template_name = 'crud/empleados_list.html'
    context_object_name = 'empleados'

    queryset = Empleados.objects.values('id_empleado', 'nombre', 'apellido','salario', 'email','id_supervisor')

class EmpleadosUpdate(UpdateView):
    model = Empleados
    form_class = EmpleadosForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        empleado = self.get_object()  # Obtenemos el objeto actual desde la base de datos

        # Solo actualizamos los campos que vienen del formulario (los visibles en el HTML)
        empleado.nombre = self.request.POST.get('nombre', empleado.nombre)
        empleado.apellido = self.request.POST.get('apellido', empleado.apellido)
        empleado.salario = self.request.POST.get('salario', empleado.salario)
        empleado.email = self.request.POST.get('email', empleado.email)
        empleado.id_puesto_id = self.request.POST.get('id_puesto', empleado.id_puesto_id)
        empleado.id_departamento_id = self.request.POST.get('id_departamento', empleado.id_departamento_id)

        empleado.save()
        return redirect(self.success_url)

    def form_invalid(self, form):
        print("Errores del formulario:", form.errors)
        return redirect(self.success_url)
    
class EmpleadosDelete(DeleteView):
    model = Empleados
    success_url = reverse_lazy('home')
    
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

# __________ Fin del apartado de las funciones de Empleados __________



# __________ Apartado de las funciones de Departamento __________
def departamento_home(request):
    nombre_dep = request.GET.get('nombre_dep')
    
    departamentos = Departamentos.objects.select_related('id_locacion').all()
    locaciones = Locaciones.objects.all()
    empleados = Empleados.objects.all()
    
    if nombre_dep:
        departamentos = Departamentos.objects.filter(nombre_departamento__icontains=nombre_dep)

    # Filtrar los id_supervisor únicos y no nulos
    supervisores_ids = Departamentos.objects.exclude(id_supervisor__isnull=True)\
                                            .values_list('id_supervisor', flat=True)\
                                            .distinct()

    return render(request, 'departamento.html', {
        'departamentos': departamentos,
        'empleados': empleados,
        'locaciones': locaciones,
        'supervisores_ids': supervisores_ids,
        'nombre_dep': nombre_dep,
    })

# Aqui se veran las funciones del CRUD de departamentos
class DepartamentoList(ListView):
    model = Departamentos
    template_name = 'crud/departamento_list.html'
    context_object_name = 'departamentos'

    queryset = Departamentos.objects.values('id_departamento', 'nombre_departamento',)

class DepartamentosUpdate(UpdateView):
    model = Departamentos
    form_class = DepartamentosForm
    success_url = reverse_lazy('departamentos')
    
    def form_valid(self, form):
        form.save()
        return redirect(self.success_url)
    

    def form_invalid(self, form):
        print("Errores del formulario:", form.errors)
        return redirect(self.success_url)

class DepartamentosDelete(DeleteView):
    model = Departamentos
    success_url = reverse_lazy('departamentos')  # Cambiado

#crear departamento
def crear_departamento (request):
    if request.method == 'POST':
        form = DepartamentosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('departamentos')
        else:
            print(form.errors)
    return redirect('departamentos')

# __________ Fin del apartado de las funciones de Departamentos __________