from django.urls import path
from .views import index
from .views import agregar_vehiculo
from .views import listar_vehiculos

urlpatterns = [
    path('', index, name='index'),
    path('vehiculo/add', agregar_vehiculo, name='agregar_vehiculo'),
    path('vehiculo/listar', listar_vehiculos, name='listar_vehiculos'),
]
