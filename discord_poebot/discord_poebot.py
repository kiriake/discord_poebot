import os
import logging
import requests

import discord


logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
client = discord.Client()

@client.event
async def reply(message):
    if message.author == client.user:
        await message.channel.send('Reforges a rare item with new random modifiers. ')

@client.event
async def on_ready():
    logging.info('discord_poebot ready. ')

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.author == client.user:
        logging.info(message)

    if client.user in message.mentions:
        await reply(message)

    if message.content == '/ping':
        await message.channel.send('pong. ')

try:
    client.run(os.environ['DISCORD_TOKEN'])
except KeyError as err:
    logging.error(err)
