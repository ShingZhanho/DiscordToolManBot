import os
from command import BotCommand

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
    if message.content.startswith('$tm'):
        if len(message.content) == 3:  # if no command found
            await message.channel.send('只找到呼叫開頭而沒有具體指令。用法：$tm [具體指令]')
            return

        command = BotCommand()
        await command.RunCommand(message.channel, message.content[4:])

client.run(TOKEN)
