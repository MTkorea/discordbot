import discord
import asyncio
import datetime
import os

client = discord.Client()

channelsRunning = []
pollYes = 0
pollNo = 0
voted = {}
client = discord.Client()
realPoll = None
pollTitle = ''

async def update_poll(realPoll, pollTitle, pollNo, pollYes):
    await client.edit_message(realPoll, """
                ```css
                [투표] %s
                [YES : %s ]  [NO : %s ]
                예'를 투표하려면 '$y'를 입력하고, '아니오' 를 투표하려면 '$n' 을 입력하세요.
                ```""" % (str(pollTitle), str(pollYes), str(pollNo)))

@client.event
async def on_ready():
    print("ready")
    print(client.user.id)
    print(client.user.name)
    print('=====================================')
    
    
@client.event
async def on_message(message):
    global pollRunning, pollNo, pollYes, realPoll, pollTitle, voted

    if message.content.startswith("+서버리스트"):
        list = []
        for server in client.servers:
            list.append(server.name)
        await  client.send_message(message.channel, "\n".join(list))

    if message.content.startswith("+투표"):
        if (message.channel not in channelsRunning):
            voted[message.channel] = []
            channelsRunning.append(message.channel)
            pollTitle = message.content[5:]
            pollYes = 0
            pollNo = 0
            realPoll = await client.send_message(message.channel, """
            ```css
            [투표] %s
            [YES : %s ]  [NO : %s ]
            '예'를 투표하려면 '$y'를 입력하고, '아니오' 를 투표하려면 '$n' 을 입력하세요.
            ```
            """ % (str(pollTitle), str(pollYes), str(pollNo)))
            await asyncio.sleep(300.0)
            channelsRunning.remove(message.channel)
            if (pollYes > pollNo):
                await client.send_message(message.channel,
                                          "과반수 (%s %s) 가 '그렇다'고 응답했다: %s." % (
                                          str((pollYes / (pollYes + pollNo)) * 100), "%", str(pollTitle)))
            elif (pollYes < pollNo):
                await client.send_message(message.channel,
                                          "과반수 (%s %s) 가 '아니오'라고 응답했다: %s." % (
                                          str((pollNo / (pollYes + pollNo)) * 100), "%", str(pollTitle)))
            else:
                await client.send_message(message.channel, "투표, " + str(pollTitle) + ", 동점으로 끝났다")

        else:
            await client.send_message(message.channel,
                                      "{0.author.mention} 새 투표가 시작될 때까지 기다리십시오.".format(
                                          message))
    # User Vote No
    if (message.content.startswith("$n") or message.content.startswith("$N")):
        if (message.channel in channelsRunning):
            author = "{0.author.mention}".format(message)
            if not author in voted[message.channel]:
                voted[message.channel].append(author)
                pollNo += 1
                await update_poll(realPoll, pollTitle, pollNo, pollYes)
            else:
                await client.send_message(message.channel, "{0.author.mention} 이미 투표하셨잖아요.".format(message))
    # User Vote Yes
    if (message.content.startswith("$y") or message.content.startswith("$Y")):
        if (message.channel in channelsRunning):
            author = "{0.author.mention}".format(message)
            if not author in voted[message.channel]:
                voted[message.channel].append(author)
                pollYes += 1
                await update_poll(realPoll, pollTitle, pollNo, pollYes)
            else:
                await client.send_message(message.channel, "{0.author.mention} 이미 투표하셨잖아요.".format(message))
    
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
