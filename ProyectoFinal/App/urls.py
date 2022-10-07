from django.urls import path    
from App.views import *

urlpatterns = [
        path("", inicio, name="inicio"),
        path("post/", post, name="post"),
        path("crear_blog/", crear_blog, name="crear_blog"),
        path("pages/", pages, name="pages"),
        path("principal", publicacion, name="princiopal"),
        path("busqueda_tema", busqueda , name="busqueda_tema"),
        path("crear_usuario", usuario , name="crear_usuario"),
]