from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

@client.event
async def on_message(message):
    x = message.content
    if message.author.bot:
        return
    if "/ping" == x:
        await message.channel.send("pong")
    if message.content == "OP":
        await message.channel.send("YEEEEEEEEEEEE")  
    
bot.run(token)
