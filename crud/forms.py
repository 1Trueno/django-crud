from django import forms
from .models import Empleados, Departamentos


class EmpleadosForm(forms.ModelForm):
    class Meta:
        model = Empleados
        fields = [
            'id_empleado',
            'nombre',
            'apellido',
            'email',
            'numero_telefono',
            'fecha_contrato',
            'id_puesto',
            'salario',
            'comision',
            'id_supervisor',
            'id_departamento',
        ]
        widgets = {
            'salario': forms.NumberInput(attrs={'min': 0})
        }

class DepartamentosForm(forms.ModelForm):
    class Meta:
        model = Departamentos
        fields = [
            'id_departamento',
            'nombre_departamento',
            'id_supervisor',
            'id_locacion',
        ]
