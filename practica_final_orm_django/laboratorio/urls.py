#  URL's de aplicación "laboratorio"
from django.urls import path, reverse
from . import views


app_name = 'laboratorio'
urlpatterns = [
    path('', views.inicio, name='inicio_labs'),
    path('agregar/', views.agregar_labs, name='agregar_labs'),
    path('mostrar/', views.mostrar_labs, name='mostrar_labs'),
    path('editar/<int:pk>/', views.editar_labs, name='editar_labs'),
    path('editarregistro/<int:id>/', views.actualizar_labs, name='actualizar_labs'),
    path('eliminar/<int:pk>/', views.eliminar_labs, name='eliminar_labs'),
]
