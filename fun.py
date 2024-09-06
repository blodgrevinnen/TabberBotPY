import discord
import random
import requests
from discord.ext import commands
import asyncio
from itertools import cycle

class Fun:
    def __init__(self, bot):
        self.bot = bot
#8ball command
    @commands.command(name='8ball', pass_context=True)
    async def eight_ball(self, ctx):
        possible_responses = [
            'It is certain. :8ball: ',
            'It is decidedly so. :8ball: ',
            'Without a doubt. :8ball: ',
            'Yes - definitely. :8ball: ',
            'You may rely on it. :8ball: ',
            'As I see it, yes. :8ball: ',
            'Most likely. :8ball: ',
            'Outlook good. :8ball: ',
            'Yes. :8ball: ',
            'Signs point to yes. :8ball: ',
            'Reply hazy, try again. :8ball: ',
            'Ask again later. :8ball: ',
            'Better not tell you now. :8ball: ',
            'Cannot predict now. :8ball: ',
            'Concentrate and ask again. :8ball: ',
            "Don't count on it. :8ball: ",
            'My reply is no. :8ball: ',
            'My sources say no. :8ball: ',
            'Outlook not so good. :8ball: ',
            'Very doubtful. :8ball: ',
        ]
        await self.bot.say(random.choice(possible_responses) + ", " + ctx.message.author.mention)
#square command
    @commands.command(pass_context=True)
    async def square(self, ctx, number):
        squared_value = int(number) * int(number)
        await self.bot.say(str(number) + " squared is " + str(squared_value) + ".")
#bitcoin command
    @commands.command()
    async def bitcoin(self):
        url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
        response = requests.get(url)
        value = response.json() ['bpi'] ['USD'] ['rate']
        await self.bot.say("Bitcoin price is : $" + value + " :money_mouth: ~~Your investment was worth it...~~ ")

#yourmomgay command
    @commands.command(pass_context=True)
    async def yourmomgay(self, ctx):
        possible_responses = [
            'No U'
        ]
        await self.bot.say(random.choice(possible_responses) + ", " + ctx.message.author.mention)
#namestory command
    @commands.command(pass_context=True)
    async def namestory(self, ctx):
        possible_responses = [
            "Tabber comes from an ancient tale long long ago... A man by the name of Rick... Uncle Rick... once had a phone. Now don't be getting yourself underwhelmed because this phone was not ordinary.. it had.. ***AUTOCORRECT*** . Now you may be thinking: What is so special about autocorrect? Well the thing is, this autocorrect didn't know names. The creator of this bot's name is Tanner. Rick's phone was so stupid that it autocorrected to 'Tabber'. That is the story about how the bot got its name. The End."
        ]
        await self.bot.say(random.choice(possible_responses) + ", " + ctx.message.author.mention)
#excuse me wtf command
    @commands.command()
    async def wtf(self):
        embed = discord.Embed(
            color = discord.Color.magenta()
        )

        embed.set_image(url='https://orig00.deviantart.net/81ca/f/2018/199/4/7/excuse_me_what_the_fuck_by_twentytwoeyes-dchnaf5.jpg')

        await self.bot.say(embed=embed)
#excuse me wtf command in french
    @commands.command()
    async def frenchwtf(self):
        embed = discord.Embed(
            color = discord.Color.magenta()
        )

        embed.set_image(url='https://cdn.discordapp.com/attachments/468759629334183956/486332454119014401/55anelv9u5j11.png')

        await self.bot.say(embed=embed)

    @commands.command(pass_context=True)
    async def wave(self, ctx):
        embed = discord.Embed(
            color = discord.Color.magenta()
        )

        embed.set_image(url='https://cdn.discordapp.com/attachments/486151487509233665/487024860233465856/IDu.gif')

        await self.bot.say(embed=embed)
        await self.bot.say( "Hello, " + ctx.message.author.mention)

def setup(client):
    client.add_cog(Fun(client))
