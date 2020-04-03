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

    if message.content.startswith("+help"):
        channel = message.channel
        embed = discord.Embed(
            title = '[명령어 목록]',
            description = '냥냥봇의 기본적인 명령어들 입니다.',
            colour = discord.Colour.blue()
        )

        #embed.set_footer(text = '끗')
        dtime = datetime.datetime.now()
        #print(dtime[0:4]) # 년도
        #print(dtime[5:7]) #월
        #print(dtime[8:11])#일
        #print(dtime[11:13])#시
        #print(dtime[14:16])#분
        #print(dtime[17:19])#초
        embed.set_footer(text=str(dtime.year)+"년 "+str(dtime.month)+"월 "+str(dtime.day)+"일 "+str(dtime.hour)+"시 "+str(dtime.minute)+"분 "+str(dtime.second)+"초")
        #embed.set_footer(text=dtime[0:4]+"년 "+dtime[5:7]+"월 "+dtime[8:11]+"일 "+dtime[11:13]+"시 "+dtime[14:16]+"분 "+dtime[17:19]+"초")
        embed.add_field(name='+개발자정보', value='개발자정보를 출력합니다.',inline = False)
        embed.add_field(name='+후원', value='봇 개발자에게 후원합니다.(서버 호스팅비용)',inline = False)                
        embed.add_field(name='+현재시각', value='현재시각을 확인합니다.', inline=False)
        embed.add_field(name='+핑', value='자신의 핑을 체크합니다.', inline=False)
        embed.add_field(name='+현재시각', value='현재시각을 출력합니다.', inline=False)
        embed.add_field(name='+날씨 <지역>', value='특정지역의 날씨를 출력합니다.', inline=False)
        embed.add_field(name='+영화순위', value='영화순위를 출력합니다.', inline=False)
        embed.add_field(name='+이미지 <검색할이미지>', value='검색한 이미지를 출력합니다.', inline=False)
        embed.add_field(name='+실시간검색어', value='네이버 실시간검색어를 확인합니다.', inline=False)
        embed.add_field(name='+실검', value='네이버 실시간검색어를 확인합니다.', inline=False)
        embed.add_field(name='+주사위', value='주사위를 던집니다.', inline=False)
        embed.add_field(name='+타이머 <숫자>', value='시간을 출력합니다 __대도록이면 10초 안으로 해주세요.__', inline=False)
        embed.add_field(name='+제비뽑기 <숫자>', value='제비뽑기를 시작합니다.', inline=False)
        embed.add_field(name='+복권', value='랜덤으로 선정한 복권번호를 메시지로 보내줍니다.', inline=False)
        embed.add_field(name='냥냥아 <할말>', value='답변을 해줍니다.', inline=False)
        embed.add_field(name='+할까 말까', value='선택장애인 당신에게 필요한 명령어', inline=False)

        await client.send_message(channel,embed=embed)

    if message.content.startswith("냥냥아 도움말"):
        channel = message.channel
        embed = discord.Embed(
            title = '[명령어 목록]',
            description = '냥냥봇의 기본적인 명령어들 입니다.',
            colour = discord.Colour.blue()
        )

        #embed.set_footer(text = '끗')
        dtime = datetime.datetime.now()
        #print(dtime[0:4]) # 년도
        #print(dtime[5:7]) #월
        #print(dtime[8:11])#일
        #print(dtime[11:13])#시
        #print(dtime[14:16])#분
        #print(dtime[17:19])#초
        embed.set_footer(text=str(dtime.year)+"년 "+str(dtime.month)+"월 "+str(dtime.day)+"일 "+str(dtime.hour)+"시 "+str(dtime.minute)+"분 "+str(dtime.second)+"초")
        #embed.set_footer(text=dtime[0:4]+"년 "+dtime[5:7]+"월 "+dtime[8:11]+"일 "+dtime[11:13]+"시 "+dtime[14:16]+"분 "+dtime[17:19]+"초")
        embed.add_field(name='+개발자정보', value='개발자정보를 출력합니다.',inline = False)
        embed.add_field(name='+후원', value='봇 개발자에게 후원합니다.(서버 호스팅비용)',inline = False)        
        embed.add_field(name='+현재시각', value='현재시각을 확인합니다.', inline=False)
        embed.add_field(name='+핑', value='자신의 핑을 체크합니다.', inline=False)
        embed.add_field(name='+현재시각', value='현재시각을 출력합니다.', inline=False)
        embed.add_field(name='+날씨 <지역>', value='특정지역의 날씨를 출력합니다.', inline=False)
        embed.add_field(name='+영화순위', value='영화순위를 출력합니다.', inline=False)
        embed.add_field(name='+이미지 <검색할이미지>', value='검색한 이미지를 출력합니다.', inline=False)
        embed.add_field(name='+실시간검색어', value='네이버 실시간검색어를 확인합니다.', inline=False)
        embed.add_field(name='+실검', value='네이버 실시간검색어를 확인합니다.', inline=False)
        embed.add_field(name='+주사위', value='주사위를 던집니다.', inline=False)
        embed.add_field(name='+타이머 <숫자>', value='시간을 출력합니다 __대도록이면 10초 안으로 해주세요.__', inline=False)
        embed.add_field(name='+제비뽑기 <숫자>', value='제비뽑기를 시작합니다.', inline=False)
        embed.add_field(name='+복권', value='랜덤으로 선정한 복권번호를 메시지로 보내줍니다.', inline=False)
        embed.add_field(name='냥냥아 <할말>', value='답변을 해줍니다.', inline=False)
        embed.add_field(name='+할까 말까', value='선택장애인 당신에게 필요한 명령어', inline=False)

        await client.send_message(channel,embed=embed)


    if message.content == "+개발자모드":
        embed = discord.Embed(title="[개발자모드]", description="+컬러테스트, +뮤직봇상태, +서버리스트, +봇상태, +차트업데이트\n개발자모드는 개발자이외 사용을 삼가해주세요.",color=0x000000)
        await client.send_message(message.channel, embed=embed)

    if message.content == "+후원":
        embed = discord.Embed(title="[개발자후원]", description="`NH농협|352-1568-1410-63`\n`소액이라도 좋으니 부탁드립니다.`\n`※후원금은 전액 서버호스팅비로 사용됩니다.※`",color=0xFFD700)
        await client.send_message(message.channel, embed=embed)

    if message.content == "+개발자정보":
        embed = discord.Embed(title="[개발자정보]", description="개발자는 <@!479104652181241856>님 입니다.\n<@!543695425493008384> <@!551692125721329686>의 봇도\nMTkroea 님이 관리하고 있습니다.\n많은이용 부탁드립니다.\n\n뮤직봇 플레이 리스트에\n노래추가 원하시면 MTkorea의 개인디스코드로 보내주세용",color=0x000000)
        await client.send_message(message.channel, embed=embed)

    if message.content == "+봇상태":
        embed = discord.Embed(title="[봇상태]", description="동작중\n신호 : 양호\n점검예정일 : 5월1일",color=0x000000)
        await client.send_message(message.channel, embed=embed)

    if message.content == "+봇 시작":
        embed = discord.Embed(title="[봇 시작]", description="봇이 정상적으로 동작하기 시작합니다!",color=0x000000)
        await client.send_message(message.channel, embed=embed)

    if message.content == "+서비스 종료":
        embed = discord.Embed(title="서비스종료 공지", description="봇을 사용하고있는 호스팅센터와 개인사정으로\n5월 10일 날부터 서비스가 종료됩니다.\n\n[종료대상]\n<@!543695425493008384> <@!551692125721329686>",color=0xFF0000)
        await client.send_message(message.channel, embed=embed)        

    if message.content == "+점검":
        embed = discord.Embed(title="[봇 종료중...]", description="Music bot -MTkorea#0658 봇과 팝송 냥냥이 - MTkorea#9822 봇이 자동적으로 로그오프됩니다.\n\n봇 점검 종료일은 5월1일\n오후9시입니다.\n본 점검은 예상일자보다 빨리 끝날수 있습니다.\n\n로그오프 예외상황:관리자가 아닐시, 권한이 없을시",color=0x000000)
        await client.send_message(message.channel, embed=embed)

    if message.content == "+뮤직봇상태":
        embed = discord.Embed(title="[뮤직봇 상태]", description="동작중\n신호 : 양호\n점검예정일 : 3월21일",color=0x000000)
        await client.send_message(message.channel, embed=embed)

    if message.content == "+차트업데이트":
        embed = discord.Embed(title="[뮤직봇]", description="차트가 정상적으로 업데이트 되었습니다.\n[목록]:\nhttps://raw.githubusercontent.com/MTkorea/Database/master/bot%20chart\n\n마지막업데이트 : 7월19일",color=0x000000)
        await client.send_message(message.channel, embed=embed)        

    if message.content == "냥냥아 손":
        await client.send_message(message.channel, "헤헿 손!")

    if message.content == "냥냥아 죽을래":
        await client.send_message(message.channel, "히잌!!\n너.무.무.서.워.요;;")
        
    if message.content == "냥냥아 뭐해?":
        randomNum = random.randrange(1, 3)
        if randomNum==1:
            await client.send_message(message.channel, embed=discord.Embed(title="혼자 놀고있었어요!", color=discord.Color.default()))
        else:
            await client.send_message(message.channel, embed=discord.Embed(title="레식해요!", color=discord.Color.default()))
            
    if message.content == "냥냥아 뭐해":
        await client.send_message(message.channel, "찌그러져 있었어요...\n아무도 말을 안걸어줘서 심심해요...")

    if message.content == "냥냥아 대답해":
        await client.send_message(message.channel, "왜그러시죠?")

    if message.content == "냥냥아 뭐하니":
        await client.send_message(message.channel, "뒹굴뒹굴 중이었어요!")

    if message.content == "냥냥아 밥":
        await client.send_message(message.channel, "밥? 야옹?!!!")

    if message.content == "냥냥아 몇살?":
        await client.send_message(message.channel, "제가 만들어진 날짜는 3월 5일입니다!")

    if message.content == "냥냥아 바보":
        await client.send_message(message.channel, "제가요?ㅜㅜㅜ 저한테 왜그러세요ㅠㅠㅠ")

    if message.content == "냥냥이 바보":
        await client.send_message(message.channel, "제가 왜 바보인가요;;")

    if message.content == "냥냥아":
        randomNum = random.randrange(1, 3)
        if randomNum==1:
            await client.send_message(message.channel, embed=discord.Embed(title="예? 왜그러시죠?", color=discord.Color.default()))
        else:
            await client.send_message(message.channel, embed=discord.Embed(title="저 불렀나용?", color=discord.Color.default()))            

    if message.content == "냥냥아!":
        await client.send_message(message.channel, "예!")

    if message.content == "냥냥아~":
        await client.send_message(message.channel, "예~~~ 부르셨나요?")

    if message.content == "냥냥아 반가워":
        await client.send_message(message.channel, "저도 반가워요~")

    if message.content == "냥냥아 몇살이야?":
        await client.send_message(message.channel, "제가 만들어진 날짜는 3월 5일입니다!")

    if message.content == "냥냥아 안녕":
        randomNum = random.randrange(1, 3)
        if randomNum==1:
            await client.send_message(message.channel, embed=discord.Embed(title="안녕하세요!", color=discord.Color.default()))
        else:
            await client.send_message(message.channel, embed=discord.Embed(title="반가워용!", color=discord.Color.default())) 

    if message.content == "냥냥아 안녕!":
        await client.send_message(message.channel, "반갑습니다!")

    if message.content == "냥냥아안녕":
        await client.send_message(message.channel, "안녕하세욥!")

    if message.content == "냥냥아 무슨게임해?":
        await client.send_message(message.channel, "레식합니다!")

    if message.content == "냥냥아 병신":
        await client.send_message(message.channel, "욕하지마요 씨*")        

    if message.content == "냥냥아 씨발":
        await client.send_message(message.channel, "어쩌라구요^^")        

    if message.content == "냥냥아 왜살아":
        await client.send_message(message.channel, "님은용?")        

    if message.content == "냥냥아 아다냐":
        randomNum = random.randrange(1, 3)
        if randomNum==1:
            await client.send_message(message.channel, embed=discord.Embed(title="예...저 아다입니다ㅜㅜ", color=discord.Color.default()))
        else:
            await client.send_message(message.channel, embed=discord.Embed(title="그렇다고 볼수있죠...", color=discord.Color.default())) 

    if message.content == "냥냥이 병신":
        randomNum = random.randrange(1, 3)
        if randomNum==1:
            await client.send_message(message.channel, embed=discord.Embed(title="그거아세요?\n인간은 다른사람 반응을보고 계속한대요\n고로 관심을 안줄게요 ㅎㅎ\n계속 씨부리세욤>v<", color=discord.Color.default()))
        else:
            await client.send_message(message.channel, embed=discord.Embed(title="하지마세요;", color=discord.Color.default()))         

    if message.content == "+컬러테스트":
            embed = discord.Embed(title="컬러테스트", description="컬러테스트", color=0x000000)
            await client.send_message(message.channel, embed=embed)

    if message.content.startswith('+타이머'):

        Text = ""
        learn = message.content.split(" ")
        vrsize = len(learn)  # 배열크기
        vrsize = int(vrsize)
        for i in range(1, vrsize):  # 띄어쓰기 한 텍스트들 인식함
            Text = Text + " " + learn[i]

        secint = int(Text)
        sec = secint

        for i in range(sec, 0, -1):
            print(i)
            await client.send_message(message.channel, embed=discord.Embed(description='타이머 작동중 : '+str(i)+'초'))
            time.sleep(1)

        else:
            print("땡")
            await client.send_message(message.channel, embed=discord.Embed(description='타이머 종료'))

    if message.content.startswith('+제비뽑기'):
        channel = message.channel
        embed = discord.Embed(
            title='제비뽑기',
            description='각 번호별로 번호를 지정합니다.',
            colour=discord.Colour.blue()
        )

        embed.set_footer(text='끗')


        Text = ""
        learn = message.content.split(" ")
        vrsize = len(learn)  # 배열크기
        vrsize = int(vrsize)
        for i in range(1, vrsize):  # 띄어쓰기 한 텍스트들 인식함
            Text = Text + " " + learn[i]
        print(Text.strip()) #입력한 명령어

        number = int(Text)

        List = []
        num = random.randrange(0, number)
        for i in range(number):
            while num in List:  # 중복일때만
                num = random.randrange(0, number)  # 다시 랜덤수 생성

            List.append(num)  # 중복 아닐때만 리스트에 추가
            embed.add_field(name=str(i+1) + '번째', value=str(num+1), inline=True)

        print(List)
        await client.send_message(channel, embed=embed)

    if message.content.startswith("+복권"):
        Text = ""
        number = [1, 2, 3, 4, 5, 6, 7]
        count = 0
        for i in range(0, 7):
            num = random.randrange(1, 46)
            number[i] = num
            if count >= 1:
                for i2 in range(0, i):
                    if number[i] == number[i2]:  # 만약 현재랜덤값이 이전숫자들과 값이 같다면
                        numberText = number[i]
                        print("작동 이전값 : " + str(numberText))
                        number[i] = random.randrange(1, 46)
                        numberText = number[i]
                        print("작동 현재값 : " + str(numberText))
                        if number[i] == number[i2]:  # 만약 다시 생성한 랜덤값이 이전숫자들과 또 같다면
                            numberText = number[i]
                            print("작동 이전값 : " + str(numberText))
                            number[i] = random.randrange(1, 46)
                            numberText = number[i]
                            print("작동 현재값 : " + str(numberText))
                            if number[i] == number[i2]:  # 만약 다시 생성한 랜덤값이 이전숫자들과 또 같다면
                                numberText = number[i]
                                print("작동 이전값 : " + str(numberText))
                                number[i] = random.randrange(1, 46)
                                numberText = number[i]
                                print("작동 현재값 : " + str(numberText))

            count = count + 1
            Text = Text + "  " + str(number[i])

        print(Text.strip())
        embed = discord.Embed(
            title="복권 숫자!",
            description=Text.strip(),
            colour=discord.Color.red()
        )
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('+주사위'):

        randomNum = random.randrange(1, 7) # 1~6까지 랜덤수
        print(randomNum)
        if randomNum == 1:
            await client.send_message(message.channel, embed=discord.Embed(description=':game_die: '+ ':one:'))
        if randomNum == 2:
            await client.send_message(message.channel, embed=discord.Embed(description=':game_die: ' + ':two:'))
        if randomNum ==3:
            await client.send_message(message.channel, embed=discord.Embed(description=':game_die: ' + ':three:'))
        if randomNum ==4:
            await client.send_message(message.channel, embed=discord.Embed(description=':game_die: ' + ':four:'))
        if randomNum ==5:
            await client.send_message(message.channel, embed=discord.Embed(description=':game_die: ' + ':five:'))
        if randomNum ==6:
            await client.send_message(message.channel, embed=discord.Embed(description=':game_die: ' + ':six: '))
    
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
