from discord.utils import get 
import discord
import os
from discord.ext import commands 
import random
import time

intents=discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix ='!', intents=intents)
bot = commands.Bot(command_prefix='!',intents=intents)


TOKEN = "MTA0OTQ2MzUxODY1MjU1MTMyOQ.GJOVKk.ZCMurWbGigrgbhx6xwhbG8yRZOjoJP-0gnMWi4" 

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.command()
async def hi(ctx):
    if ctx.message.author.id == "384941322831790080":
        await ctx.send({"Hello boss"})
    else:
        await ctx.send("bruh")
    

@client.command()
async def mute(ctx, member: discord.Member):
    if ctx.message.author.guild_permissions.administrator: 
        role = discord.utils.get(ctx.guild.roles, name='Muted') 
        await member.add_roles(role)
        embed = discord.Embed(title="User Muted!",
                              description="**{}** was muted by **{}**!".format(member, ctx.message.author),
                              color=0xff00f6)
        await ctx.send(embed=embed)
        await member.edit(mute=True)
    else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff00f6)
        await ctx.send(embed=embed)

@client.command()
async def ban(ctx, member : discord.Member, *, reason = None):
    if ctx.message.author.guild_permissions.administrator: 
        await member.ban(reason=reason)
        embed = discord.Embed(title="User Banned!",
                              description="**{}** was banned by **{}**!".format(member, ctx.message.author),
                              color=0xff00f6)
        await ctx.send(embed=embed)
    else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff00f6)
        await ctx.send(embed=embed)
        
@client.command()
async def unban(ctx, member:discord.User, *, reason=None):
    if ctx.message.author.guild_permissions.administrator: 
        await ctx.guild.unban(member, reason=reason)
        embed = discord.Embed(title="User Unbanned!",
                                description="**{}** was unbanned by **{}**!".format(member, ctx.message.author),
                                color=0xff00f6)
        await ctx.send(embed=embed)
    else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff00f6)
        await ctx.send(embed=embed)

@client.command(description="Kicks a member from the server...")
async def kick(ctx, member: discord.Member, *, reason=None):
    if ctx.message.author.guild_permissions.administrator: 
        try:
            if ctx.author.guild_permissions.kick_members:
                await member.kick(reason=reason)
                embed = discord.Embed(title="User Kicked!",
                                description="**{}** was kicked by **{}**!".format(member, ctx.message.author),
                                color=0xff00f6)
                await ctx.send(embed=embed)
        except:
            embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff00f6)
            await ctx.send(embed=embed)
#ROLL
@client.command()
async def roll(ctx):
     await ctx.send(str(random.randint(1,6)))

#TROLL COMMANDS
@client.command()
async def valorant(ctx):
    await ctx.send("https://tracker.gg/valorant")

@client.command()
async def youtube(ctx):
    await ctx.send("https://www.youtube.com")

@client.command()
async def twitch(ctx):
    await ctx.send("https://www.twitch.tv")

@client.command()
async def harvey(ctx):
    await ctx.send("https://www.twitch.tv/sniper_beast27")

@client.command()
async def whipquan(ctx):
    await ctx.send("https://steamcommunity.com/profiles/76561199020431662/inventory/")

@client.command()
async def evan(ctx):
    await ctx.send("https://www.instagram.com/evan_uyem/")
    
@client.command()
async def eric(ctx):
    await ctx.send("https://www.instagram.com/superstaric04/")

#CALCULATOR
@client.command()
async def calc(ctx):
    def check(m):
        return len(m.content) >= 1 and m.author != client.user

    await ctx.send("Number 1: ")
    number_1 = await client.wait_for("message", check=check)
    await ctx.send("Operator: ")
    operator = await client.wait_for("message", check=check)
    await ctx.send("number 2: ")
    number_2 = await client.wait_for("message", check=check)
    try:
        number_1 = float(number_1.content)
        operator = operator.content
        number_2 = float(number_2.content)
    except:
        await ctx.send("invalid input")
        return
    output = None 
    if operator == "+":
        output = number_1 + number_2
    elif operator == "-":
        output = number_1 - number_2
    elif operator == "/":
        output = number_1 / number_2
    elif operator == "*":
        output = number_1 * number_2
    else:
        await ctx.send("invalid input")
        return
    await ctx.send("Answer: " + str(output))

@client.command(name='join', help='Tells the bot to join the voice channel')
async def join(ctx):
    if not ctx.message.author.voice:
        await ctx.send("{} is not connected to a voice channel".format(ctx.message.author.name))
        return
    else:
        channel = ctx.message.author.voice.channel
    await channel.connect()
@client.command(name='leave', help='To make the bot leave the voice channel')
async def leave(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_connected():
        await voice_client.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")

client.run(TOKEN) 
