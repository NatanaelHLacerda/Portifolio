from mapa.mapa import pesquisa
from mapa.acrescimos import remover_caracteres

while True:
    rua = ''
    for c in range(0, 1):
        if c == 0:
            rua = str(input('\033[1;93mDigite o nome da Rua: \033[m').lower())
            print()

    pesquisa(remover_caracteres(rua))
