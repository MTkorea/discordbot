import discord
import asyncio
import random
import time
import datetime
import os

client = discord.Client()

@client.event
async def on_ready():
    print("ready")
    print(client.user.id)
    print(client.user.name)
    print('=====================================')
    
@client.event
async def on_message(message):
    if message.content.startswith('!공지'):
            for i in message.guild.members:
                if i.bot == True:
                    pass
                else:
                    try:
                        msg = message.content[4:]
                        if message.author.id == 560330444428673026:
                            embed=discord.Embed(colour=0xFF0000, timestamp=message.created_at, title="초고퀄 최저가 프사샵")
                            embed.add_field(name="전체공지", value=msg, inline=True)
                            embed.set_footer(text=f"부담없이 문의주세용!")
                            await i.send(embed=embed)
                    except:
                        pass
            
    if message.content.startswith("!삭제"):
        await message.channel.purge(limit=100)
        await message.channel.send('메세지 100개 가삭제되었습니다.')
        await message.channel.purge(limit=1)

    if message.content.startswith("!내정보"):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(color=0xFF0000)
        embed.add_field(name="닉네임", value=message.author.name, inline=True)
        embed.add_field(name="서버 닉네임", value=message.author.display_name, inline=True)
        embed.add_field(name="디스코드가입일", value=str(date.year) + "/" + str(date.month) + "/" + str(date.day), inline=True)
        embed.add_field(name="디스코드주소: discord.gg/t5tZUUg", value=message.author.name + "님 반가워요!", inline=True)
        embed.set_thumbnail(url=message.author.avatar_url)
        await message.channel.send(embed=embed)      

    if message.content == '!배너문의':
            embed=discord.Embed(title='배너문의', color=0x64FE2E, timestamp=message.created_at)
            embed.add_field(name="배너문의", value=f'OOOP!#2036', inline=True)
            embed.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            await message.channel.send(embed=embed)
            
    if message.content == '!디스코드':
            embed=discord.Embed(title='Discord', color=0xFF00FF, timestamp=message.created_at)
            embed.add_field(name="디스코드 주소", value=f'https://discord.gg/t5tZUUg', inline=True)
            embed.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            await message.channel.send(embed=embed)              
        
async def my_background_task():
    await client.wait_until_ready()
    while not client.is_closed():
        game = discord.Game("!배너문의")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(2)
        game = discord.Game("초고퀄프사 제작중")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(2)
        game = discord.Game(f'{len(client.guilds)}개의 서버에 참여중')
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(2)
        game = discord.Game(f'{len(client.users)}명의 유저들과 소통하는중')
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(2)

access_token = os.environ["BOT_TOKEN"]
        
client.loop.create_task(my_background_task())

client.run(access_token)
