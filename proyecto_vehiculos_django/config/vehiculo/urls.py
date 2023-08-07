#  URL's de aplicación "vehiculo"
from django.contrib import admin
from django.urls import path
from . import views
from django.urls import path
from . import views
from . views import*

app_name = "vehiculo"
urlpatterns = [
    path('', views.index, name='index'),
    path('login/',views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registro_uss/', views.registra_usuario, name='registro_uss'),
    path('vehiculo/add/', views.agregar_vehiculo, name='agregar_vehiculo'),
    path('vehiculo/list/', views.listar_vehiculos, name='listar_vehiculos'),
]
