from django.contrib import admin
from django.urls import path
from django.urls import include
from crud import views
from crud.views import EmpleadosList, EmpleadosCreate, EmpleadosUpdate, EmpleadosDelete,DepartamentosCreate,DepartamentosDelete,DepartamentosUpdate
from django.shortcuts import redirect
#empleados/
urlpatterns = [
    path('admin/', admin.site.urls),
    #Usa redirect para que asi en el navegador me redirija automaticamente a empleados/ que seria home.html
    path('', lambda request: redirect('empleados/', permanent=True)),
    path('empleados/', views.home, name='home'),
    path('empleados/create/', EmpleadosCreate.as_view(), name='empleados_create'),
    path('empleados/update/<int:pk>/', EmpleadosUpdate.as_view(), name='empleados_update'),
    path('empleados/delete/<int:pk>/', EmpleadosDelete.as_view(), name='empleados_delete'),
    path('departamentos/', views.departamento_home, name='departamentos'),
    path('departamentos/create/', DepartamentosCreate.as_view(), name='departamento_create'),
    path('departamentos/update/<int:pk>/', DepartamentosUpdate.as_view(), name='departamento_update'),
    path('departamentos/delete/<int:pk>/', DepartamentosDelete.as_view(), name='departamento_delete'),
    
]
