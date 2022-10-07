import email
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from App.forms import * 


def inicio(request):
    return render (request, "App/inicio.html")
    
def post(request):
    return render (request, "App/BlogPost.html")

def crear_blog(request):

    if request.method == "POST":

        formulario_user = BlogForm(request.POST, request.FILES)

        if formulario_user.is_valid():
            info=formulario_user.cleaned_data
            tit=info["titulo"]
            subt=info["subtitulo"]
            cuerpo=info["cuerpo"]
            aut=info["autor"]
            fecha=info["fecha_pub"]
            cat=info["categoria"]
            img=info["img"]
            blog=Blog(titulo=tit, subtitulo=subt, cuerpo=cuerpo, autor=aut, fecha_pub=fecha, categoria=cat, img=img)
            blog.save()
            return render (request, "App/inicio.html", {'mensaje': "Blog publicado!"})
        else:
            return render (request, "App/crear_blog.html", {"formulario":formulario_user, 'mensaje': "Error en los datos"}) 
    else:
        formulario_user=BlogForm()
        return render (request, "App/crear_blog.html", {"formulario":formulario_user})



def pages(request):
    blogs=Blog.objects.all() 
    return render(request, "App/pages.html", {'blogs':blogs})

def publicacion(request):
    return render (request, "App/publicacion.html")

def busqueda(request):
    return render (request, "App/busqueda_tema.html")

def usuario(request):
    if request.method == "POST":

            formulario_user = UsuarioForm(request.POST, request.FILES)

            if formulario_user.is_valid():
                info=formulario_user.cleaned_data
                nom=info["nombre_usuario"]
                cont=info["contraseña"]
                mail=info["email"]
                blog=Blog(nombre_usuario=nom, contraseña=cont, email=mail)
                blog.save()
                return render (request, "App/inicio.html", {'mensaje': "Usuario Creado!"})
            else:
                return render (request, "App/crear_usuario.html", {"formulario":formulario_user, 'mensaje': "Error en los datos"}) 
    else:
            formulario_user=UsuarioForm()
            return render (request, "App/crear_usuario.html", {"formulario":formulario_user})

'''
nombre_usuario = forms.CharField(max_length=100)
    contraseña = forms.CharField(max_length=50)
    email = forms.EmailField(max_length = 254)
'''