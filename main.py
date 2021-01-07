import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from discord import User
from discord.ext.commands import Bot, guild_only

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='cou!')

@bot.command(name='p')
async def p(ctx, num1,num2):
    response = int(num1)+int(num2)
    await ctx.send(response)

@bot.command(name='m')
async def m(ctx, num1,num2):
    response = int(num1)*int(num2)
    await ctx.send(response)

@bot.command(name='ban')
async def ban(ctx, member : discord.Member, reason=None):
    """Bans a user"""
    if reason == None:
        await ctx.send(f"Chu... {ctx.author.mention}, Chu make swure to provide reason!")
    else:
        messageok = f"Cou! chu have been bwanned in {ctx.guild.name} for {reason}"
        await member.send(messageok)
        await member.ban(reason=messageok)

        @bot.command(name='unban')
        @guild_only()  # Might not need ()
        async def _unban(ctx, id: int):
            user = await bot.fetch_user(id)
            await ctx.guild.unban(user)

bot.run(TOKEN)