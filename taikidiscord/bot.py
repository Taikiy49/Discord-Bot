from discord.utils import get 
import discord
from discord.ext import commands 
import random
import time

intents=discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix ='!', intents=intents) 

TOKEN = "MTA0OTQ2MzUxODY1MjU1MTMyOQ.GkQiQb.DvX-P42HbfrJn5KrXeljNVlSRHghJcSpfbwRLw" 

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

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

#The below code bans player.
@client.command()
async def ban(ctx, member : discord.Member, *, reason = None):
    if ctx.message.author.guild_permissions.administrator: 
        await member.ban(reason = reason)
        embed = discord.Embed(title="User Banned!",
                              description="**{}** was banned by **{}**!".format(member, ctx.message.author),
                              color=0xff00f6)
        await ctx.send(embed=embed)

    else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff00f6)
        await ctx.send(embed=embed)
        
#The below code unbans player.
@client.command()
async def unban(ctx, member:discord.User, *, reason=None):
    if ctx.message.author.guild_permissions.administrator: 
        await ctx.guild.unban(member, reason=reason)
        embed = discord.Embed(title="User Unbanned!",
                                description="**{}** was unbanned by **{}**!".format(member, ctx.message.author),
                                color=0xff00f6)
        await ctx.send(embed=embed)
        
@client.command()
async def roll(ctx):
     await ctx.send(str(random.randint(1,6)))

@client.command()
async def valorant(ctx):
    await ctx.send("https://tracker.gg/valorant")


client.run(TOKEN) 