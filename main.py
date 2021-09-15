import discord
import os
import requests
import json
import random

from dotenv import load_dotenv

client = discord.Client()

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable"]

starter_encouragements = [
    "Cheer up!",
    "Hang in there.",
    "You are a great person / bot!"
]


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return quote


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg = message.content

    if msg.startswith('$hello'):
        await message.channel.send('Hello')

    elif msg.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)

    elif msg.startswith('nice'):
        await message.channel.send('to meet you')

    elif any(word in msg for word in sad_words):
        await message.channel.send(random.choice(starter_encouragements))

    elif msg.startswith('good'):
        await message.channel.send('work!')


load_dotenv('Token/Token.env')
client.run(os.getenv('TOKEN'))
