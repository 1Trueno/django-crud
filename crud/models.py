from django.db import models

# Create your models here.
class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=200)

    class Meta:
        db_table = 'clientes'   # nombre real de la tabla en tu base
        managed = False  