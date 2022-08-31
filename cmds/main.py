import discord
from discord.ext import commands
import json
import random, os, asyncio
from core.classes import Cog_Extension

class Main(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(self.bot.latency*1000)}(ms)')

    @commands.command()
    async def peko(self, ctx):
        pic_peko=discord.File('D:\\Holomon\\Project_holo\\pic\\pekora.jpg')
        await ctx.send(file=pic_peko)
    @commands.command()
    async def gen0(self, ctx):
        with open('holomem.json',mode='r',encoding='utf8') as hmem:
                holo_0=json.load(hmem)['holo_0_gen']
                mem=random.sample(holo_0,k=3)
                us_name=str(ctx.message.author)
                us_data={us_name:[{"member":mem},{"team":mem},
                {"team_1_skill":["atk1","atk2","def1","def2"]},
                {"team_2_skill":["atk1","atk2","def1","def2"]},
                {"team_3_skill":["atk1","atk2","def1","def2"]}]}
                print(str(ctx.message.author))
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
                    
    @commands.command()
    async def mem(self, ctx):#目前擁有的角色
        with open('user.json',mode='r',encoding='utf8') as userfin_3:
            p=json.load(userfin_3 )
            usname=str(ctx.message.author)
            memb=str(p[usname][0]["member"])
            await ctx.send(usname+"目前擁有的角色有:"+memb)

    @commands.command()
    async def team(self, ctx):#目前的隊伍
        with open('user.json',mode='r',encoding='utf8') as userfin_3:
            p=json.load(userfin_3 )
            usname=str(ctx.message.author)
            teamm=str(p[usname][1]["team"])
            await ctx.send(usname+"目前的隊伍成員為:"+teamm)

    @commands.command()
    async def team_info(self, ctx):
        embed=discord.Embed(title="Team info", description="當前隊伍及招式", color=0x1fffb4)
        embed.set_author(name="QAQ", icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ0Uq9lBhkHYd6rTJoou4Ww5DWnQMEzTxsghA&usqp=CAU")
        embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ0Uq9lBhkHYd6rTJoou4Ww5DWnQMEzTxsghA&usqp=CAU")
        embed.add_field(name="隊伍", value="undefined", inline=False)
        embed.add_field(name="前鋒招式", value="undefined", inline=True)
        embed.add_field(name="中鋒招式", value="undefined", inline=True)
        embed.add_field(name="大將招式", value="undefined", inline=True)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Main(bot))
