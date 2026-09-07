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
import time
import speedtest
import discord

@bot.command(name='p')
async def p(ctx):
    inicio = time.time()
    msg = await ctx.send(embed=discord.Embed(
        title="⚡ Loki SpeedTest", 
        description="Iniciando test... ⏳", 
        color=0xff0000
    ))
    
    # Ping a Discord
    fin = time.time()
    ping_discord = round((fin - inicio) * 1000)
    ping_api = round(bot.latency * 1000)
    
    await msg.edit(embed=discord.Embed(
        title="⚡ Loki SpeedTest", 
        description="Conectando al mejor servidor...", 
        color=0xffaa00
    ))
    
    try:
        # Test de velocidad
        st = speedtest.Speedtest()
        st.get_best_server()
        server = st.results.server['name']
        
        st.download()
        down = round(st.results.download / 1_000_000, 2)
        
        st.upload()
        up = round(st.results.upload / 1_000_000, 2)
        
        server_ping = st.results.ping
        tiempo_total = round(time.time() - inicio, 2)
        
        embed = discord.Embed(title="⚡ Resultado SpeedTest", color=0x00ff00)
        embed.add_field(name="📶 Ping Discord", value=f"{ping_discord}ms", inline=True)
        embed.add_field(name="🌐 Ping API", value=f"{ping_api}ms", inline=True)
        embed.add_field(name="🖥️ Ping Servidor", value=f"{server_ping}ms", inline=True)
        embed.add_field(name="📥 Bajada", value=f"{down} Mbps", inline=True)
        embed.add_field(name="📤 Subida", value=f"{up} Mbps", inline=True)
        embed.add_field(name="⏱️ Tiempo", value=f"{tiempo_total}s", inline=True)
        embed.add_field(name="📍 Servidor", value=server, inline=False)
        embed.set_footer(text="Test por Loki Bot")
        
        await msg.edit(embed=embed)
        
    except Exception as e:
        await msg.edit(embed=discord.Embed(
            title="❌ Error", 
            description=f"No se pudo hacer el test: {e}\nKoyeb gratis a veces bloquea esto", 
            color=0xff0000
        ))
