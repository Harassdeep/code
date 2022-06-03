
import discord
import random

from discord.ext import commands

#Nanda quote
#Nanda ask

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print('bot working')

@client.command()
async def sodiumquote(ctx):






    quotes = [
    '🤣',
    'Bruhhhhhhhh',
    'my sexuality is as straight as siraj\'s whatever',
    'IF FATE PERMITS ME I WILL COME',
    'Yeah he will scream at top of his lungs: You know what f ing thing sodium said....????? \n OH SAD THAT YOUR ENTRAILS ARE ALL STREWN OVER! NOW WHAT SHALL I SAY? RIP!',
    'Anyway am happy that I was able to confuse you',
    'Good bye, my love. The one who stole my heart. The queen of my life, my everything!!!❤️❤️❤️❤️❤️',
    'or we can call him daddy',
    'Saturday is for playing',
    'Isn\'t that marvelous? Shouldn\'t I be praised for such a feat because apparently you guys "hate" girls, so I am not a girl',
    'The feminine part of me has disappeared into thin air',
    'Actually I will not even indulge in your talks. I thought you guys will remove me, so just replied. I would be an inactive bitch',
    'I got it from a porn site (Just Kidding)',
    'You guys won\'t let me sleep. Thanks my love. Love you back as well (i really hope you aren\'t lesbian because then it will look like I am playing with your emotions as I am as straight as Siraj\'s whatever)'



    ]

    await ctx.send(f'{random.choice(quotes)}')
@client.command()
async def sodiumask(ctx, *, question):

    answers = [
    'it is what it is',
    'vote for me Nanda guys 🤣',
    '🤣🤣🤣🤣🤣🤣🤣🤣',
    'if fate permits me i will come',
    'Voice Message',
    'Saturday is for playing',
    'or we can call him daddy',
    'Anyway am happy that I was able to confuse you',
    'The feminine part of me has disappeared into thin air',
    'I got it from a porn site (Just Kidding)',
    'Yeah he will scream at top of his lungs: You know what f ing thing sodium said....????? \n OH SAD THAT YOUR ENTRAILS ARE ALL STREWN OVER! NOW WHAT SHALL I SAY? RIP!'


    ]
    await ctx.send(f'{random.choice(answers)}')



client.run('OTM4NjQzNjQ4MzkwNzcwNzA4.YftSBA.-v-HHs0F_7ddT5JbhczmrSZ1Rgk')
