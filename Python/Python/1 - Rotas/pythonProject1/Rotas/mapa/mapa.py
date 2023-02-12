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

                      'planalto': ['adelina sales pereira', 'alfredo guzella', 'anibal andrade camara',
                                   'arthur lima de azevedo',
                                   'av doutor cristiano guimaraes', 'av dom pedro primeiro',
                                   'av general carlos guedes',
                                   'capitao leonidio soares', 'cel castro', 'cel fortes', 'cel costa dias',
                                   'cel quintiliano valadares',
                                   'david nasser', 'delio jose coelho',
                                   'deputado ultimo de carvalho',
                                   'dom carloto tavora', 'doutor jose ferolla', 'epaminondas de moura e silva',
                                   'fernando ferrari',
                                   'frei hilario', 'helio salomao', 'henrique horta', 'herculano dias coelho',
                                   'iracema souza pinto', 'irma celeste', 'joao fernandes de oliveira',
                                   'jornalista fernando carvalho',
                                   'jose oscar barreira', 'josue azevedo', 'lourival carneiro de vasconcelos',
                                   'luiz de mello mattos', 'maria ferreira dos santos',
                                   'manoel xavier macedo', 'mardocheu diniz', 'marechal rondon',
                                   'miguel aranha de azevedo',
                                   'nilo aparecida pinto',
                                   'nossa sra da eucaritia', 'otavio nicolai', 'pastor abreu',
                                   'praca padre julio maria', 'professor massanielo santos',
                                   'professor jose carvalho lopes',
                                   'professor tristao da cunha', 'professor teodoro vaz', 'recy souza paiva',
                                   'risoleta pinto sardinha',
                                   'roberto lucio aroeira',
                                   'rua dos carmelitas',
                                   'rua dos jesuitas', 'rua das clarissas',
                                   'rua dos maristas',
                                   'rua dos sacramentinos',
                                   'rua dos salesianos', 'rua dos vicentinos', 'sesostris leal paixao', 'sao felix',
                                   'sao jose do jacuri',
                                   'sao tomas', 'vereador orlando bonfim', 'wilde jose pereira',
                                   'wilsom soares fernandes', ],

                      'vila aeroporto': ['beco da amizade', 'beco beira muro', 'beco dos esportes', 'beco santa rosa',
                                         'beco sao bernardo', 'beco do joao pedro', 'eduardo quentel', 'rua d',
                                         'rua da paz', 'praca dos esportes', 'santo elias', 'washington luiz'], }

                     }

    for r, b in mapa.items():
        for nome_bairro, ruas in b.items():
            if rua in ruas:
                return detalhes(rua, r, nome_bairro)
