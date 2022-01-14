
import nest_asyncio 
nest_asyncio.apply()
import discord
import asyncio
import urllib.request
from bs4 import BeautifulSoup
from urllib import parse
import random
from time import time
import discord, asyncio, random, re, time, os, bs4, urllib, requests, re
import datetime



client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("삐악이")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_reaction_add(reaction, user):
    if user.bot == 1: #봇이면 패스
        return None

@client.event
async def on_message(message):
        if message.content.startswith("!"):
                msg = message.content.split(" ")
                msg[0] = msg[0][1:]
                if msg[0] == "만든이":
                        await message.channel.send("God영철")
                elif msg[0] == "흐르는총알":
                    await message.channel.send("")
                elif msg[0] == "루찌배마":
                    await message.channel.send("The 길드마스터")
                elif msg[0] == "에베붸벱":
                    await message.channel.send("수락 리버시티 CU쟁이")
                elif msg[0] == "쌜밍":
                    await message.channel.send("존엄바드")
                elif msg[0] == "웜어":
                    await message.channel.send("창든 유미")
                elif msg[0] == "박살":
                    await message.channel.send("잔혹한 혈투사")
                elif msg[0] == "흩날려라유령무희":
                    await message.channel.send("분노조절장애")
                elif msg[0] == "삐악이":
                    await message.channel.send("Happy New Year")           
                elif msg[0] == "네루다":
                    await message.channel.send("자책머신")                 
                elif msg[0] == "강한다홀":
                    await message.channel.send("~이슈 숙코") 
                elif msg[0] == "소금잉":
                    await message.channel.send("숙련인데 트라이인척~") 
                elif msg[0] == "샨모씨":
                    await message.channel.send("전설의 포켓몬")
                elif msg[0] == "홍달자":
                    await message.channel.send("인파1")  
                elif msg[0] == "글로벌허세":
                    await message.channel.send("인파2") 
                elif msg[0] == "곰도":
                    await message.channel.send("인파3") 

                elif msg[0] == "원정대골드":

                    def goldcal(a,b,c,d,e,f,g,h,i,j,k):
                        #1415:a,1430:b,1445:c,1460:d,1475:e,1490:f,1500:g,1520,:h
                        gold = 0
                        gold += a*4100
                        gold += b*6600
                        gold += c*8600
                        gold += d*10600
                        gold += e*13500
                        gold += f*13500
                        gold += g*15000
                        gold += h*17500
                        gold += i*18500
                        gold += j*19000
                        gold += k*19500

                        return gold

                    if msg[1] == "웜어":
                        await message.channel.send(goldcal(2,2,0,0,0,0,0,0,1,0,0))
                    elif msg[1] == "루찌배마":
                        await message.channel.send(goldcal(0,1,1,0,1,0,0,0,1,0,1))
                    elif msg[1] == "바나나맛곰":
                        await message.channel.send(goldcal(0,0,1,0,0,0,0,0,0,0,1))
                    elif msg[1] == "네루다":
                        await message.channel.send(goldcal(0,0,3,0,1,0,1,0,0,0,1))
                    elif msg[1] == "곰도":
                        await message.channel.send(goldcal(0,1,2,1,0,0,0,0,0,0,1))
                    elif msg[1] == "쥬니퍼":
                        await message.channel.send(goldcal(1,0,1,2,0,0,0,0,0,0,1))
                    elif msg[1] == "흐르는총알":
                        await message.channel.send(goldcal(0,0,0,0,0,2,0,0,3,0,1))
                    elif msg[1] == "더디그":
                        await message.channel.send(goldcal(1,0,4,0,0,0,0,0,0,1,0))
                    elif msg[1] == "kixx":
                        await message.channel.send(goldcal(0,0,2,0,1,1,1,0,1,0,0))
                    elif msg[1] == "에베붸벱":
                        await message.channel.send(goldcal(1,0,3,0,1,0,0,0,0,0,1))
                    elif msg[1] == "쌜밍":
                        await message.channel.send(goldcal(1,1,1,0,1,0,0,0,0,0,1))
                    elif msg[1] == "박살":
                        await message.channel.send(goldcal(2,0,1,0,0,0,0,0,0,0,1))

                elif msg[0] == "파티모집":
                    now = datetime.datetime.now()
                    embed = discord.Embed(title=msg[1],description=now.strftime('%Y-%m-%d'), color=0x00aaaa)
                    embed.add_field(name="본캐딜러⚔️", value="본캐딜러는 ⚔️에 투표해주세요 ", inline=False)
                    embed.add_field(name="부캐딜러🍺", value="부캐딜러는 🍺에 투표해주세요 ", inline=False)
                    embed.add_field(name="유미🦶", value="본캐 부캐 상관없이 유미는 🦶에 투표해주세요. You and Me ", inline=False)
                    embed.add_field(name="※주의", value="삐악이가 투표했으니 인원수를 잘 확인해주세요", inline=False)
                    
                    msg = await message.channel.send(embed=embed)
                    await msg.add_reaction("⚔️")
                    await msg.add_reaction("🍺") 
                    await msg.add_reaction("🦶") 
                
                elif msg[0] == "정보":
                    resText = "'''"
                    profileUrl = "https://lostark.game.onstove.com/Profile/Character/"
                    await message.channel.send(msg[1] + "님의 전투정보실 링크에요!\n" + profileUrl + msg[1]) 



                elif msg[0] == "사사게":
                        resText = "```"
                        #profileUrl = "https://lostark.game.onstove.com/Profile/Character/"
                        profileUrl = "https://www.inven.co.kr/board/lostark/5355?query=list&p=1&my=chu&sterm=&name=subject&keyword="
                        await message.channel.send(msg[1] + "님의 사사게 링크에요!\n" + profileUrl + msg[1])
                        """encStr = parse.quote(msg[1])
                        profileUrl = profileUrl + encStr
                        req = urllib.request.urlopen(profileUrl)
                        res = req.read()

                        soup = BeautifulSoup(res, 'html.parser')  # BeautifulSoup 객체생성

                        loahaeUrl = "https://loahae.com/profile/"
                        loahaeUrl = loahaeUrl + encStr
                        req2 = urllib.request.urlopen(loahaeUrl)
                        res2 = req2.read()
                        soup2 = BeautifulSoup(res2, 'html.parser')  # BeautifulSoup 객체생성
                        serverName = soup.find_all('div', class_='game-info__server')
                        serverName = [each_line.get_text().strip() for each_line in serverName[:20]]
                        guildName = soup.find_all('div', class_='game-info__guild')
                        guildName = [each_line.get_text().strip() for each_line in guildName[:20]]
                        className = soup.find_all('div', class_='game-info__class')
                        className = [each_line.get_text().strip() for each_line in className[:20]]
                        levelInfoItem = soup.find_all('div', class_='level-info__item')
                        levelInfoItem = [each_line.get_text().strip() for each_line in levelInfoItem[:20]]
                        levelInfoExpd = soup.find_all('div', class_='level-info__expedition')
                        levelInfoExpd = [each_line.get_text().strip() for each_line in levelInfoExpd[:20]]
                        ability = soup.find_all('div', class_='profile-ability-basic')
                        ability = [each_line.get_text().strip() for each_line in ability[:20]]
                        abilArray = ability[0].split('\n')
                        resText += msg[1] + "[" + serverName[0][3:] + "/" + guildName[0][2:] + "] - " + className[0][3:] + "\n"
                        resText += "레벨: " + levelInfoItem[0][6:] + "(" + levelInfoExpd[0][6:] + ")" + "\n"
                        abil1 = ""
                        for i in abilArray:
                                if '힘 ' in i[:2] or '지능 ' in i[:2] or '체력 ' in i[:4]:
                                        abil1 = abil1 + i + "\n"
                        resText += abil1 + "\n"

                        abilityBattle = soup.find_all('div', class_='profile-ability-battle')
                        abilityBattle = [each_line.get_text().strip() for each_line in abilityBattle[:]]
                        abil2Array = abilityBattle[0].split('\n')
                        abil2 = ""
                        for i in abil2Array:
                                if '치명 ' in i[:4] or '특화 ' in i[:4] or '제압 ' in i[:4] or '신속 ' in i[:4] or '인내 ' in i[:4] or '숙련 ' in i[:4]:
                                        abil2 = abil2 + i + "\n"
                        resText += abil2 + "\n"

                        abilityEngrave = soup.find_all('div', class_='profile-ability-engrave')
                        abilityEngrave = [each_line.get_text().strip() for each_line in abilityEngrave[:]]
                        abil3Array = abilityEngrave[0].split('\n')
                        abil3 = ""
                        for i in abil3Array:
                                if 'Lv' in i or '펫' in i[:4]:
                                        abil3 += i + "\n"
                        resText += abil3 + "\n"
                        rank1 = soup2.find_all('div', class_='infobox infobox-l')
                        rank1 = [each_line.get_text().strip() for each_line in rank1[:10]]
                        for i in rank1:
                                for j in i.split("\n"):
                                        resText += j + " - "
                                resText = resText[:len(resText) - 2]
                                resText += "\n"
                        rank2 = soup2.find_all('div', class_='infobox infobox-r')
                        rank2 = [each_line.get_text().strip() for each_line in rank2[:10]]
                        for i in rank2:
                                for j in i.split("\n"):
                                        resText += j + " - "
                                resText = resText[:len(resText) - 2]
                                resText += "\n"
                        resText += "```"
                        await message.channel.send(resText)"""

                elif msg[0] == "주사위":
                        r = random.randrange(1,100)
                        await message.channel.send(message.author.name + "님의 주사위는 ~~~~ " + repr(r) + " 입니다. (1-100)")

               
                elif msg[0] == "강화":
                    def isNumber(s):
                        try:
                            float(s)
                            return True
                        except ValueError:
                            return False
                    if len(msg) < 2:
                            await message.channel.send("명령어를 !강화 [확률]로 입력하면 강화 시뮬레이션을 해볼 수 있어요!")
                    elif isNumber(msg[1])==True:
                            r = random.randrange(1,100)
                            await message.channel.send("강화 결과는...")
                            time.sleep(2)
                            await message.channel.send("성공!" if r <= int(msg[1]) else "꽝! 장인의 기운이 쌓여가네요..")
                    else:
                             await message.channel.send("숫자만 입력해주세요!")
      
                elif msg[0] == "도움말":
                        await message.channel.send(msg)

                        str = "*---명령어---*\n"
                        str += "명령어 : 주사위, 강화, 사사게, 파티모집, 정보\n"
                        str += "명령어 추가 및 업데이트는 웜어에게 말해주세요 :)"
                        
                        await message.channel.send(str)

client.run('TOKEN')
