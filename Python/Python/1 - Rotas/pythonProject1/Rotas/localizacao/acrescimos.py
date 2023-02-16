def detalhes(rua, regiao, bairro, request):
    from django.shortcuts import render

    if regiao == ''

    respostas = {'rua': rua, 'bairro': bairro, 'regiao': regiao, }
    print(respostas)

    return render(request, 'endereco.html', {'respostas': respostas})


def remover_caracteres(rua):

    substituicao = {'á': 'a', 'à': 'a', 'â': 'a', 'ã': 'a',
                    'é': 'e', 'è': 'e', 'ê': 'e', 'ñ': 'n',
                    'í': 'i', 'ì': 'i', 'î': 'i',
                    'ó': 'o', 'ò': 'o', 'ô': 'o', 'õ': 'o',
                    'ú': 'u', 'ù': 'u', 'û': 'u',
                    'ç': 'c'}

    for k, v in substituicao.items():
        for c in rua:
            if k == c:
                rua = rua.replace(k, v)
    return rua

