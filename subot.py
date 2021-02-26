import os
import random
import discord
from dotenv import load_dotenv #not that important if you are running a baby bot
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN') 
#set up .env file with DISCORD_TOKEN = bot_token

#names are store in a file and load
subek_names = set()
f = open("names.txt","r")
for name in f:
    subek_names.add(name)
f.close()

subek_names=list(subek_names)

 
bot = commands.Bot(command_prefix='!')



@bot.command(name='bek',help='Responds with a random subek nickname')
async def bek_command(ctx):
    response = "Call bek for a random subek nickname"
    await ctx.send(response)

#tutorial code you can ignore
@bot.event
async def on_ready():
    #print all server/guild bot is connected to
    for guild in bot.guilds:
        print(
            f'{bot.user.name} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
        )
        #members list
        '''members = '\n - '.join([member.name for member in guild.members])
        print(f'Guild Members:\n - {members}')'''


@bot.event
async def on_message(message):
    #process commands first
    await bot.process_commands(message)
    #check if this bot made the message (no recursive calls) 
    if message.author == bot.user:
        return 1

    if message.content.lower() == 'bek':
        response = random.choice(subek_names)
        await message.channel.send(response)

bot.run(TOKEN)