from django.urls import path
from . import views
urlpatterns=[
    path("",views.index,name="index"),
    path("contactos/",views.contactos,name="contactos"),
    path("empleado/",views.empleado,name="empleado"),
    path("clientes/",views.clientes,name="clientes"),
    path("productos/",views.productos,name="productos"),
    path("proveedor/",views.proveedor,name="proveedor"),
    path("venta/",views.venta,name="venta"),
]