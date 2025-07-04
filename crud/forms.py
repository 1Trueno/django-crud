from django import forms
from .models import Empleados


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