from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from .forms import SucursalForm, ProveedorForm, ClientesForm
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DeleteView

def inicio(request):
    return render(request, "AppEntrega/inicio.html")


def sucursal(request):
    if request.method=="POST":
        form=SucursalForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            numero=info["numero"]
            sucursal=Sucursal(nombre=nombre, numero=numero)
            sucursal.save()
            mensaje="Sucursal Creada!"   
        else:
            mensaje="Dastos Invalidos"
        formulario_sucursal=SucursalForm()
        return render(request, "AppEntrega/sucursal.html", {"formulario":formulario_sucursal,"mensaje":mensaje,})
    else:
        formulario_sucursal=SucursalForm()
    return render(request, "AppEntrega/sucursal.html", {"formulario": formulario_sucursal,})



def clientes(request):
    if request.method=="POST":
        form=ClientesForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            apellido=info["apellido"]
            email=info["email"]
            clientes=Cliente(nombre=nombre, apellido=apellido, email=email)
            clientes.save()
            mensaje="Cliente registrado!"     
        else:
            mensaje="Dastos Invalidos"
        formulario_clientes=ClientesForm()
        return render(request, "AppEntrega/clientes.html", {"formulario":formulario_clientes,"mensaje":mensaje,})
    else:
        formulario_clientes=ClientesForm()
    return render(request, "AppEntrega/clientes.html", {"formulario": formulario_clientes,})




def proveedores(request):
    if request.method=="POST":
        form=ProveedorForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            apellido=info["apellido"]
            email=info["email"]
            producto=info["producto"]
            proveedor=Proveedor(nombre=nombre, apellido=apellido, email=email, producto=producto)
            proveedor.save()
            mensaje="Proveedor Creado! "
            
        else:
            mensaje="Datos Invalidos"
        formulario_proveedor=ProveedorForm()
        proveedores=Proveedor.objects.all()
        return render(request, "AppEntrega/proveedores.html", {"mensaje":mensaje, "proveedores":proveedores })
    else:
        formulario_proveedor=ProveedorForm()
        proveedores=Proveedor.objects.all()
    return render(request, "AppEntrega/proveedores.html", {"formulario":formulario_proveedor, "proveedores":proveedores})




def busquedaSucursal(request):
    return render(request, "AppEntrega/busquedaSucursal.html",)


def buscar(request):
    sucursal=request.GET["numero"]
    if sucursal!="":
        sucursales=Sucursal.objects.filter(numero__icontains=sucursal)
        sucursales_=Sucursal.objects.all()
        return render(request, "AppEntrega/resultadosBusqueda.html", {"sucursales":sucursales, "sucursales_":sucursales_})
    else:
        sucursales_=Sucursal.objects.all()
        return render(request, "AppEntrega/busquedaSucursal.html", {"mensaje":"Datos invalidos", "sucursales_":sucursales_})
