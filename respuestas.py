import discord
import random

def get_response(message:str)->str:
    mensaje = message.lower().strip()
    if mensaje == 'hola':
        return 'Holaaaa'
    if mensaje == 'dado':
        return str(random.randint(1,6))
    if mensaje == 'adios':
        return 'z-u!'
    if mensaje == 'como estas?':
        return 're bien, gracias por preguntar'
    return 'Mejor duérmete otro rato' # respuesta por defecto
