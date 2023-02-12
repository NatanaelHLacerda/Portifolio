from mapa.mapa import pesquisa
from mapa.acrescimos import remover_caracteres

while True:
    rua = ''
    for c in range(0, 1):
        if c == 0:
            rua = str(input('Digite o nome da Rua: ').lower())

    pesquisa(remover_caracteres(rua))
