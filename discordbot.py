from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
    
@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)
    
@client.event
async def on_message(message):
    if message.auther.bot:
        return
    if message.content.startswith("OP"):
        await message.channel.send('YEEEEEEEEEE!!')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
bot.run(token)
