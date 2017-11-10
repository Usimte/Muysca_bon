from django.conf.urls import url, static
from . import views

urlpatterns = [
    url(r'^$', views.home, name='Home'),
    url(r'^cargar$', views.upload, name='Upload'),
    url(r'^conjuntos_datos$', views.datos, name='ConjuntoDatos'),
    url(r'^registro$', views.registro, name='Registro')
]
