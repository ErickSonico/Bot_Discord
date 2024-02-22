import os, time, string, random, re
from random import randrange


def recomendarJuego():
    '''
    Elige un juego de forma aleatoria.
    
    :return El juego
    :rtype str
    '''
    juegos = ['Halo Wars',
          'Halo Reach',
          'Halo: Combat Evolved',
          'Halo 2',
          'Halo 3',
          'Halo 3: ODST',
          'Halo 4',
          'Halo 5: Guardians',
          'Halo Infinite',
          'Halo Wars 2']
    
    juego = random.choice(juegos)
    return juego

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

def datoCurioso():
    '''
    Elige un dato curioso de forma aleatoria.

    :return El dato curioso
    :rtype str
    '''
    datos = ['el flood es una evolución de los Precursores, los creadores de nuestro universo',
             'los forerunners son una raza que se autodenominaba como los guardianes de la galaxia',
             'los San \'Shyuum formaron una alianza con la humanidad antigua para combatir a los forerunners hace miles de años',
             'los Prometeos son vida artificial creada para combatir al flood',
             'Mendicant Bias es un constructo forerunner que se volvió en contra de su creador y ayudó al blood',
             'el equipo Noble estuvo compuesto por Spartan-III y Spartan-II',
             'los spartan se diseñaron para reprimir rebeliones en colonias humanas de otros mundos',
             'el nombre del Novato en Halo 3: ODST es Jonathan',
             'el planeta de donde vienen os Jiralhanae se llama Doisac',
             'Después de la guerra, los Sangheili se unieron a la humanidad para formar una alianza',
             'cuando el Covenant perdió la guerra, se dividió en facciones tales como La de Jul \'Mdama y Los Defensores de la Unica Libertad',
             'los spartan II fueron secuestrados de sus hogares cuando eran niños para ser entrenados como supersoldados',
             'el flood cuenta con una plaga logica que infecta sistemas de inteligencia artificial'
            ]
        
    dato = random.choice(datos)
    return dato

def recomendarMusica():
    '''
    Elige una canción de forma aleatoria.
    
    :return link del soundtrack
    :rtype str
    '''
    soundtracks =[
        'https://www.youtube.com/watch?v=Nie2-3L37EY',
        'https://www.youtube.com/watch?v=An43pufqcXY',
        'https://www.youtube.com/watch?v=p4mRgxIYtE0',
        'https://www.youtube.com/watch?v=aAKEdd_H0XY',
        'https://www.youtube.com/watch?v=5asR5mcYJmU',
        'https://www.youtube.com/watch?v=vDVDwgCQ6Qo',
        'https://www.youtube.com/watch?v=YMKf6j-AFIQ',
        'https://www.youtube.com/watch?v=kjmu5bj5yBA',
        'https://www.youtube.com/watch?v=g_OAjpbXRj4',
        'https://www.youtube.com/watch?v=Txraa3mELzw',
        'https://www.youtube.com/watch?v=0-TgUJ09AU8'
        ]
    soundtrack = random.choice(soundtracks)
    return soundtrack

def contarHistoria():
    # TODO: Poner historia de halo
    return

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