import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix = "a!")

@client.event
async def on_ready():
    print(f'BOT SUDAH ONLINE')


@client.command()
async def ping(ctx):
    await ctx.send('Pong !!')

client.run(TOKEN)