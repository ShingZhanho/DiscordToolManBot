import discord
from utils.dictionary import *


class BotCommand:
    async def run_command(self, channel, command: str):
        await channel.send(f'找到了指令: {command}')

        command_name = command.split()[0]
        if command_name == 'dict':
            dictionary = Dictionary(command.split(' ', 1)[1])
            await channel.send(dictionary.check_meaning())

        print(f'Command \'{command}\' detected in channel {channel.id}')
