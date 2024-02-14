import discord
import respuestas

# message es un json que contiene el mensaje que el usuario envió y sus datos
async def send_message(message, user_message, is_private):
    response = respuestas.get_response(user_message)
    await message.author.send(response) if is_private else await message.channel.send(response)


def run_discordBot():
    TOKEN = open('TOKEN.txt').read().strip()
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    # definimos un evento para el cliente de discord
    # esta función sirve para saber que el bot se concectó a discord
    # client.user es el bot
    @client.event
    async def on_ready():
        print(f'{client.user} ha salido del infierno')
    
    @client.event 
    async def on_message(message):
        # revisa si el autor del mensaje no es el bot, si lo es, no hace nada
        if message.author == client.user:
            return
        username = str(message.author)
        user_message=str(message.content)
        channel = str(message.channel)

        print(f'{username} en {channel} dijo: {user_message}')

        if user_message[0:3] == 'uwu': 
            user_message = user_message[3:]
            # Cambiar a false para que responda en el canal donde se mandó el mensaje
            await send_message(message, user_message, is_private=False)
        else:
            await send_message(message, user_message, is_private=False)


    client.run(TOKEN)