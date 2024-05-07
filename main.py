import discord
from tokenDiscord import token

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
voice = discord.VoiceClient

@client.event
async def on_ready():
    print(f'Se a logrado contectar como {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!join'):
        if message.author.voice:
            voice_channel = message.author.voice.channel
            await voice_channel.connect()
        else:
            await message.channel.send("¡Debes estar en un canal de voz para que pueda unirme!")

client.run(token)
