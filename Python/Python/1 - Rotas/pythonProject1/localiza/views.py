from django.shortcuts import render
from django.http import HttpResponse
from Rotas.localizacao import mapa

# Create your views here.


def localiza(request):
    if request.method == "GET":
        return render(request, 'endereco.html')
    elif request.method == "POST":
        rua = request.POST.get('rua')
        resultado = mapa.pesquisa(rua, request, )

        return HttpResponse(resultado)
