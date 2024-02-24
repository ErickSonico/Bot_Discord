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

def descripcionPersonaje(user_input):
    '''
    Devuelve la descripción del personaje elegido
    '''
    personajes = {
        
        'jefe maestro' : '**Jefe Maestro** \n El Jefe Maestro, cuyo nombre real es John-117, es el personaje principal y protagonista de la serie de videojuegos. Es un supersoldado genéticamente mejorado conocido como Spartan-II, creado por el Proyecto SPARTAN-II del UNSC (United Nations Space Command). El Jefe Maestro es reconocido por su armadura verde distintiva y su visor opaco que oculta su rostro. Es un experto en combate, tácticas militares y manejo de armas avanzadas. A lo largo de la serie "Halo", el Jefe Maestro es protagonista y líder de numerosas misiones para proteger a la humanidad de amenazas alienígenas, especialmente del Covenant y del Flood. Su determinación, habilidades de combate y lealtad al deber lo convierten en un icono dentro del universo de Halo.',
        
        'cortana' : '**Cortana** \n Cortana es un personaje de inteligencia artificial (IA) en la serie de videojuegos. Fue creada por el Dr. Catherine Halsey como una IA avanzada basada en la personalidad de Halsey y programada para asistir al Jefe Maestro en sus misiones. Cortana se presenta como un holograma azul femenino con una voz sintética. Posee una inteligencia excepcional, capaz de procesar información a gran velocidad y proporcionar análisis tácticos en tiempo real. A lo largo de la serie, Cortana demuestra habilidades de piratería informática, capacidad de comunicación con sistemas alienígenas y una comprensión profunda de la tecnología Forerunner. Su relación con el Jefe Maestro es de confianza y compañerismo, y su papel es crucial en la historia, ya que proporciona orientación y apoyo durante las misiones.',
        
        'inquisidor' : "**El inquisidor** \n El Inquisidor, cuyo nombre completo es Thel 'Vadam, es un Sangheili (comúnmente conocido como Elite). Antes de convertirse en el Inquisidor, 'Vadam era el Comandante Supremo del Covenant y un devoto seguidor de la fe religiosa del Covenant. \n Después de los eventos de Halo 2, donde fue traicionado y despojado de su rango por el Profeta de la Verdad, 'Vadam se une al Jefe Maestro en su lucha contra el Covenant tras darse cuenta de la traición y las mentiras del liderazgo Covenant. Eventualmente, 'Vadam asume el papel de Inquisidor y lidera una facción de los Sangheili en la lucha contra el Covenant y los Flood. \n El Inquisidor es un personaje complejo que experimenta un profundo desarrollo a lo largo de la serie, desde ser un enemigo del Jefe Maestro hasta convertirse en su aliado y luchar juntos por un objetivo común: derrotar a los enemigos que amenazan a la humanidad y al Covenant. Su papel en la historia de Halo es crucial para el desarrollo del conflicto y para la comprensión de la complejidad del universo del juego.",
        
        'noble 6' : '**Noble 6** \n Noble 6 es un Spartan-III asignado al Noble Tean en Halo Reach. Este soldado altamente habilidoso y valiente juega un papel crucial en la defensa del planeta Reach contra las fuerzas del Covenant. A lo largo del juego, Noble 6 lidera misiones peligrosas y demuestra una tenacidad inquebrantable en el campo de batalla. Su dedicación a la misión y su capacidad para enfrentarse a desafíos abrumadores lo convierten en un miembro valioso del equipo. Sin embargo, su sacrificio final, al proteger la evacuación de Reach y permitir que el Jefe Maestro continúe la lucha contra el Covenant, lo consagra como un héroe legendario en el universo de Halo, dejando un legado perdurable de coraje y sacrificio.',
        
        'novato' : '**El novato** \n El novato es un personaje anónimo y silencioso que forma parte del Pelotón Orbital de Choque durante los eventos de Halo 3: ODST. Después de ser separado de su equipo durante un aterrizaje forzoso en Nueva Mombasa, el Novato despierta horas después para encontrarse solo en la ciudad invadida por el Covenant. A través de flashbacks que experimenta mientras investiga la ciudad en busca de pistas sobre sus compañeros perdidos, se revela que es un miembro valioso y leal del pelotón. Su determinación para reunir al equipo y completar la misión, a pesar de enfrentarse a desafíos abrumadores y una amenaza aparentemente imposible, muestra su valentía y su compromiso con sus compañeros y su deber como soldado del UNSC. A medida que avanza en su búsqueda, el Novato demuestra habilidades tácticas y de combate excepcionales, ganándose el respeto de sus compañeros y dejando un impacto duradero en la historia de Halo.',
        
        'johnson' : '**Sargento Johnson** \n El Sargento Avery Junior Johnson, más conocido como el Sargento Johnson, es un veterano soldado del UNSC (United Nations Space Command) con una larga historia de servicio en las guerras contra el Covenant y otras amenazas. Johnson es conocido por su personalidad carismática, su sentido del humor y su valentía en el campo de batalla. Aparece en varios juegos de la serie, incluyendo Halo: Combat Evolved, Halo 2, Halo 3, Halo 3: ODST y Halo: Reach. En estos juegos, el Sargento Johnson sirve como un aliado clave para el Jefe Maestro y otros personajes principales, brindando apoyo táctico, liderazgo y sabiduría militar. A lo largo de la serie, el Sargento Johnson se enfrenta a numerosos desafíos y peligros, pero siempre muestra una determinación inquebrantable y un espíritu combativo. Su presencia en la serie ha dejado una marca duradera y lo ha convertido en uno de los personajes más queridos.',
        
        'halsey' : '**Doctora Catherine Halsey** \n Catherine Elizabeth Halsey es una científica brillante y controvertida, conocida por su liderazgo en la creación del Proyecto SPARTAN-II. Responsable de reclutar niños para convertirlos en supersoldados, su ética cuestionable y métodos controversiales han generado debate dentro del UNSC. Además, Halsey es la mente detrás de Cortana, la inteligencia artificial que asiste al Jefe Maestro, añadiendo una capa de complejidad a su personaje. A lo largo de la serie, su desarrollo revela una persona con profundidad moral y emocional, cuyas acciones tienen consecuencias significativas en la lucha contra el Covenant y en el universo de Halo.',
        
        'spark' : '**343 Guilty Spark** \n 343 Guilty Spark es una inteligencia artificial Forerunner creada para administrar y proteger las instalaciones de los Anillos Halo. Aparece por primera vez en Halo: Combat Evolved como una figura enigmática que guía al Jefe Maestro a través de la instalación Halo. A medida que avanza la saga, se revela que Guilty Spark está programado para activar los Halos en caso de que los Flood amenacen la galaxia, lo que lo convierte en un personaje ambiguo cuyas acciones y lealtades son difíciles de predecir. A lo largo de la serie, su presencia añade una capa de misterio y sus motivaciones se vuelven cada vez más complejas, lo que lo convierte en un personaje intrigante.',
        
        'carter' : '**Carter (Noble 1)** \n Carter-A259 (Noble 1), también conocido como Noble 1, es el líder del Noble Team y un Spartan-III altamente capacitado. Antes de los eventos de Halo: Reach, Carter lideró numerosas misiones contra el Covenant, demostrando habilidades tácticas excepcionales y un compromiso inquebrantable con la misión y la protección de la humanidad. Durante la batalla por Reach, muestra un liderazgo valiente al dirigir al Noble Team en la defensa del planeta, tomando decisiones difíciles para asegurar la supervivencia de su equipo. Su sacrificio final al estrellar su Pelican en un Crucero de Batalla Covenant para permitir que su equipo escape es un acto de heroísmo que lo convierte en un símbolo de liderazgo y sacrificio.',
        
        'kat' : '**Kat (Noble 2)** \n Kat-B320 (Noble 2), la segunda al mando del Noble Team y jefa de operaciones, es una Spartan-III conocida por su habilidad con la tecnología y su enfoque pragmático. Antes de unirse al Noble Team, Kat sobrevivió a un encuentro devastador con los Covenant que dejó a su equipo anterior diezmado, lo que la llevó a unirse al Noble Team. Durante la batalla por Reach, desempeña un papel crucial en la coordinación de misiones y la toma de decisiones tácticas, utilizando su experiencia y habilidades para guiar al equipo. Sin embargo, su vida llega a un trágico final cuando es asesinada por un francotirador Sangheili mientras intentaba asegurar un artefacto Forerunner crucial para la misión. Su muerte deja al equipo devastado y sirve como un recordatorio doloroso de los sacrificios necesarios en la lucha contra el Covenant.',
        
        'jun' : '**Jun (Noble 3)** \n Jun-A266 (Noble 3), el francotirador del Noble Team, es un experto en operaciones encubiertas y reconocimiento. Antes de unirse al Noble Team, Jun sirvió como miembro de élite de las fuerzas especiales de la UNSC, demostrando habilidades excepcionales en combate y reconocimiento. Durante la batalla por Reach, Jun utiliza su habilidad excepcional con el rifle de francotirador para proporcionar apoyo desde la distancia, eliminando objetivos de alto valor con precisión letal. Aunque sobrevive a los eventos de Halo: Reach, su destino después de la caída de Reach no se detalla en el juego principal. Sin embargo, se le ve en otros medios relacionados con Halo, continuando su lucha contra el Covenant y otras amenazas.',
        
        'emile' : 'Emile (Noble 4)** \n Emile-A239 (Noble 4), conocido por su ferocidad en el combate y su habilidad en combate cuerpo a cuerpo, es un Spartan-III especializado en operaciones de asalto y defensa. Antes de unirse al Noble Team, Emile sirvió en numerosas misiones de combate contra el Covenant, demostrando su determinación y valentía en el campo de batalla. Durante la batalla por Reach, Emile se destaca en enfrentamientos directos con el enemigo, mostrando una ferocidad implacable mientras defiende una instalación crucial contra el Covenant. Sin embargo, su vida llega a un fin trágico cuando es asesinado por un Sangheili Zealot mientras defiende la instalación, sacrificando su vida para proteger a sus compañeros y cumplir con la misión.',
        
        'jorge' : '**Jorge (Noble 5)** \n Jorge-052 (Noble 5), conocido por su lealtad y valentía, es el artillero pesado del Noble Team y un Spartan-II de gran estatura y fuerza. Antes de unirse al Noble Team, Jorge sirvió en misiones altamente clasificadas, demostrando su habilidad en combate y su dedicación a la protección de la humanidad. Durante la batalla por Reach, Jorge desempeña un papel crucial en varias misiones, incluida la entrega de un dispositivo nuclear improvisado al Covenant para destruir un supertransportador en órbita. Aunque sobrevive a la misión, sacrifica su vida para asegurar que el dispositivo se detone correctamente, lo que resulta en la destrucción del supertransportador y la salvación temporal de Reach. Su sacrificio final es un acto de heroísmo que lo convierte en un símbolo de valentía y determinación para el Noble Team y la humanidad.',
        
        'buck' : '**Buck** \n El Sargento Edward Buck, conocido como Buck, es un veterano carismático y líder del equipo Orbital Drop Shock Troopers (ODST) en Halo 3: ODST. Guía al equipo Alpha-Nine en una misión en la Ciudad de Nueva Mombasa, mostrando habilidades excepcionales en combate y liderazgo mientras buscan al Novato. Su determinación para cumplir con la misión y proteger a su equipo lo convierten en un personaje querido por los fans de la saga "Halo". Tras los eventos de Halo 3: ODST, Buck se convierte en un Spartan-IV y es miembro del Equipo Osiris, junto con Locke, Vale y Tanaka. Después de los eventos de Halo 4, Buck se une a la agencia de inteligencia ONI (Oficina de Inteligencia Naval) y es reclutado por Jameson Locke para formar parte de su equipo de élite. Buck demuestra ser un activo valioso para el Equipo Osiris, mostrando sus habilidades de combate y liderazgo mientras luchan contra los rebeldes Covenant y la facción separatista conocida como "Los Susurros de la Verdad". Su presencia en el juego agrega profundidad al personaje y establece su importancia continua en el universo de Halo. Buck también aparece en la serie animada Halo: The Fall of Reach y en la novela Halo: New Blood, lo que amplía su trasfondo y desarrollo como personaje. Su evolución de un ODST a un Spartan-IV refleja su determinación y compromiso continuo con la lucha contra las amenazas que enfrenta la humanidad en el universo de Halo.',
        
        'locke' : '**Locke (Equipo Osiris)** \n Jameson Locke es el líder del equipo Osiris en Halo 5: Guardians. Como ex-agente de la Oficina de Inteligencia Naval (ONI), Locke es conocido por su determinación inflexible y su habilidad para resolver problemas en situaciones de alta presión. Su formación en la ONI le ha otorgado habilidades excepcionales en el combate, así como una capacidad única para planificar y ejecutar misiones de alto riesgo. Locke es un líder respetado que inspira confianza en sus compañeros de equipo y es fundamental para mantener la cohesión y la efectividad de Osiris durante las misiones más peligrosas.',
        
        'tanaka' : '**Tanaka (Equipo Osiris) \n Holly Tanaka es una ingeniera altamente cualificada que se une al equipo Osiris con experiencia en ingeniería mecánica y robótica. Su conocimiento técnico es fundamental para el éxito del equipo en misiones que requieren el uso de tecnología avanzada, reparaciones rápidas o manipulación de sistemas complejos. Tanaka es reconocida por su habilidad para resolver problemas técnicos en el campo y su capacidad para improvisar soluciones ingeniosas en situaciones de emergencia. Su perspectiva científica y su enfoque metódico complementan las habilidades de combate de sus compañeros de equipo, asegurando que Osiris esté preparado para enfrentar cualquier desafío.',
        
        'vale' : '**Vale (Equipo Osiris)** \n Olympia Vale, también conocida como "Vale", es una ex-lingüista militar y experta en culturas alienígenas que aporta una perspectiva única al equipo Osiris. Su experiencia en interpretación y comunicación con diversas especies alienígenas es esencial para establecer alianzas y comprender las motivaciones de los enemigos en el universo de Halo. Vale es una investigadora curiosa y una experta en inteligencia cultural, lo que la convierte en una activo valioso durante las misiones de reconocimiento y diplomacia. Su capacidad para hablar varios idiomas alienígenas y su profundo conocimiento de las costumbres extraterrestres hacen de Vale una pieza clave en el equipo Osiris, facilitando la colaboración efectiva con aliados y la identificación de puntos débiles en los enemigos.'
    }
    
    personaje = ''
    for key in personajes.keys():
        if user_input.find(key) != -1:
            personaje = key
        
    return personajes[personaje]

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
    historiaHalo = 'En un futuro distante, la humanidad se encuentra en medio de una guerra desesperada contra una alianza alienígena conocida como los Covenant. En medio de este conflicto, emerge un héroe legendario conocido como el Jefe Maestro, un super soldado genéticamente mejorado.'\
        'La historia comienza con el descubrimiento de un anillo artificial gigante llamado Halo, creado por una antigua civilización conocida como los Forerunners. Halo tiene el poder de destruir toda vida en la galaxia y los Covenant están obsesionados con activarlo.'\
        'A lo largo de su viaje, el Jefe Maestro se enfrenta a innumerables desafíos, desde combates épicos contra las fuerzas Covenant hasta la lucha contra los Flood, una forma de vida parasitaria que amenaza con consumir toda la galaxia.'\
        'Acompañado por la inteligencia artificial Cortana, el Jefe Maestro se embarca en una misión para detener a los Covenant, descubrir los secretos de Halo y los Forerunners, y proteger a la humanidad de la extinción.'\
        'La historia de Halo es una epopeya de valor, sacrificio y determinación, que explora temas profundos como la guerra, la moralidad y el destino. A través de sus batallas y triunfos, el Jefe Maestro se convierte en un símbolo de esperanza y resistencia en un universo en guerra'\
    
    return historiaHalo

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

def especies(user_input = '1'):
    covenantInformacion = 'El Covenant es una alianza de razas alienígenas. Está formado por varias especies alienígenas que comparten una religión común y una jerarquía social estricta. Estas son algunas de las razas más destacadas dentro del Covenant:\n'\
                '\t - Sangheili (Elites): Los Elites son una de las especies más prominentes y respetadas dentro del Covenant. Son guerreros hábiles y honorables que sirven como líderes militares y comandantes de las fuerzas Covenant.\n'\
                '\t - Jiralhanae (Brutes): Los Brutes son una especie poderosa y agresiva que sirve como fuerza de choque en el Covenant. A menudo se enfrentan a los Elites en disputas de poder dentro de la jerarquía Covenant.\n'\
                '\t - Kig-Yar (Jackals): Los Jackals son una raza astuta y oportunista que a menudo actúa como francotiradores o piratas dentro del Covenant. Son conocidos por su habilidad con armas de energía.\n'\
                '\t - Unggoy (Grunts): Los Grunts son una raza más débil y menos inteligente que sirve como mano de obra y fuerza de choque en grandes números dentro del Covenant.\n'\
                'Estas son solo algunas de las razas que componen el Covenant, que está unido por la creencia en los "Dioses Antiguos" (los Forerunners) y la búsqueda de tecnología y poder para llevar a cabo su Gran Viaje, que es su interpretación religiosa de activar los anillos Halo para ascender a un estado superior de existencia.'
    
    humanosInformacion = 'Son nativos del planeta Tierra y se han expandido por la galaxia, estableciendo colonias en diferentes planetas y sistemas solares. Los humanos son representados principalmente por la UNSC (United Nations Space Command),'\
                ' una organización militar que lucha para proteger a la humanidad de la amenaza Covenant. La UNSC está equipada con tecnología avanzada, incluidas naves espaciales, armas de alta tecnología y armaduras de combate como la icónica armadura MJOLNIR usada por el Jefe Maestro.'
    
    forerunnersInformacion = 'Los Forerunners eran una especie alienígena avanzada y antigua en el universo. Eran conocidos por su tecnología avanzada, su cultura altamente desarrollada y su capacidad para construir estructuras y artefactos monumentales.'\
                'Los Forerunners evolucionaron en un planeta llamado Ghibalb, ubicado en la galaxia de la Vía Láctea. A lo largo de su historia, desarrollaron una civilización altamente avanzada y próspera. Su tecnologia incluia armas, naves espaciales, '\
                'inteligencias artificiales y estructuras gigantescas como los anillos Halo. Su tecnología era tan avanzada que a menudo se la consideraba mágica por otras razas menos desarrolladas. Los Forerunners mantenían relaciones con otras razas en la galaxia, '\
                'incluidas las humanas, aunque estas relaciones a menudo eran complicadas y tensas debido a las diferencias culturales y tecnológicas.  Una de las mayores hazañas de los Forerunners fue su guerra contra los Flood lucharon desesperadamente, pero finalmente fueron derrotados.'\
                'Como medida desesperada para contener la propagación de los Flood, los Forerunners construyeron los anillos Halo, enormes estructuras con el poder de destruir toda forma de vida en la galaxia. Estos anillos se activaron al final de la guerra contra los Flood, lo que llevó a la extinción de los Forerunners y muchas otras especies.'
    
    floodInformacion = 'El Flood es una forma de vida parasitaria y altamente peligrosa. Son una de las principales amenazas a la vida en la galaxia. Se cree que es el resultado de un organismo parasitario creado por una raza precursora como una herramienta para investigar la vida y la enfermedad. Sin embargo,'\
                ' el Flood eventualmente se salió de control y se convirtió en una plaga galáctica. Este infecta a otras formas de vida, tomando el control de sus cuerpos y convirtiéndolos en formas de combate conocidas como formas de combate. El Flood también tiene formas de infección que pueden propagarse rápidamente y convertir a las víctimas en más Flood.'\
                'El objetivo principal del Flood es consumir toda forma de vida en la galaxia para alimentar su crecimiento y propagación. Son una fuerza destructiva y voraz que no conoce límites en su búsqueda de nuevos huéspedes. Los Forerunners fueron los principales enemigos del Flood, librando una guerra desesperada para contener y detener su propagación.'\
                ' Sin embargo, los Forerunners finalmente fueron derrotados y se vieron obligados a activar los anillos Halo como último recurso para detener al Flood, lo que resultó en la extinción de muchas formas de vida en la galaxia.'
                
    especies = {'humanos': humanosInformacion, 'covenant': covenantInformacion, 'forerunners':forerunnersInformacion, 'flood':floodInformacion, '': 'Perdon he tenido una fallo'}

    if user_input == '1':        
        return " ,".join(str(element) for element in list(especies.keys()))
    else:
        especie = ''
        for key in list(especies.keys()):
            if user_input.find(key) != -1:
                especie = key
                return especies[especie]
        