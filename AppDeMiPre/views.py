from django.shortcuts import render, redirect
from AppDeMiPre.forms import Alta_formulario
from .models import Usuarios
from django.template import loader
from django.http import HttpResponse

def inicio(request):
    return render(request, "padre.html") #Respuesta del servidor


def ver_usuarios(request):
    usuarios = Usuarios.objects.all()
    dicc = {"usuarios": usuarios}
    plantilla = loader.get_template("base_de_datos.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)

def alta_usuario(request):
    if request.method == "POST":
        
        mi_formulario = Alta_formulario(request.POST)
        
        if mi_formulario.is_valid():
            
            datos = mi_formulario.cleaned_data
            print(datos)
            
            usuario = Usuarios(nombre=datos["nombre"], rol=datos["rol"])
            usuario.save()
            print("Guardado exitoso")
            return redirect("home")  # Redirige a la página de inicio después de guardar el usuario
        else:
            print(mi_formulario.errors)  # Imprime los errores de validación del formulario
    else:
        mi_formulario = Alta_formulario()
    
    return render(request, "registro_forms.html", {'form': mi_formulario})

def buscador_usuarios(request):
    return render(request, "buscar_usuarios.html")

def buscar(request):
    
    if request.GET["nombre"]:
        nombre= request.GET["nombre"]
        usuarios = Usuarios.objects.filter(nombre__icontains=nombre)
        return render (request, "resultado_busqueda.html", {"usuarios":usuarios})
    else:
        return HttpResponse("Ingrese el nombre del curso")

def eliminar_usuario(request, id):
    usuario = Usuarios.objects.get(id=id)
    usuario.delete()
    usuario = Usuarios.objects.all()
    return render(request, "base_de_datos.html", {"usuarios":usuario})

def editar(request, id):
    usuario = Usuarios.objects.get(id=id)
    if request.method == "POST":
        pass
    else:
        mi_formulario = Alta_formulario(initial={"nombre":usuario.nombre, "rol":usuario.rol})
    return render (request, "editar_usuario.html", {"miformulario":mi_formulario, "usuarios":usuario})