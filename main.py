import discord
import requests
import pyttsx3 as pyt
from discord.ext import commands

engine = pyt.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

for index, voice in enumerate(voices):
    print(f"Índice: {index} | Nome: {voice.name} | ID: {voice.id}")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)


@bot.command()

bot.run("TOKEN")
