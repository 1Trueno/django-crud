from django.shortcuts import render
from .models import Empleado

# Create your views here.
def index(request):
    empleados = Empleado.objects.all()  # Trae todos los empleados
    return render(request, 'index.html', {'empleados': empleados})