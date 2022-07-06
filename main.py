import discord
import os
import json
from discord.ext import commands, tasks
from itertools import cycle

TOKEN = 'token'


def prefixChanger(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
    return prefixes[str(message.guild.id)]

client = commands.Bot(command_prefix=prefixChanger, activity=discord.Game(name='Roblox'), case_insensitive=True, help_command=None)

games = cycle(['Minecraft', 'Hytale', 'Half-Life 3', 'Tetris', 'Roblox'])

@client.event
async def on_ready():
    gameschange.start()
    print('I AM LOGGED IN!')
    return


@tasks.loop(seconds=300)
async def gameschange():
    await client.change_presence(activity=discord.Game(next(games)))


# CONECTANDO COGS


def is_it_me(ctx):  # Comandos que só eu posso usar
    return ctx.author.id == 325049357063815176


@client.command()
@commands.check(is_it_me)
async def load(ctx, extension):
    await ctx.send('Cog Loaded')
    client.load_extension(f'c0gs.{extension}')


@client.command()
@commands.check(is_it_me)
async def unload(ctx, extension):
    await ctx.send('Cog Unloaded')
    client.unload_extension(f'c0gs.{extension}')


@client.command()
@commands.check(is_it_me)
async def reload(ctx, extension):
    await ctx.send('Cog Reloaded')
    client.unload_extension(f'c0gs.{extension}')
    client.load_extension(f'c0gs.{extension}')


for filename in os.listdir('./c0gs'):
    if filename.endswith('.py'):
        client.load_extension(f'c0gs.{filename[:-3]}')

client.run(TOKEN)
