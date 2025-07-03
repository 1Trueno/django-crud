from django.db import models

# Create your models here.
class Empleado(models.Model):
    NOMBRE = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    email = models.EmailField()

    class Meta:
        db_table = 'dbo.EMPLEADOS'  # o el nombre real exacto de tu tabla