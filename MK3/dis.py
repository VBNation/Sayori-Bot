import asyncio
import discord
import requests
import youtube_dl

from chatterbot import ChatBot

TOKEN = 'NDQzNDk0MTc2MTM1NTc3NjMw.DnzM6w.EaLd-H0JW1KjgmJt6tbcSyofv-U'

client = discord.Client()
chatbot = ChatBot(
    'Saya',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)

chatbot.train("chatterbot.corpus.english")


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!saya'):
        new_input = message.content[6:]
        print (new_input)
        response = chatbot.get_response(new_input)
        msg = response
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)