from django.urls import path
from . import views
urlpatterns= [
    path('home', views.inicio, name="home"),
    path('alta_usuario/', views.alta_usuario, name="alta_usuario"),
    path('bbdd', views.ver_usuarios, name="base_de_datos"),
    path('busqueda_usuario', views.buscador_usuarios, name="busqueda_usuarios"),
    path('resultado_busqueda', views.buscar, name="resultado_busqueda"),
    path('eliminar_usuario/<int:id>', views.eliminar_usuario, name="eliminar_usuario"),
    path("editar_usuario/<int:id>", views.editar, name="editar_usuario")
    ]