import discord
import os
import random

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!help'):
      await message.channel.send("Commands:\n**!general** to get a quote from General Iroh \n**!inspire** to get insiprational quotes from General Iroh \n**!element** to get elemental quotes from General Iroh\n**!tea** to get tea quotes from General Iroh  ")
    if message.content.startswith('!element'):
      
      await message.channel.send(random.choice(open('quotes/element.txt').readlines()) + "- Iroh")
    if message.content.startswith('!inspire'):
      
      await message.channel.send(random.choice(open('quotes/inspirational.txt').readlines()) + "- Iroh")
    if message.content.startswith('!general'):
      
      await message.channel.send(random.choice(open('quotes/quotes.txt').readlines()) + "- Iroh")
    if message.content.startswith('!tea'):
      
      await message.channel.send(random.choice(open('quotes/tea.txt').readlines()) + "- Iroh")

client.run(os.getenv('TOKEN'))

