import os, time, string, random, re
from random import randrange


def recomendarLibro():
    '''
    Eligue un libro de forma aleatoria.

    :return El libro
    :rtype str
    '''
    libros = ['Halo: Cryptum',
           'Halo: Primordium',
           'Halo: Silentium',
           'Halo: Fall Of Reach',
           'Halo: The Flood',
           'Halo: First Strike',
           'Halo: Ghosts of Onyx',
           'Halo: Contact Harvest',
           'Halo: The Cole Protocol',
           'Halo: Broken Circle',
           'Halo: New Blood',
           'Halo: Hunters in the Dark',
           'Halo: Saint\'s Testimony',
           'Halo: Last Light',
           'Halo: Shadow of Intent',
           'Halo: Smoke and Shadow',
           'Halo: Envoy',
           'Halo: Retribution',
           'Halo: Legacy of Onyx',
           'Halo: Bad Blood',
           'Halo: Renegades',
           'Halo: Oblivion',
           'Halo: Shadows of Reach',
           'Halo: Divine Wind',
           'Halo: Point of Light',
           'Halo: The Rubicon Protocol',
           'Halo: Epitaph'
           ]
    libro = random.choice(libros)
    return libro

def despedida(user_input):
    '''
    Devuelve la despedida de glados

    :param str user_input: El texto escrito por el usuario
    :return La despedida de glados
    :rtype str
    '''
    des = user_input.split()
    despedida_usuario = ['salir', 'adios', 'bye', 'hasta luego', 'adiós']
    despedida_glados = ['Adiós', 'Bye!', '¡Hasta la vista, baby!']
    despedida_definitiva = ''
    for i in des:
        if i in des:
            despedida_definitiva = random.choice(despedida_glados)
    return despedida_definitiva
