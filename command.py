import discord


class BotCommand:
    async def RunCommand(self, channel, command: str):
        await channel.send(f'找到了指令: {command}')
        print(f'Command detected: {command}')
