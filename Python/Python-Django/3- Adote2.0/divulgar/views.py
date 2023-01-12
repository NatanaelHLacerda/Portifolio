from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Tag, Raca, Pet

@login_required
def novo_pet(request):
    if request.method=="GET":
        tags = Tag.objects.all()
        return render(request, 'novo_pet.html', {'tags': tags})
