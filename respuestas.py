import random

def get_response(message:str)->str:
    mensaje = message.lower().strip()
    if 'hola' in mensaje:
        return 'Holaaaa'
    if mensaje == 'dado':
        return str(random.randint(1,6))
    if mensaje == 'adios' or mensaje == 'chau' or mensaje == 'bye':
        return 'Bai, vuelve pronto!'
    if mensaje == 'como estas?':
        return 'Re bien, gracias por preguntar!'
    if mensaje == 'te necesitare cuando sea necesario por ahora descansa':
        return 'Despiertame cuando me necesites.'
    if mensaje == 'como estas jefe?':
        return 'Necesito un arma.'
    return 'No te entiendo, mejor duérmete otro rato zzZzz' # respuesta por defecto
