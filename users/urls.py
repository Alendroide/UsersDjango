from django.urls import path
from .views import *

urlpatterns = [
    path('crear/',Registrar,name='Registrar'),
    path('',Listar,name='Listar')
]