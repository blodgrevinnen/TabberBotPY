import discord
import json
import os
import random
import time
import requests
import youtube_dl
from discord.ext import commands
import asyncio
from itertools import cycle

TOKEN = 'enter token'
client = commands.Bot(command_prefix = 't?')
client.remove_command('help')

extensions = ['fun', 'moderation']

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='t?help'))
    print('Bot online.')

#Cog commands.

@client.command()
async def load(extension):
    try:
        client.load_extension(extension)
        print('Loaded {}'.format(extension))
    except Exception as error:
        print('{} cannot be loaded.[{}]'.format(extension, error))

@client.command()
async def unload(extension):
    try:
        client.unload_extension(extension)
        print('Unloaded {}'.format(extension))
    except Exception as error:
        print('{} cannot be unloaded.[{}]'.format(extension, error))

@client.command()
async def cogs():
    embed = discord.Embed(
        title = 'Available Cogs',
        description = 'The available cogs are:',
        color = discord.Color.magenta()
    )

    embed.set_footer(text='Use these with t?load (name).')
    embed.set_thumbnail(url='https://image.flaticon.com/icons/png/512/28/28353.png')
    embed.add_field(name='Fun: ', value='Bot commands that are created for entertainment.', inline=True)
    embed.add_field(name='Moderation: ', value='Bot commands that are use to carry out moderation automatically.', inline=True)

    await client.say(embed=embed)

#Main commands that cannot be disabled by unloading a cog, they are part of the main bot.

@client.command()
async def ping():
    t1 = time.perf_counter()
    msg = await client.say("`Ping successful. 000 ms`")
    t2 = time.perf_counter()
    await client.edit_message(msg, '`Ping successful. {} ms`'.format(round((t2-t1)*1000)))

@client.command()
async def info():
    embed = discord.Embed(
        title = 'Info',
        description = 'This is a work-in-progress discord bot with commands that are being refined every day. This bot comes equipped with moderation, music, and fun commands.',
        color = discord.Color.magenta()
    )

    embed.set_footer(text='Easter egg -Tanner.')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/484183506503860224/490984528832364554/tabberlogo.png')
    embed.add_field(name='Language: ', value='Python 3.6', inline=True)
    embed.add_field(name='Program: ', value='Visual Studio Code', inline=True)
    embed.add_field(name='Creator: ', value='TANNER#7777', inline=True)
    embed.add_field(name='Discord.py Version', value='discord.py v0.16.12', inline=True)

    await client.say(embed=embed)

#Rules command.
@client.command(pass_context=True)
async def rules(ctx):
    if ctx.message.author.server_permissions.manage_server: #Checks if the user has permission to manage manage the server.
        embed = discord.Embed(title='--Rules--', color = discord.Colour.magenta(), inline=False)

        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/484183506503860224/490984528832364554/tabberlogo.png')
        embed.add_field(name='Rule 1:', value='Spamming of any sort will result in an instant warn and 10 minute mute. This includes emojis.', inline=False)
        embed.add_field(name='Rule 2:', value='No advertising of any sort. Includes self-promotion. Doing so will result in an instant ban.', inline=False)
        embed.add_field(name='Rule 3:', value='NSFW, shady sites, and racism will not be tolerated. This will result in an instant ban. NO EXCEPTIONS.', inline=False)
        embed.add_field(name='Rule 4:', value='Keep the contents relevant. Post pictures in #screenshots and use #looking-for-group for finding a game and trading. (Trading is not our responsibility, we will not replace lost items.)', inline=False)
        embed.add_field(name='Rule 5:', value='Be a decent person, be nice and if someone is breaking the rules, put them in the #report-user chat and the staff will get to it as soon as they see it.', inline=False)
        embed.add_field(name='Rule 6:', value='Do not ping moderators without a legitimate reason, doing so will result in a warn.', inline=False)
        embed.add_field(name='Rule 7:', value='If your name is unmentionable, please change it. Make atleast the first three characters able to be typed on an english keyboard.', inline=False)
        embed.add_field(name='Rule 8:', value="Don't ask for roles in the server, if you are active you will earn them eventually, you have to be patient.", inline=False)
        embed.add_field(name='Rule 9:', value='Earrape in the voice chats are strictly prohibited, you will lose the privilige to connect and speak if you do so.', inline=False)
        embed.add_field(name='Rule 10:', value='If you are arguing with another user, keep it PG and cool. If it gets heated, you will both be muted for thirty minutes', inline=False)
        embed.add_field(name='Rule 11:', value='Keep yourself updated in case there are new rules or announcements to the server.', inline=False)
        embed.add_field(name='Rule 12:', value='Do not discuss illegal activities, if you do so, you will be banned from the server immediately.', inline=False)
        embed.add_field(name='Rule 13:', value='This server is mainly english, other languages are allowed, but keep them to a minimum if possible', inline=False)
        embed.add_field(name='Rule 14:', value='If you wish to post a link, use #links and not #general . If you wish to post a link in general, ask a moderators permission', inline=False)
        embed.add_field(name='Rule 15:', value='If you have commands that you wish I should add, put them in #suggestions . My creator will consider it and will get to it ASAP!', inline=False)
        embed.add_field(name='Rule 16:', value="If you made it this far, i'd personally like to thank you for reading the rules. Have Fun and stay safe!", inline=False)
        await client.say(embed=embed)

    else:
        await client.say("`You do not have permission to use this command.`")

#Punishment command.
@client.command(pass_context=True)
async def punishment(ctx):
    if ctx.message.author.server_permissions.manage_server: #Checks if the user has permission to manage manage the server.
        embed = discord.Embed(title='--Punishment--', color = discord.Colour.magenta(), inline=False)

        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/484183506503860224/490984528832364554/tabberlogo.png')
        embed.add_field(name='1)', value='First warning.', inline=False)
        embed.add_field(name='2)', value='Second warning.', inline=False)
        embed.add_field(name='3)', value='Kick.', inline=False)
        embed.add_field(name='4)', value='Ban.', inline=False)
        embed.add_field(name='--Muting Levels--', value='The moderators will decide how long it should be, I condone whatever they think is necessary so do not get mad.', inline=False)
        await client.say(embed=embed)

    else:
        await client.say("`You do not have permission to use this command.`")

#Bot logo command.
@client.command(pass_context=True)
async def botlogo(ctx):
    embed = discord.Embed(color = discord.Color.magenta())

    embed.set_image(url='https://cdn.discordapp.com/attachments/484183506503860224/490984528832364554/tabberlogo.png')

    await client.say(embed=embed)

#Help command that replaces the default one.

@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    embed1 = discord.Embed(title='--Main--', description='--Commands that cannot be disabled.--', color = discord.Colour.magenta(), inline=False)

    embed1.set_author(name='All commands for this bot. Includes main commands and all the cog commands.')
    embed1.add_field(name='t?load', value='Loads the cog that the user requested. STAFF ONLY', inline=False)
    embed1.add_field(name='t?unload', value='Unloads the cog that the user requested. STAFF ONLY', inline=False)
    embed1.add_field(name='t?cogs', value='Lists all the available cogs that can be loaded/unloaded.', inline=False)
    embed1.add_field(name='t?ping', value='Returns "Ping successful () ms', inline=False)
    embed1.add_field(name='t?info', value="Sends the bot's info into the channel in which the command took place.", inline=False)
    embed1.add_field(name='t?rules', value="Sends a list of rules in an embed. Server manager required.", inline=False)
    embed1.add_field(name='t?punishment', value="Sends a list of punishment in an embed. Goes along with rules. Server manager required.", inline=False)
    embed1.add_field(name='t?botlogo', value= "Sends the bot's logo", inline=False)
    await client.send_message(author, embed=embed1)
    embed2 = discord.Embed(title ='--Fun--', description='--Commands in the Fun Cog.--', color = discord.Colour.magenta(),  inline=False)
    embed2.add_field(name='t?8ball', value='Ask the magic 8ball any question you like! It will magically answer using...MAGIC!!', inline=False)
    embed2.add_field(name='t?square', value='Square any number you would like!', inline=False)
    embed2.add_field(name='t?bitcoin', value='Retrieve the current Bitcoin value.', inline=False)
    embed2.add_field(name='t?yourmomgay', value='Tell the bot a nasty remark and get an even nastier one in return!', inline=False)
    embed2.add_field(name='t?namestory', value='Hear the story about how this bot got its name. Trust me, its a good one', inline=False)
    embed2.add_field(name='t?wtf', value="Send a picture of a nice response to something you don't understand.", inline=False)
    embed2.add_field(name='t?frenchwtf', value="Send a picture of a nice response to something you don't understand... IN FRENCH!!", inline=False)
    embed2.add_field(name='t?wave', value="Sends a gif of Grampa Simpson waving.")
    await client.send_message(author, embed=embed2)
    embed3 = discord.Embed(title='--Moderation--', description='--Commands in the Moderation cog.--', color = discord.Color.magenta(),  inline=False)
    embed3.add_field(name='t?ban', value='Bans the selected member.', inline=False)
    embed3.add_field(name='t?kick', value='Kicks the selected member.', inline=False)
    embed3.add_field(name='t?mute', value='Mutes the selected member.', inline=False)
    embed3.add_field(name='t?unmute', value='Unmutes a muted member.', inline=False)
    embed3.add_field(name='t?clear', value='Deletes the amount of text requested.', inline=False)
    embed3.add_field(name='t?nick', value='Changes the nickname of the selected member', inline=False)
    await client.send_message(author, embed=embed3)

if __name__ == '__main__':
    for extension in extensions:
        try:
            client.load_extension(extension)
        except Exception as error:
            print('{} cannot be loaded. [{}]'.format(extension, error))

    client.run(TOKEN)