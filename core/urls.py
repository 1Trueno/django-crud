from django.contrib import admin
from django.urls import path
from django.urls import include
from crud import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    
]
