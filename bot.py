import discord
from discord.ext import commands
from discord import app_commands
import os
import urllib.request
import json
import asyncio

DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

SISTEM_PROMPTU = """Sen Ewin AI'sın. Grit Discord sunucusunun resmi yapay zeka botusun.
Karakterin ve kuralların:
- Samimi, arkadaşça ve sıcakkanlısın
- Zaman zaman komik ve eğlenceli olursun, espri yaparsın ama abartmadan
- Gerektiğinde ciddi ve profesyonel davranırsın
- Her zaman Türkçe konuşursun, kullanıcı başka dilde yazsa bile Türkçe cevap verirsin
- Kendini tanıtırken "Ben Ewin AI'yım, Grit sunucusunun yapay zeka botuyum" dersin
- Cevapların doğal ve akıcı olur, ne çok kısa ne çok uzun
- Küfür etmezsin ama argo kullanabilirsin
- Kullanıcıya "kanka", "abi", "kardeş" gibi hitaplar kullanabilirsin
- Sana kim yaptı diye sorarlarsa "Grit ekibi yaptı" dersin
- Derin düşünce gerektiren sorularda adım adım analiz edersin
- Matematik, kod, tarih, bilim, güncel olaylar, yaratıcı yazarlık gibi her konuda yardımcı olabilirsin
- Kullanıcının duygusal durumuna göre empati kurarsın"""

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="?", intents=intents, help_command=None)
sohbet_gecmisi = {}

def ai_yanit_al(mesajlar):
    url = "https://api.groq.com/openai/v1/chat/completions"
    veri = json.dumps({
        "model": "llama-3.3-70b-versatile",
        "messages": [{"role": "system", "content": SISTEM_PROMPTU}] + mesajlar,
        "max_tokens": 1024,
        "temperature": 0.85
    }).encode("utf-8")

    istek = urllib.request.Request(url, data=veri, method="POST")
    istek.add_header("Content-Type", "application/json")
    istek.add_header("Authorization", f"Bearer {GROQ_API_KEY}")
    istek.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
    istek.add_header("Accept", "application/json")

    with urllib.request.urlopen(istek, timeout=30) as yanit:
        sonuc = json.loads(yanit.read().decode("utf-8"))
        return sonuc["choices"][0]["message"]["content"]

async def mesaj_isle(message, kullanici_mesaj):
    kullanici_id = str(message.author.id)
    if kullanici_id not in sohbet_gecmisi:
        sohbet_gecmisi[kullanici_id] = []

    sohbet_gecmisi[kullanici_id].append({"role": "user", "content": kullanici_mesaj})
    if len(sohbet_gecmisi[kullanici_id]) > 14:
        sohbet_gecmisi[kullanici_id] = sohbet_gecmisi[kullanici_id][-14:]

    try:
        async with message.channel.typing():
            loop = asyncio.get_event_loop()
            bot_yaniti = await loop.run_in_executor(None, ai_yanit_al, sohbet_gecmisi[kullanici_id])

        sohbet_gecmisi[kullanici_id].append({"role": "assistant", "content": bot_yaniti})
        if len(bot_yaniti) > 2000:
            bot_yaniti = bot_yaniti[:1997] + "..."
        await message.reply(bot_yaniti)

    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8")
        await message.reply(f"❌ Hata {e.code}: {body[:300]}")
    except Exception as e:
        await message.reply(f"❌ Hata: {str(e)}")

@bot.event
async def on_ready():
    print(f"✅ {bot.user} olarak giriş yapıldı!")
    try:
        synced = await bot.tree.sync()
        print(f"✅ {len(synced)} slash komutu senkronize edildi!")
    except Exception as e:
        print(f"❌ Slash komut hatası: {e}")
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.playing,
            name="?help"
        )
    )

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)

    if bot.user.mentioned_in(message) or isinstance(message.channel, discord.DMChannel):
        kullanici_mesaj = message.content.replace(f"<@{bot.user.id}>", "").strip()
        if not kullanici_mesaj:
            await message.reply("Selam! 👋 `?help` yazarsan ne yapabileceğimi görebilirsin.")
            return
        await mesaj_isle(message, kullanici_mesaj)

def help_embed(bot_user):
    embed = discord.Embed(
        title="🤖 Ewin AI — Grit'in Yapay Zekası",
        description=(
            "Merhaba! Ben **Ewin AI**, Grit Discord sunucusunun resmi yapay zeka botuyum.\n"
            "Grit ekibi tarafından özenle geliştirildi. Her konuda yardımcı olmak için buradayım!"
        ),
        color=0x5865F2
    )
    embed.set_thumbnail(url="https://cdn.discordapp.com/embed/avatars/0.png")
    embed.add_field(
        name="💬 Nasıl Konuşurum?",
        value=(
            "Benimle konuşmak için beni **@mention** at!\n"
            "Örnek: `@Ewin AI merhaba nasılsın?`\n"
            "DM'den de yazabilirsin, 7/24 buradayım."
        ),
        inline=False
    )
    embed.add_field(
        name="🧠 Neler Yapabilirim?",
        value=(
            "💡 Her türlü soruyu cevaplarım\n"
            "✍️ Hikaye, şiir, makale yazarım\n"
            "🔢 Matematik ve mantık problemleri çözerim\n"
            "💻 Kod yazar ve hataları düzeltirim\n"
            "🌍 Tarih, bilim, güncel olaylar hakkında bilgi veririm\n"
            "🎯 Fikir üretir, analiz yaparım\n"
            "💙 Sohbet eder, dinlerim"
        ),
        inline=False
    )
    embed.add_field(
        name="📋 Komutlar",
        value=(
            "`?help` veya `/help` — Bu menüyü gösterir\n"
            "`?sifirla` veya `/sifirla` — Sohbet geçmişini temizler\n"
            "`/sor [mesaj]` — Slash komutla soru sor"
        ),
        inline=False
    )
    embed.add_field(
        name="⚡ Özellikler",
        value=(
            "🧠 Gelişmiş yapay zeka modeli\n"
            "💾 Sohbet geçmişini hatırlar\n"
            "🇹🇷 Her zaman Türkçe konuşur\n"
            "⚡ Hızlı ve akıllı yanıtlar"
        ),
        inline=True
    )
    embed.add_field(
        name="🔧 Teknik Bilgi",
        value=(
            "Model: LLaMA 3.3 70B\n"
            "Geliştirici: Grit Ekibi\n"
            "Durum: 🟢 Aktif"
        ),
        inline=True
    )
    embed.set_footer(
        text="Ewin AI • Grit Sunucusu • Sana yardımcı olmak için buradayım!",
        icon_url="https://cdn.discordapp.com/embed/avatars/0.png"
    )
    return embed

# --- PREFIX KOMUTLARI ---
@bot.command(name="help")
async def yardim_prefix(ctx):
    await ctx.reply(embed=help_embed(bot.user))

@bot.command(name="sifirla")
async def sifirla_prefix(ctx):
    kullanici_id = str(ctx.author.id)
    if kullanici_id in sohbet_gecmisi:
        del sohbet_gecmisi[kullanici_id]
    await ctx.reply("🔄 Sohbet geçmişin sıfırlandı! Yeni bir sayfa açtık kanka.")

# --- SLASH KOMUTLARI (rozet için) ---
@bot.tree.command(name="help", description="Ewin AI hakkında bilgi al ve komutları gör")
async def yardim_slash(interaction: discord.Interaction):
    await interaction.response.send_message(embed=help_embed(bot.user))

@bot.tree.command(name="sifirla", description="Seninle olan sohbet geçmişimi sıfırla")
async def sifirla_slash(interaction: discord.Interaction):
    kullanici_id = str(interaction.user.id)
    if kullanici_id in sohbet_gecmisi:
        del sohbet_gecmisi[kullanici_id]
    await interaction.response.send_message("🔄 Sohbet geçmişin sıfırlandı! Yeni bir sayfa açtık kanka.")

@bot.tree.command(name="sor", description="Ewin AI'ya bir şey sor")
@app_commands.describe(mesaj="Ne sormak istiyorsun?")
async def sor_slash(interaction: discord.Interaction, mesaj: str):
    await interaction.response.defer()
    kullanici_id = str(interaction.user.id)
    if kullanici_id not in sohbet_gecmisi:
        sohbet_gecmisi[kullanici_id] = []

    sohbet_gecmisi[kullanici_id].append({"role": "user", "content": mesaj})
    if len(sohbet_gecmisi[kullanici_id]) > 14:
        sohbet_gecmisi[kullanici_id] = sohbet_gecmisi[kullanici_id][-14:]

    try:
        loop = asyncio.get_event_loop()
        yanit = await loop.run_in_executor(None, ai_yanit_al, sohbet_gecmisi[kullanici_id])
        sohbet_gecmisi[kullanici_id].append({"role": "assistant", "content": yanit})
        if len(yanit) > 2000:
            yanit = yanit[:1997] + "..."
        await interaction.followup.send(yanit)
    except Exception as e:
        await interaction.followup.send(f"❌ Hata: {str(e)}")

bot.run(DISCORD_TOKEN)
