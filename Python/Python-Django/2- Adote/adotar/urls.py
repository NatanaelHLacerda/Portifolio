from django.urls import path
from . import views

urlpatterns = [
    path('listar_pets/', views.listar_pets, name="listar_pets"),
]