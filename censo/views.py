from django.shortcuts import render
from .models import registro_censo
from .forms import upload_archivo_censo


def home(request):
    return render(request, 'censo/home.html')

def upload(request):
    form = upload_archivo_censo()
    return render(request, 'censo/cargar.html', {'form': form})
