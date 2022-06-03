import discord
#from discord.ext import commands

#import random

from discord.ext import commands

#Nanda quote
#Nanda ask

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print('bot working')

@client.command()
##async def thankyou(ctx):
async def thankyou(ctx, user1: discord.Member):
    for i in range(24):
        await ctx.send(f'{user1.mention} Happy Birthday')
#await ctx.send("smd")

#@client.command()
#async def e(ctx):
#    UnwantedProtists = get(ctx.guild.members, name='UnwantedProtists')
#    await ctx.send(f"{UnwantedProtists.mention}")


client.run('[discord_token]')
