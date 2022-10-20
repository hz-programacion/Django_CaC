from django.urls import path
from . import views
from productos.views import lista_clases, galeria, contacto

urlpatterns = [
    path('',views.index,name='inicio'),
    # path('saludar/',saludar, name='saludar'),
    # path('saludando/<str:nombre>', saludar_nombre, name='saludando'),
    path('lista-clases/', lista_clases, name='lista_clases'),
    path('clases/', lista_clases, name='clases'),
    path('galeria/', galeria, name='galeria'),
    path('contacto/', contacto, name='contacto')
    
]
