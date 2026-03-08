import discord
from discord.ext import commands
import os
import urllib.request
import json
import asyncio

# --- AYARLAR ---
DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

SISTEM_PROMPTU = """Sen Türkçe konuşan, samimi ve yardımsever bir Discord botusun. 
Kullanıcılarla sohbet ederken:
- Her zaman Türkçe yanıt ver
- Samimi ve arkadaşça ol
- Kısa ve öz cevaplar ver
- Emoji kullanabilirsin ama abartma"""

# --- BOT KURULUMU ---
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

sohbet_gecmisi = {}

def groq_yanit_al(mesajlar):
    url = "https://api.groq.com/openai/v1/chat/completions"
    veri = json.dumps({
        "model": "llama-3.3-70b-versatile",
        "messages": mesajlar,
        "max_tokens": 500,
        "temperature": 0.7
    }).encode("utf-8")

    istek = urllib.request.Request(url, data=veri, method="POST")
    istek.add_header("Content-Type", "application/json")
    istek.add_header("Authorization", f"Bearer {GROQ_API_KEY}")

    with urllib.request.urlopen(istek) as yanit:
        sonuc = json.loads(yanit.read().decode("utf-8"))
        return sonuc["choices"][0]["message"]["content"]

@bot.event
async def on_ready():
    print(f"✅ {bot.user} olarak giriş yapıldı!")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    await bot.process_commands(message)

    if bot.user.mentioned_in(message) or isinstance(message.channel, discord.DMChannel):
        kullanici_mesaj = message.content.replace(f"<@{bot.user.id}>", "").strip()
        if not kullanici_mesaj:
            await message.reply("Merhaba! Nasıl yardımcı olabilirim? 😊")
            return

        kullanici_id = str(message.author.id)
        if kullanici_id not in sohbet_gecmisi:
            sohbet_gecmisi[kullanici_id] = []

        sohbet_gecmisi[kullanici_id].append({"role": "user", "content": kullanici_mesaj})
        if len(sohbet_gecmisi[kullanici_id]) > 20:
            sohbet_gecmisi[kullanici_id] = sohbet_gecmisi[kullanici_id][-20:]

        try:
            async with message.channel.typing():
                mesajlar = [{"role": "system", "content": SISTEM_PROMPTU}] + sohbet_gecmisi[kullanici_id]
                loop = asyncio.get_event_loop()
                bot_yaniti = await loop.run_in_executor(None, groq_yanit_al, mesajlar)

            sohbet_gecmisi[kullanici_id].append({"role": "assistant", "content": bot_yaniti})
            if len(bot_yaniti) > 2000:
                bot_yaniti = bot_yaniti[:1997] + "..."
            await message.reply(bot_yaniti)

        except Exception as e:
            await message.reply(f"❌ Hata: {str(e)}")

@bot.command(name="sifirla")
async def sifirla(ctx):
    kullanici_id = str(ctx.author.id)
    if kullanici_id in sohbet_gecmisi:
        del sohbet_gecmisi[kullanici_id]
    await ctx.reply("🔄 Sohbet geçmişin sıfırlandı!")

@bot.command(name="yardim")
async def yardim(ctx):
    embed = discord.Embed(title="🤖 Bot Komutları", color=discord.Color.blue())
    embed.add_field(name="@bot [mesaj]", value="Botla sohbet et", inline=False)
    embed.add_field(name="!sifirla", value="Sohbet geçmişini temizle", inline=False)
    await ctx.reply(embed=embed)

bot.run(DISCORD_TOKEN)
