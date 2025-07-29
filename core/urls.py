from django.contrib import admin
from django.urls import path
from django.urls import include
from crud import views
from crud.views import EmpleadosList, EmpleadosCreate, EmpleadosUpdate, EmpleadosDelete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('empleados/create/', EmpleadosCreate.as_view(), name='empleados_create'),
    path('empleados/update/<int:pk>/', EmpleadosUpdate.as_view(), name='empleados_update'),
    path('empleados/delete/<int:pk>/', EmpleadosDelete.as_view(), name='empleados_delete'),
    
]
