from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from .models import Vehiculo

def index(request):
    return render(request, 'vehiculo/index.html')

@login_required
@permission_required('vehiculo.visualizar_catalogo', raise_exception=True)
def listar_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    
    for vehiculo in vehiculos:
        if vehiculo.precio <= 10000:
            vehiculo.condicion_precio = "Bajo"
        elif 10000 < vehiculo.precio <= 30000:
            vehiculo.condicion_precio = "Medio"
        else:
            vehiculo.condicion_precio = "Alto"
    
    return render(request, 'vehiculo/listar.html', {'vehiculos': vehiculos})

@login_required
@permission_required('vehiculo.agregar_vehiculo', raise_exception=True)
def agregar_vehiculo(request):
    pass
