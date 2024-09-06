import discord
import random
import time
import requests
import youtube_dl
from discord.ext import commands
import asyncio
from itertools import cycle

class Moderation:
    def __init__(self, bot):
        self.bot = bot
        
#Purges a specified amount of messages.
    @commands.command(pass_context=True)
    async def clear(self, ctx, amount):
        if ctx.message.author.server_permissions.manage_messages: #Checks if the user can manage messages.
            channel = ctx.message.channel
            messages = []
            async for message in self.bot.logs_from(channel, limit=int(amount)+1):
                messages.append(message)
            await self.bot.delete_messages(messages)
        else:
            await self.bot.say("`You do not have permission to use this command.`")

#Bans the selected member.
    @commands.command(pass_context=True)
    async def ban(self, ctx, user: discord.Member, *, reason=None):
        if ctx.message.author.server_permissions.ban_members: #Checks if the user has permission to ban the user.
            if reason == None:
                embed = discord.Embed(color = discord.Color.magenta())
                embed.set_author(name='{} Has been banned'.format(user.name))
                embed.add_field(name='Reasoning', value='{}'.format(reason), inline=True)
                embed.set_thumbnail(url=user.avatar_url)
                await self.bot.say(embed=embed)
                await self.bot.ban(user)
        else:
            await self.bot.say("`You do not have permission to use this command.`")

#Kicks the selected member.
    @commands.command(pass_context=True)
    async def kick(self, ctx, user: discord.Member, *, reason=None):
        if ctx.message.author.server_permissions.kick_members: #Checks if the user has permission to kick the user.
            if reason == None:
                embed = discord.Embed(color = discord.Color.magenta())
                embed.set_author(name='{} Has been kicked.'.format(user.name))
                embed.add_field(name='Reasoning', value='{0}'.format(reason), inline=True)
                embed.set_thumbnail(url=user.avatar_url)
                await self.bot.say(embed=embed)
                await self.bot.kick(user)
        else:
            await self.bot.say("`You do not have permission to use this command.`")
#Mutes the selected member.
    @commands.command(pass_context=True) 
    async def mute(self, ctx, user: discord.Member, *, reason=None):
        if ctx.message.author.server_permissions.mute_members: #Checks if the user has permission to mute members.
            MutedRole = discord.utils.get(ctx.message.server.roles, name='Muted')
            if reason == None:
                embed = discord.Embed(colour = discord.Colour.magenta())
                embed.set_author(name='{} Has been muted'.format(user.name))
                embed.add_field(name='Reasoning', value='{0}'.format(reason), inline=True)
                await self.bot.say(embed=embed)
                await self.bot.add_roles(user, MutedRole)
        else:
            await self.bot.say('`You do not have permission to use this command.`')
#Unmutes the selected member.
    @commands.command(pass_context=True)
    async def unmute(self, ctx, user: discord.Member, *, reason=None):
        if ctx.message.author.server_permissions.mute_members: #Checks if the user has permission to mute members.
            MutedRole = discord.utils.get(ctx.message.server.roles, name='Muted')
            if reason == None:
                embed = discord.Embed(colour = discord.Colour.magenta())
                embed.set_author(name='{} Has been unmuted'.format(user.name))
                await self.bot.say(embed=embed)
                await self.bot.remove_roles(user, MutedRole)
        else:
            await self.bot.say('`You do not have permission to use this command.`')

#Changes the nickname of the selected user.
    @commands.command(pass_context=True)
    async def nick(self, ctx, user: discord.Member, *, nickname=None):
        if ctx.message.author.server_permissions.manage_nicknames: #Checks if the user has permission to manage nicknames.
            await self.bot.change_nickname(user, nickname)
        else:
            await self.bot.say("`You do not have permission to use this command.`")

def setup(client):
    client.add_cog(Moderation(client))
