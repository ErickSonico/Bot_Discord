#----------------------------------------------------------------------
# Base de conocimiento
# La base de conocimiento representa una lista de todos los casos o intents.
#
# Cada caso o intent es un diccionario que incluye los siguientes keys (propiedades):
# - intent: Nombre para identificar el intent
# - regex: Lista de posibles expresiones regulares asociadas al intent, donde los parámetros se obtienen del texto parentizado en la expresión regular
# - respuesta: Lista de posibles respuestas al usuario, indicando los parámetros obtenidos con la notación %1, %2, %3, etc para cada parámetro
#----------------------------------------------------------------------
def conocimientoT():
    '''
    Define la base de conocimiento de glados

    :return El conicimiento a mostrar
    :rtype str 
    '''
    conocimiento = [
        #////////////////////////////////////////////////Bienvenida.
        {
            'intent': 'bienvenida',
            'regex': [
                r'.*hola.*',
                r'.*buen(a|o)s (dias|tardes|noches).*',
            ],
            'respuesta': [
                'Holaaaa',
                'Hola, soy la Halopedia.'
            ]
        },
        #////////////////////////////////////////////////Libro.
        {
            'intent': 'libro',
            'regex': [
                r'.*(recomienda|recomendar)+ .*(libro|novela).*',
            ],
            'respuesta': [
                'Te recomiendo',
                'Te podria gustar'
            ]
        },
        #////////////////////////////////////////////////Dato.
        {
            'intent': 'dato',
            'regex': [
                r'.*(dime|cuentame|decirme)+ (un dato|algo curioso).*',
            ],
            'respuesta': [
                'Sabias que',
                'Un dato curioso es que',
                'Te cuento que'
            ]
        },
        #////////////////////////////////////////////////Juegos.
        {
            'intent': 'juego',
            'regex': [
                r'.*(dime|recomiendame)+.*(juego).*',
            ],
            'respuesta': [
                'Este es mi favorito',
                'A la critica le gusta',
                'Una buena historia la tiene'
            ]
        },
        #////////////////////////////////////////////////Estado.
        {
            'intent': 'estado',
            'regex': [
                r'^(que tal|como)? (estas|te sientes).*',
            ],
            'respuesta': [
                'Feliz de poder compartir contigo mi conocimiento, sobre el basto universo de Halo',
                'Emocionado de poder hablar sobre Halo',
                'Compartir mi conocimiento sobre Halo me hacen muy feliz',
                'Si crece tu conocimiento sobre Halo mi proposito se habra cumplido'
            ]
        },
        #////////////////////////////////////////////////Emocion Negativa
        {
            'intent': 'negativo',
            'regex': [
                r'.* me siento (mal|triste|enojado|ansioso|perdido|solo)+',
                r'.* no me siento (bien|feliz|a gusto|trnquilo)'
            ],
            'respuesta': [
                'Mi conocimiento sobre Halo debe de animarte',
                'No debes de sentirte asi, jugar Halo te animara',
                'Hablar sobre Halo te hara feliz',
                'Ese sentimineto se debe de erradicar con mi concomiento sobre Halo'
            ]
        },
        #////////////////////////////////////////////////Otro.
        {
            'intent': 'repetir',
            'regex': [
                r'.*(cuentame|dime|saca)* otr(o|a).*',
                r'.*otr(o|a).*',
            ],
            'respuesta': [
                'Bueno...'
            ]
        },
        #////////////////////////////////////////////////Música.
        {
            'intent': 'musica',
            'regex': [
                r'.*(pon.*|toc.*|recom.*)+.*(musica|cancion|soundtrack).*',
            ],
            'respuesta': [
                'Ahí te va',
                'Esta es mi favorita:',
                'Aquí tienes'
            ]
        },
        #////////////////////////////////////////////////Fin.
        {
            'intent': 'terminar',
            'regex': [
                r'.*salir.*',
                r'.*adios.*',
                r'.*bye.*',
                r'.*hasta luego.*'
            ],
            'respuesta': [
                ''
            ]
        },
        #////////////////////////////////////////////////Cualquier caso no contemplado.
        {
            'intent': 'desconocido',
            'regex': [
                r'.*'
            ],
            'respuesta': [
                'No te entendí ¿Puedes repetirlo por favor?',
                'Creo que no tengo información al respecto; lo siento',
                'Disculpa, no comprendí lo que dices'
            ]
        }
        #////////////////////////////////////////////////
    ]
    return conocimiento