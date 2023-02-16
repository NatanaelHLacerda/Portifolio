from django.urls import path
from . import views

urlpatterns = [
    path('localiza/', views.localiza, name="localiza")
]