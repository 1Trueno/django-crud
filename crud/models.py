from django.db import models


class Empleados(models.Model):
    id_empleado = models.IntegerField(db_column='ID_EMPLEADO', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    apellido = models.CharField(db_column='APELLIDO', max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    numero_telefono = models.CharField(db_column='NUMERO_TELEFONO', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fecha_contrato = models.DateTimeField(db_column='FECHA_CONTRATO', blank=True, null=True)  # Field name made lowercase.
    id_puesto = models.CharField(db_column='ID_PUESTO', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    salario = models.IntegerField(db_column='SALARIO', blank=True, null=True)  # Field name made lowercase.
    comision = models.IntegerField(db_column='COMISION', blank=True, null=True)  # Field name made lowercase.
    id_supervisor = models.IntegerField(db_column='ID_SUPERVISOR', blank=True, null=True)  # Field name made lowercase.
    id_departamento = models.IntegerField(db_column='ID_DEPARTAMENTO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EMPLEADOS'
