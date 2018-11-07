from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('galeria/', galeria, name="galeria"),
    path('agregar-auto/', agregar_auto, name="agregar_auto"),
    path('listar-autos/', listar_autos, name="listar_autos"),
    path('eliminar-auto/<id>/',eliminar_auto, name="eliminar_auto"),

    path('service-worker.js',ServiceWorker.as_view(), name="service_worker"),
    path('api/listado-autos/', api_listado_autos, name="api_listado_autos"),
    path('api/eliminar-auto/<id>/', rest_eliminar, name="rest_eliminar"),
    path('api/agregar-auto/', api_agregar_auto, name="api_agregar_auto"),
    path('api/modificar-auto/', api_modificar_auto, name="api_modificar_auto"),
]
