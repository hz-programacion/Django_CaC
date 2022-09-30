from django.urls import path
from productos.views import saludar

urlpatterns = [
    path('saludar/',saludar, name='saludar'),
]
