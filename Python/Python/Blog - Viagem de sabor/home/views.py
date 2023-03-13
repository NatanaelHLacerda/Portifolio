from django.shortcuts import render
from django.http import HttpResponse
from publicar.models import Post

def home(request):
    post = Post.objects.all()

    if request.method == "GET":
        return render(request, 'home.html', {'posts': post})
