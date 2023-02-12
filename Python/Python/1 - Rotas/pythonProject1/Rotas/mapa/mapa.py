def pesquisa(rua):

    from .acrescimos import detalhes

    mapa = {'norte': {'são bernado': ['abilio peres da silva', 'adonis', 'av cecilia pinto', 'av cristiano machado',
                                      'av libania pena', 'av washington luiz', 'av waldomiro lobo', 'aderito tavora',
                                      'america', 'antonio jose diniz', 'antonio moreira pacheco',
                                      'armando ribeiro dos santos', 'bela vista', 'bernadino ventura', 'botafogo',
                                      'caetano dias', 'conceicão silencio luciano', 'delvaux vicente luciano',
                                      'dinorah ferreira messeder', 'doutor alberto horta', 'dr alberto horta',
                                      'dr souza gomes', 'edna quintel', 'edson tomas santos', 'enrique tamn',
                                      'flamengo', 'fluminense', 'francisco amancio ferreira', 'hero', 'francisco spino',
                                      'joao lopes de oliveira', 'jose alves dos reis', 'josue sotte', 'kenedy',
                                      'marcelo reginaldo gomes', 'maria amelia maia', 'padre antonio araujo',
                                      'rua dos beneditinos', 'rua dos salesianos', 'sao cristovao', 'rosalina rocha',
                                      'vasco da gama'],

                      'são tomaz': ['armando couto', 'barao de coromandel', 'beco b', 'carlos tomas', 'comendador wigg',
                                    'dez de novembro', 'dr jose rodrigues', 'geraldo antonio de freitas', 'imperatriz',
                                    'maria amelia maia', 'maria candida', 'nelia', 'portugal', 'rua dos jesuitas',
                                    'sao bento', 'sao tiago', 'sao luiz', 'santa bárbara', 'santa rosa',
                                    'santo antonio', 'santa rita de cassia', 'tancredo esteves', 'visconde de morais'],

                      'planalto': ['cel castro', 'cel fortes', 'irma celeste', 'nossa sra da eucaritia',
                                   'rua dos carmelitas',
                                   'rua dos jesuitas', 'rua dos maristas',
                                   'rua dos sacramentinos',
                                   'rua dos salesianos', 'rua dos vicentinos',
                                   'sao tomas'],

                      'vila aeroporto': ['beco da amizade', 'beco beira muro', 'beco dos esportes', 'beco santa rosa',
                                         'beco sao bernardo', 'beco do joao pedro', 'eduardo quentel', 'rua d',
                                         'rua da paz', 'praca dos esportes', 'santo elias', 'washington luiz'], }

                     }

    for r, b in mapa.items():
        for nome_bairro, ruas in b.items():
            if rua in ruas:
                return detalhes(rua, r, nome_bairro)
