import discord
from discord.ext import commands
import os
import traceback
import asyncio

client = discord.Client()  
token = os.environ['DISCORD_BOT_TOKEN']  

ID_CHANNEL_README = 715182446164836402 # 該当のチャンネルのID  
ID_ROLE_WELCOME = 715183433906782316 # 付けたい役職のID  

@client.event  
async def on_raw_reaction_add(payload):  
    channel = client.get_channel(payload.channel_id)  
    if channel.id == ID_CHANNEL_README:  
        guild = client.get_guild(payload.guild_id)  
        member = guild.get_member(payload.user_id)  
        role = guild.get_role(ID_ROLE_WELCOME)  
        await member.add_roles(role)  
        await channel.send('いらっしゃいませ！')  

client.run(token)  
