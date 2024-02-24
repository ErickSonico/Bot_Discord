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
                r'.*buen(a|o)s (d(i|í)as|tardes|noches).*',
            ],
            'respuesta': [
                'Holaaaa',
                'Hola, soy la Halopedia.'
            ]
        },
        #////////////////////////////////////////////////Esepcies.
        {
            'intent': 'raza',
            'regex': [
                r'.*(cu(a|á)les|conoces|que).*(razas|especies|alien(i|í)genas).*',
            ],
            'respuesta': [
                'Existen varias de estas, por ejemplo tenemos',
                'Justo tuve recientemente mi clase de taxonomia, ahi te van'
            ]
        },
        #////////////////////////////////////////////////Humanos.
        {
            'intent': 'humano',
            'regex': [
                r'.*(que|h(a|á)blame|cu(e|é)ntame).*(humano|humanos).*',
            ],
            'respuesta': [
                'De ellos tengo la informacion siguiente ',
                'Masomenos he escuchado esto sobre ellos'
            ]
        },
        #////////////////////////////////////////////////Forerunners.
        {
            'intent': 'forerunners',
            'regex': [
                r'.*(que|h(a|á)blame|cu(e|é)ntame).*forerunners.*',
            ],
            'respuesta': [
                'De ellos tengo la informacion siguiente ',
                'Masomenos he escuchado esto sobre ellos'
            ]
        },
        #////////////////////////////////////////////////Flood.
        {
            'intent': 'flood',
            'regex': [
                r'.*(que|h(a|á)blame|cu(e|é)ntame).*flood.*',
            ],
            'respuesta': [
                'De ellos tengo la informacion siguiente ',
                'Masomenos he escuchado esto sobre ellos'
            ]
        },
        #////////////////////////////////////////////////Covenant.
        {
            'intent': 'covenant',
            'regex': [
                r'.*(que|h(a|á)blame|cu(e|é)ntame).*covenant.*',
            ],
            'respuesta': [
                'De ellos tengo la informacion siguiente ',
                'Masomenos he escuchado esto sobre ellos'
            ]
        },
        #////////////////////////////////////////////////Historia.
        {
            'intent': 'historia',
            'regex': [
                r'.*(cu(a|á)l|cu(e|é)ntame)?.* historia de (H|h)alo.*',
            ],
            'respuesta': [
                'Toma asiento que estas apunto de escuchar una obra maestra ',
                'Hmmm, vamos a ver si la recuerdo toda '
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
                r'.*(dime|cu(e|é)ntame|decirme)+ (un dato|algo curioso).*',
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
        #////////////////////////////////////////////////Imagen.
        {
            'intent': 'imagen',
            'regex': [
                r'.*(muestrame|ens(e|é)ñame|quiero ver|imagen|foto)+.*(jefe maestro|cortana|inquisidor|noble 6|novato|johnson|halsey|spark|carter|kat|jun|emile|jorge|buck|locke|tanaka|vale).*',
                r'.*(muestrame|ens(e|é)ñame|quiero ver|imagen|foto)+.*(jiralhanae|brutes|kig-yar|jackals|sangheili|elites|yanme|drones|skirmishers|huragok|hunters|mgalekgolo|grunts|unggoy|profetas|san \'shyum|flood).*'
            ],
            'respuesta': [
                'Aquí tienes:',
                'Claro:',
                'Halopedia al servicio:'
            ]
        },
        #////////////////////////////////////////////////Personajes.
        {
            'intent': 'personaje',
            'regex': [
                r'(.*)(|habla de|hablame de|quien es)+ (.*) (jefe maestro|cortana|inquisidor|noble 6|novato|johnson|halsey|spark|carter|kat|jun|emile|jorge|buck|locke|tanaka|vale)+.*',
            ],
            'respuesta': [
                'Un personaje muy interesante:',
                'Esta es una breve descripción sobre:',
                'Te contaré sobre:'
            ]
        },
        #////////////////////////////////////////////////Estado.
        {
            'intent': 'estado',
            'regex': [
                r'^(que tal|como)? (estas|te sientes).*',
            ],
            'respuesta': [
                'Feliz de poder compartir contigo mi conocimiento sobre el basto universo de Halo',
                'Emocionado de poder hablar sobre Halo',
                'Compartir mi conocimiento sobre Halo me hace muy feliz',
                'Si crece tu conocimiento sobre Halo mi propósito se habrá cumplido'
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
                'No debes de sentirte así, jugar Halo te animará',
                'Hablar sobre Halo te hará feliz',
                'Ese sentimineto se debe de erradicar con mi concomiento sobre Halo'
            ]
        },
        #////////////////////////////////////////////////Otro.
        {
            'intent': 'repetir',
            'regex': [
                r'.*(cuenta|cuentame|dime|di|saca)* (otro|otra).*',
                r'.*(otro|otra)+.*',
            ],
            'respuesta': [
                'Bueno...'
            ]
        },
        #////////////////////////////////////////////////Música.
        {
            'intent': 'musica',
            'regex': [
                r'.*(pon.*|toc.*|recom.*)+.*(m(u|ú)sica|canci(o|ó)n|soundtrack).*',
            ],
            'respuesta': [
                'Ahí te va:',
                'Esta es mi favorita:',
                'Aquí tienes:',
                'Halopedia al servicio:'
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