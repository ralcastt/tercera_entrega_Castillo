from django.urls import path
from .views import *


urlpatterns = [
    path("sucursal/", sucursal, name="sucursal"),
    path("clientes/", clientes, name="clientes"),
    path("proveedores/", proveedores, name="proveedores"),
    path("busquedaSucursal", busquedaSucursal, name="busquedaSucursal"),
    path("buscar", buscar, name="buscar"),
    
    
    
]