import discord
from discord.ext import commands
import json
import random, os, asyncio

intents = discord.Intents.all()
discord.member = True

client = discord.Client(intents=intents)

with open('setting.json',mode='r',encoding='utf8') as jfile:
    jdata=json.load(jfile)


bot = commands.Bot(command_prefix='&',intents = intents)

@bot.event
async def on_ready():
    print('> Bot is online <')



@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'load {extension} done.')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'unload {extension} done.')

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'reload {extension} done.')


for Filename in os.listdir('./cmds'):
    if Filename.endswith('.py'):
        bot.load_extension(f'cmds.{Filename[:-3]}')

for Filename in os.listdir('./core'):
    if Filename.endswith('.py'):
        bot.load_extension(f'core.{Filename[:-3]}')


if __name__ == "__main__":
    bot.run(jdata['TOKEN'])
