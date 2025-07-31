from django.db import models

#Clase Puestos que trae los parametros de la tabla PUESTOS
class Puestos(models.Model):
    id_puesto = models.CharField(db_column='ID_PUESTO', primary_key=True, max_length=10)
    titulo_puesto = models.CharField(db_column='TITULO_PUESTO', max_length=35, blank=True, null=True)
    salario_minimo = models.IntegerField(db_column='SALARIO_MINIMO', blank=True, null=True)
    salario_maximo = models.IntegerField(db_column='SALARIO_MAXIMO', blank=True, null=True)

    class Meta:
        # Unica forma de que django nos deje trabajar con la base de datos (Anderson)  false ---> True
        managed = True
        db_table = 'PUESTOS'

#Clase Locaciones que trae los parametros de la tabla LOCACIONES
class Locaciones(models.Model):
    id_locacion = models.CharField(db_column='ID_LOCACION', primary_key=True, max_length=10)
    direccion = models.CharField(db_column='DIRECCION', max_length=40, blank=True, null=True)
    codigo = models.CharField(db_column='CODIGO_POSTAL', max_length=12, blank=True, null=True)
    ciudad = models.CharField(db_column='CIUDAD', max_length=30, blank=True, null=True)
    provincia = models.CharField(db_column='PROVINCIA', max_length=25, blank=True, null=True)
    id_pais = models.CharField(db_column='ID_PAIS', max_length=2, blank=True, null=True)
    


    class Meta:
    # Unica forma de que django nos deje trabajar con la base de datos (Anderson) false ---> True
        managed = False
        db_table = 'LOCACIONES'

#Clase Departamentos que trae los parametros de la tabla DEPARTAMENTOS
class Departamentos(models.Model):
    id_departamento = models.CharField(db_column='ID_DEPARTAMENTO', primary_key=True, max_length=10)
    nombre_departamento = models.CharField(db_column='NOMBRE_DEPARTAMENTO', max_length=35, blank=True, null=True)
    id_supervisor = models.IntegerField(db_column='ID_SUPERVISOR', blank=True, null=True)
    id_locacion = models.ForeignKey(Locaciones,db_column='ID_LOCACION', on_delete=models.DO_NOTHING, blank=True, null=True)


    class Meta:
    # Unica forma de que django nos deje trabajar con la base de datos (Anderson) false ---> True
        managed = True
        db_table = 'DEPARTAMENTOS'


class Empleados(models.Model):
    id_empleado = models.IntegerField(db_column='ID_EMPLEADO', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    apellido = models.CharField(db_column='APELLIDO', max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    numero_telefono = models.CharField(db_column='NUMERO_TELEFONO', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fecha_contrato = models.DateTimeField(db_column='FECHA_CONTRATO', blank=True, null=True)  # Field name made lowercase.
    id_puesto = models.ForeignKey(Puestos, db_column='ID_PUESTO', on_delete=models.DO_NOTHING, blank=True, null=True)
    salario = models.IntegerField(db_column='SALARIO', blank=True, null=True)  # Field name made lowercase.
    comision = models.IntegerField(db_column='COMISION', blank=True, null=True)  # Field name made lowercase.
    id_supervisor = models.IntegerField(db_column='ID_SUPERVISOR', blank=True, null=True)  # Field name made lowercase.
    id_departamento = models.ForeignKey(Departamentos,db_column='ID_DEPARTAMENTO', on_delete=models.DO_NOTHING, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # Unica forma de que django nos deje trabajar con la base de datos (Anderson) false ---> True
        managed = True
        db_table = 'EMPLEADOS'

