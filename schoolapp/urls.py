from django.urls import path

from schoolapp.models import Programa 
from .views import home, crear_programa
import django.contrib.staticfiles

#Desde aquí se va acceder a las plantillas mediante
#a través de las vistas y las plantillas

#Ej1:
# view --> home
# templates - Plantilla inicio --> PlantillaHome.html

#Ej2:
#view --> Login
#templates - Usuarios --> crear_persona
#templates - Usuarios --> olvido_contraseña

urlpatterns = [
    path('',home), #Hace petición a la función home que esta en views
    path('crear/programa/',crear_programa)
]