import discord
from utils.dictionary import *


class BotCommand:
    async def run_command(self, message, command: str):
        # await message.channel.send(f'找到了指令: {command}')
        print(f'Command \'{command}\' detected in channel {message.channel.id}')

        permissions = message.author.permissions_in(message.channel)

        command_name = command.split()[0]
        if command_name == 'dict':
            dictionary = Dictionary(message.channel, command)
            if dictionary.status != '0':
                await message.channel.send('出錯：你冇講要查咩單字。用法：$tm dict [要查嘅單字]')
                print(f'Dictionary check was failed with status {dictionary.status}.')
                return
            await message.channel.send(dictionary.check_meaning())

        elif command_name == "mute":
            if not permissions.manage_channels:
                await message.channel.send('你冇執行呢個作業嘅權限，行動已經取消。')
                print(f'An action called by user {message.author.id} in channel {message.channel.id} has been cancelled'
                      f' due to insufficient permission.')
                return

            if len(message.mentions) == 0:
                await message.channel.set_permissions(message.author, send_messages=False)
                await message.channel.send('己經毒啞咗你自己')
                print(f'Muted user {message.author} in channel id {message.channel.id}.')
                return

            for user_to_mute in message.mentions:
                await message.channel.set_permissions(user_to_mute, send_messages=False)
                await message.channel.send(f'己經毒啞咗{user_to_mute.name}')
                print(f'Muted user {user_to_mute.id} in channel id {message.channel.id}.')

        elif command_name == 'unmute':
            if not permissions.manage_channels:
                await message.channel.send('你冇執行呢個作業嘅權限，行動已經取消。')
                print(f'An action called by user {message.author.id} in channel {message.channel.id} has been cancelled'
                      f' due to insufficient permission.')
                return

            for user_to_mute in message.mentions:
                await message.channel.set_permissions(user_to_mute, send_messages=True)
                await message.channel.send(f'被毒啞咗嘅{user_to_mute.name}因為得到{message.author.name}嘅幫助可以講嘢')
                print(f'Unmuted user {user_to_mute.id} in channel id {message.channel.id}.')

        elif command_name == "blind":
            if not permissions.manage_channels:
                await message.channel.send('你冇執行呢個作業嘅權限，行動已經取消。')
                print(f'An action called by user {message.author.id} in channel {message.channel.id} has been cancelled'
                      f' due to insufficient permission.')
                return

            if len(message.mentions) == 0:
                await message.channel.set_permissions(message.author, read_messages=False)
                await message.channel.send('己經插盲咗你自己')
                print(f'Blinded user {message.author} in channel id {message.channel.id}.')
                return

            for user_to_mute in message.mentions:
                await message.channel.set_permissions(user_to_mute, read_messages=False)
                await message.channel.send(f'己經插盲咗{user_to_mute.name}')
                print(f'Blinded user {user_to_mute.id} in channel id {message.channel.id}.')
