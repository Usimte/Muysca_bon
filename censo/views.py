from django.shortcuts import render
from .models import registro_censo, censo_archivo
from .forms import upload_archivo_censo, form_registro_censo


def home(request):
    return render(request, 'censo/home.html')


def upload(request):
    if request.method == 'POST':
        form = upload_archivo_censo(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = upload_archivo_censo()
    return render(request, 'censo/cargar.html', {'form': form})


def datos(request):
    item = censo_archivo.get_
    return render(request, 'censo/ConjuntoDatos.html')


def registro(request):
    if request.method == 'POST':
        form = form_registro_censo(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = form_registro_censo()
    return render(request, 'censo/registro.html', {'form': form})
