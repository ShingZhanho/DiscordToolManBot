import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()


@client.event
async def on_ready():
    print('ToolMan is connected and ready for use.')
    for guild in client.guilds:
        print(f'I am now in guild: {guild.name}({guild.id})')


@client.event
async def on_message(message):
    if message.content.startswith('$tm '):
        await message.channel.send(f'[DEBUG MODE] 我聽到你叫我。指令係：{message.content}。')
        await message.channel.send('DEBUG MODE之下無法執行任何指令。')

client.run(TOKEN)
