def detalhes(rua, regiao, bairro):

    titulo = '\033[1;97m-=-=-=-=\033[m \033[1;93mLOCALIZAÇÃO DO PEDIDO\033[m \033[1;97m-=-=-=-=\033[m '
    print(titulo)

    print(f'\033[1;97mRegião ->\033[m {regiao} ')
    print(f'\033[1;97mLocalidade ->\033[m {bairro} ')


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

