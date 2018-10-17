from django.urls import path
from .views import home, galeria, agregar_auto,listar_autos,eliminar_auto

urlpatterns = [
    path('', home, name="home"),
    path('galeria/', galeria, name="galeria"),
    path('agregar-auto/', agregar_auto, name="agregar_auto"),
    path('listar-autos/', listar_autos, name="listar_autos"),
    path('eliminar-auto/<id>/',eliminar_auto, name="eliminar_auto"),
]
