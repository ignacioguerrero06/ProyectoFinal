from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from App.forms import * 

# Create your views here.
def inicio(request):
    return render (request, "App/inicio.html")