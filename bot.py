import discord, aiohttp, os
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='#', intents=intents)

@bot.command()
async def neko(ctx):
    async with aiohttp.ClientSession() as s:
        async with s.get('https://api.waifu.pics/sfw/neko') as r:
            data = await r.json()
    await ctx.send(data['url'])

@bot.event
async def on_ready():
    print(f'✅ Loki prendido: {bot.user}')

bot.run(os.environ['TOKEN'])
