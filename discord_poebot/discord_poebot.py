import os
import logging
import requests
import discord


logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
TOKEN = os.environ['DISCORD_TOKEN']


class Discord_poebot(discord.Client):


    # @client.event
    async def on_ready(self):
        logging.info('discord_poebot ready. ')

    # @client.event
    async def reply(self, message):
        if message.author == self.user:
            reply = '{message.author.mention} Reforges a rare item with new random modifiers. '
            await message.channel.send(reply)

    # @client.event
    async def on_message(self, message):
        if message.author.bot or message.channel.id != 810816487044546591:
            return

        if message.author == self.user:
            logging.info(message)

        if self.user in message.mentions:
            await self.reply(message)

        if message.content == '/ping':
            await message.channel.send('pong. ')

client = Discord_poebot()
try:
    client.run(TOKEN)
except KeyError as err:
    logging.error(err)

