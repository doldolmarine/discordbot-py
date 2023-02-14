import discord
from discord.ext import commands
while True:
    comdo =';'
    app = commands.Bot(intents
                       =discord.Intents.default(), command_prefix=comdo ) #command_prefix=comdo     
    @app.event
    async def on_ready():
        print('다음으로 로그인합니다: {}'.format(app.user.name))
        await app.change_presence(status=discord.Status.do_not_disturb  , activity=None, )


    @app.event
    async def sayon(ctx):
        if ctx.content.startswith('ab'):
            await ctx.channel.sand('반갑습니다')
        

    app.run('MTA3NDkxNDg5ODMwNTM1NTc3Ng.GF672Y.BEprEDtepCdDE-p6_jMeXQKAQKYAv88pUXXu5Y')
