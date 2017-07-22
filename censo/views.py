from django.shortcuts import render
from .models import Registro_censo
from .forms import create_registro_censo


def home(request):
    return render(request, 'censo/home.html')

def upload(request):
    return render(request, 'censo/cargar.html')
