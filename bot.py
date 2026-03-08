import discord
from discord.ext import commands
import os
import urllib.request
import json
import asyncio

DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

SISTEM_PROMPTU = """Sen Türkçe konuşan, samimi ve yardımsever bir Discord botusun. 
Her zaman Türkçe yanıt ver, samimi ve arkadaşça ol, kısa ve öz cevaplar ver."""

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

sohbet_gecmisi = {}

def gemini_yanit_al(mesajlar):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"
    
    # Sistem promptunu ve geçmişi birleştir
    icerik = [{"role": "user", "parts": [{"text": SISTEM_PROMPTU}]},
              {"role": "model", "parts": [{"text": "Anladım, Türkçe konuşan yardımsever bir bot olarak hizmet vereceğim!"}]}]
    
    for m in mesajlar:
        rol = "user" if m["role"] == "user" else "model"
        icerik.append({"role": rol, "parts": [{"text": m["content"]}]})
    
    veri = json.dumps({"contents": icerik}).encode("utf-8")
    istek = urllib.request.Request(url, data=veri, method="POST")
    istek.add_header("Content-Type", "application/json")
    
    with urllib.request.urlopen(istek) as yanit:
        sonuc = json.loads(yanit.read().decode("utf-8"))
        return sonuc["candidates"][0]["content"]["parts"][0]["text"]

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
                loop = asyncio.get_event_loop()
                bot_yaniti = await loop.run_in_executor(None, gemini_yanit_al, sohbet_gecmisi[kullanici_id])

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

bot.run(DISCORD_TOKEN)
