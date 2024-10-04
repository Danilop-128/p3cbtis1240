from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, "index.html")

def contactos(request):
    return render(request, "contactos.html")

def empleado(request):
    return render(request, "empleado.html")

def clientes(request):
    return render(request, "clientes.html")

def productos(request):
    return render(request, "productos.html")

def proveedor(request):
    return render(request, "proveedor.html")

def venta(request):
    return render(request, "venta.html")