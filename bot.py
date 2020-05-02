import discord

cliente_discord = discord.Client()
channel = cliente_discord.get_guild('Your_Server_ID')  # Do not use strings in this, use the value in INT type


@cliente_discord.event
async def on_ready():
    print('We have logged in as {0.user}'.format(cliente_discord))  # Message im terminal to confirm the start


@cliente_discord.event
async def on_message(text):

    if text.author.id == 'Your_Client_ID':  # To avoid loops
        return

    # Example of a text message
    if text.content.startswith('!lauren'):
        await text.channel.send('Irá ter jogadas ou gameplays de jogo FPS ou CORRIDA(pois são os que eu mais jogo'
                                'Não quero ser Youtuber(mais talvez eu consiga então YEAHH)')
        return

    # Example of a image message
    elif text.content.startswith('!jhonny'):
        await text.channel.send(file=discord.File('img/photo.jpg'))

        return


cliente_discord.run('Your_Discord_Bot_Token')
