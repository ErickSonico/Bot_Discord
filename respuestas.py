import random

def get_response(message:str)->str:
    mensaje = message.lower().strip()
    if 'hola' in mensaje:
        return 'Holaaaa'
    
    if mensaje == 'te necesitare cuando sea necesario por ahora descansa':
        return 'Despiertame cuando me necesites.'
    
    if mensaje == 'como estas jefe?':
        return 'Necesito un arma.'
    
    if mensaje == 'adios' or mensaje == 'chau' or mensaje == 'bye':
        return 'Bai, vuelve pronto!'
    
    if ('novelas' in mensaje or 'libros' in mensaje) and 'recomienda' in mensaje:
        return '¡Por supuesto! te recomiendo estas ' + ', '.join(random.sample(novelas, 3))
    
    if ('novela' in mensaje or 'libro' in mensaje) and 'recomienda' in mensaje:
        return '¡Por supuesto! te recomiendo esta ' + random.choice(novelas)
    
    if 'favorito' in mensaje and 'juego' in mensaje:
        return 'Mi juego favorito es ' + juegos[0]
    
    if 'juegos' in mensaje and 'orden' in mensaje:
        return 'El orden de los juegos es:\n' + '\n'.join(juegos)
    
    if ('libros' in mensaje or 'novelas' in mensaje) and 'orden' in mensaje:
        return 'El orden de los libros es:\n' + '\n'.join(novelas)
    
    if mensaje in datos:
        return random.choice(datos[mensaje])
    
    if mensaje == 'como estas?':
        return '¡Muy bien!, listo para el gran viaje'
    
    return 'No te entiendo, deberíamos activar los Halos' # respuesta por defecto

novelas = ['Halo: Cryptum',
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

datos = {'noble' : 
         ['El Equipo Noble fue un grupo de Spartan\'s III que lucharon en Reach', 'Noble Six fue el último miembro del equipo Noble, no está vivo en una cueva como muchos piensan'],

         'cortana' : 
         ['Cortana es una inteligencia artificial creada por Dr. Halsey, es la compañera de John-117', 'Cortana se sacrificó para salvar a John-117 en Halo 4', 'Se volvió mala después de Halo 5'],

         'jefe maestro' : 
         ['John-117, conocido como el Jefe Maestro, es un Spartan-II que luchó en la guerra contra el Covenant', 'Es todo un capo', 'Es un verdadero héroe', 'Gracias a él, la humanidad sobrevivió'],

         'halo' : 
         ['Los Halos son anillos gigantes que tienen la capacidad de destruir toda forma de vida inteligente en la galaxia', 'Fueron creados por los Forerunners', 'Son como un reinicio para la galaxia'],

         'flood' : 
         ['El Flood es un parásito que consume toda forma de vida con un sistema nervioso', 'Es una evolución de los Precursores, los arquitectos del universo', 'Es el enemigo más peligroso de la galaxia'],
}
