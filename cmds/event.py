import discord
from discord.ext import commands
import json
import random, os, asyncio

from core.classes import Cog_Extension

intents = discord.Intents.all()
discord.member = True

client = discord.Client(intents=intents)

with open('setting.json',mode='r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(int(jdata['welcome']))
        await channel.send(f'{member} join')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f'{member} leave!')
        channel = self.bot.get_channel(int(jdata['welcome']))
        await channel.send(f'{member} leave')
    
    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        print(reaction)
        print(user)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        print(payload.member)
        print(payload.message_id)
        print(payload.guild_id)
        print(payload.emoji)
        print(payload.user_id)
        print(str(payload.emoji))
        #獲取身分組及起始角色
        if (str(payload.emoji) == "❤️")&(str(payload.message_id) =='923867231195123782') :
            print(payload.member)
            guild = self.bot.get_guild(payload.guild_id)
            beginner=guild.get_role(923913896908173333)
            await payload.member.add_roles(beginner)
            with open('holomem.json',mode='r',encoding='utf8') as hmem:
                holo_0=json.load(hmem)['holo_0_gen']
                mem=random.sample(holo_0,k=3)
                us_name=str(payload.member)
                us_data={us_name:[{"member":mem},{"team":mem},
                {"win_rate":[]},
                {"items":[]},
                {"item_1":[]},
                {"item_2":[]},
                {"item_3":[]},
                {"team_1_skill":["atk1","atk2","def1","def2"]},
                {"team_2_skill":["atk1","atk2","def1","def2"]},
                {"team_3_skill":["atk1","atk2","def1","def2"]}]}
                print(us_name)
                with open('user.json',mode='r',encoding='utf8') as userfile:
                    us_file=json.load(userfile)
                    for i in us_data:
                        us_file[i]=us_data[i]
                        jsobj=json.dumps(us_file, ensure_ascii=False)
                        userfile.close
                        with open('user.json',mode='w',encoding='utf8') as userfin:
                            userfin.write(jsobj)
                            userfin.close
                            print(jsobj)
        if (str(payload.emoji) == "🧡")&(str(payload.message_id) =='923867231195123782') :
            print(payload.member)
            guild = self.bot.get_guild(payload.guild_id)
            beginner=guild.get_role(923913896908173333)
            await payload.member.add_roles(beginner)
            with open('holomem.json',mode='r',encoding='utf8') as hmem:
                holo_0=json.load(hmem)['holo_1_gen']
                mem=random.sample(holo_0,k=3)
                us_name=str(payload.member)
                #創建帳號資訊
                us_data={us_name:[{"member":mem},{"team":mem},
                {"win_rate":[]},
                {"opponent":[0]},#對戰對手(AI or 真人)
                {"status":[0]}, #行動(招式or換人)
                {"items":[]},
                {"item_1":[]},
                {"item_2":[]},
                {"item_3":[]},
                {"team_1_skill":["atk1","atk2","def1","def2"]},
                {"team_2_skill":["atk1","atk2","def1","def2"]},
                {"team_3_skill":["atk1","atk2","def1","def2"]},
                {"team_1_status":[0,2,2,2,2,2,2,2,2,2,2,1,1,1,1,0]},
                #當前HP,攻擊上升,攻擊下降,防禦上升,防禦下降,智力上升,智力下降,幸運上升,幸運下降,速度上升,速度下降,燒傷,麻痺,中毒,冰凍,控制(安可,挑釁,誘惑,踩影)
                {"team_2_status":[0,2,2,2,2,2,2,2,2,2,2,1,1,1,1,0]},
                {"team_3_status":[0,2,2,2,2,2,2,2,2,2,2,1,1,1,1,0]}
                ]}
                us_data_ai={str(us_name+"_AI"):[]}
                #創建帳號對應ai(野怪)
                print(us_name)
                with open('user.json',mode='r',encoding='utf8') as userfile:
                    us_file=json.load(userfile)
                    for i in us_data:
                        us_file[i]=us_data[i]
                    jsobj=json.dumps(us_file, ensure_ascii=False)
                    userfile.close
                    with open('user.json',mode='w',encoding='utf8') as userfin:
                        userfin.write(jsobj)
                        userfin.close
                        print(jsobj)        
                with open('user.json',mode='r',encoding='utf8') as userfile_2:
                    us_file_2=json.load(userfile_2)
                    for i in us_data_ai:
                        us_file_2[i]=us_data_ai[i]
                    jsobjai=json.dumps(us_file_2, ensure_ascii=False)
                    userfile_2.close
                with open('user.json',mode='w',encoding='utf8') as userfin_2:
                    userfin_2.write(jsobjai)
                    userfin_2.close
                with open('user.json',mode='r',encoding='utf8') as userfin_3:
                    p=json.load(userfin_3 )
                    print(p[us_name][0]["member"])
        if (str(payload.emoji) == "💛")&(str(payload.message_id) =='923867231195123782') :
            print(payload.member)
            guild = self.bot.get_guild(payload.guild_id)
            beginner=guild.get_role(923913896908173333)
            await payload.member.add_roles(beginner)
            with open('holomem.json',mode='r',encoding='utf8') as hmem:
                holo_0=json.load(hmem)['holo_2_gen']
                mem=random.sample(holo_0,k=3)
                us_name=str(payload.member)
                us_data={us_name:[{"member":mem},{"team":mem},
                {"win_rate":[]},
                {"items":[]},
                {"item_1":[]},
                {"item_2":[]},
                {"item_3":[]},
                {"team_1_skill":["atk1","atk2","def1","def2"]},
                {"team_2_skill":["atk1","atk2","def1","def2"]},
                {"team_3_skill":["atk1","atk2","def1","def2"]}]}
                print(us_name)
                with open('user.json',mode='r',encoding='utf8') as userfile:
                    us_file=json.load(userfile)
                    for i in us_data:
                        us_file[i]=us_data[i]
                        jsobj=json.dumps(us_file, ensure_ascii=False)
                        userfile.close
                        with open('user.json',mode='w',encoding='utf8') as userfin:
                            userfin.write(jsobj)
                            userfin.close
                            print(jsobj)  
        if (str(payload.emoji) == "💚")&(str(payload.message_id) =='923867231195123782') :
            print(payload.member)
            guild = self.bot.get_guild(payload.guild_id)
            beginner=guild.get_role(923913896908173333)
            await payload.member.add_roles(beginner)
            with open('holomem.json',mode='r',encoding='utf8') as hmem:
                holo_0=json.load(hmem)['holo_3_gen']
                mem=random.sample(holo_0,k=3)
                us_name=str(payload.member)
                us_data={us_name:[{"member":mem},{"team":mem},
                {"win_rate":[]},
                {"items":[]},
                {"item_1":[]},
                {"item_2":[]},
                {"item_3":[]},
                {"team_1_skill":["atk1","atk2","def1","def2"]},
                {"team_2_skill":["atk1","atk2","def1","def2"]},
                {"team_3_skill":["atk1","atk2","def1","def2"]}]}
                print(us_name)
                with open('user.json',mode='r',encoding='utf8') as userfile:
                    us_file=json.load(userfile)
                    for i in us_data:
                        us_file[i]=us_data[i]
                        jsobj=json.dumps(us_file, ensure_ascii=False)
                        userfile.close
                        with open('user.json',mode='w',encoding='utf8') as userfin:
                            userfin.write(jsobj)
                            userfin.close
                            print(jsobj)
        if (str(payload.emoji) == "💙")&(str(payload.message_id) =='923867231195123782') :
            print(payload.member)
            guild = self.bot.get_guild(payload.guild_id)
            beginner=guild.get_role(923913896908173333)
            await payload.member.add_roles(beginner)
            with open('holomem.json',mode='r',encoding='utf8') as hmem:
                holo_0=json.load(hmem)['holo_4_gen']
                mem=random.sample(holo_0,k=3)
                us_name=str(payload.member)
                us_data={us_name:[{"member":mem},{"team":mem},
                {"win_rate":[]},
                {"items":[]},
                {"item_1":[]},
                {"item_2":[]},
                {"item_3":[]},
                {"team_1_skill":["atk1","atk2","def1","def2"]},
                {"team_2_skill":["atk1","atk2","def1","def2"]},
                {"team_3_skill":["atk1","atk2","def1","def2"]}]}
                print(us_name)
                with open('user.json',mode='r',encoding='utf8') as userfile:
                    us_file=json.load(userfile)
                    for i in us_data:
                        us_file[i]=us_data[i]
                        jsobj=json.dumps(us_file, ensure_ascii=False)
                        userfile.close
                        with open('user.json',mode='w',encoding='utf8') as userfin:
                            userfin.write(jsobj)
                            userfin.close
                            print(jsobj)
        if (str(payload.emoji) == "💜")&(str(payload.message_id) =='923867231195123782') :
            print(payload.member)
            guild = self.bot.get_guild(payload.guild_id)
            beginner=guild.get_role(923913896908173333)
            await payload.member.add_roles(beginner)
            with open('holomem.json',mode='r',encoding='utf8') as hmem:
                holo_0=json.load(hmem)['holo_5_gen']
                mem=random.sample(holo_0,k=3)
                us_name=str(payload.member)
                us_data={us_name:[{"member":mem},{"team":mem},
                {"win_rate":[]},
                {"items":[]},
                {"item_1":[]},
                {"item_2":[]},
                {"item_3":[]},
                {"team_1_skill":["atk1","atk2","def1","def2"]},
                {"team_2_skill":["atk1","atk2","def1","def2"]},
                {"team_3_skill":["atk1","atk2","def1","def2"]}]}
                print(us_name)
                with open('user.json',mode='r',encoding='utf8') as userfile:
                    us_file=json.load(userfile)
                    for i in us_data:
                        us_file[i]=us_data[i]
                        jsobj=json.dumps(us_file, ensure_ascii=False)
                        userfile.close
                        with open('user.json',mode='w',encoding='utf8') as userfin:
                            userfin.write(jsobj)
                            userfin.close
                            print(jsobj)


def setup(bot):
    bot.add_cog(Event(bot))