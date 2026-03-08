import discord
from discord.ext import commands
from groq import Groq
import os

# --- AYARLAR ---
DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

# Botun yanıt vereceği kanal ID'si (0 = tüm kanallar)
KANAL_ID = 0

# Botun karakteri / sistem promptu
SISTEM_PROMPTU = """Sen Türkçe konuşan, samimi ve yardımsever bir Discord botusun. 
Kullanıcılarla sohbet ederken:
- Her zaman Türkçe yanıt ver
- Samimi ve arkadaşça ol
- Kısa ve öz cevaplar ver (çok uzun yazma)
- Emoji kullanabilirsin ama abartma
- Argo veya küfürlü dil kullanma"""

# --- BOT KURULUMU ---
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)
groq_client = Groq(api_key=GROQ_API_KEY)

# Her kullanıcı için sohbet geçmişi (botun hafızası)
sohbet_gecmisi = {}

@bot.event
async def on_ready():
    print(f"✅ {bot.user} olarak giriş yapıldı!")
    print(f"📡 {len(bot.guilds)} sunucuda aktif")

@bot.event
async def on_message(message):
    # Botun kendi mesajlarını yoksay
    if message.author == bot.user:
        return

    # Komutları işle (!yardım, !sifirla gibi)
    await bot.process_commands(message)

    # Belirli bir kanal ayarlandıysa sadece orada yanıtla
    if KANAL_ID != 0 and message.channel.id != KANAL_ID:
        return

    # Komut değilse ve bota mention varsa VEYA direkt mesajsa yanıtla
    # Eğer her mesaja yanıt vermesini istersen aşağıdaki satırı düzenle
    if bot.user.mentioned_in(message) or isinstance(message.channel, discord.DMChannel):
        kullanici_mesaj = message.content.replace(f"<@{bot.user.id}>", "").strip()

        if not kullanici_mesaj:
            await message.reply("Merhaba! Nasıl yardımcı olabilirim? 😊")
            return

        await yanit_ver(message, kullanici_mesaj)

    await bot.process_commands(message)

async def yanit_ver(message, kullanici_mesaj):
    """Groq API'ye istek at ve yanıtı Discord'a gönder"""
    kullanici_id = str(message.author.id)

    # Bu kullanıcının geçmişi yoksa oluştur
    if kullanici_id not in sohbet_gecmisi:
        sohbet_gecmisi[kullanici_id] = []

    # Kullanıcının mesajını geçmişe ekle
    sohbet_gecmisi[kullanici_id].append({
        "role": "user",
        "content": kullanici_mesaj
    })

    # Geçmişi max 20 mesajla sınırla (token tasarrufu)
    if len(sohbet_gecmisi[kullanici_id]) > 20:
        sohbet_gecmisi[kullanici_id] = sohbet_gecmisi[kullanici_id][-20:]

    try:
        # "Yazıyor..." göster
        async with message.channel.typing():
            yanit = groq_client.chat.completions.create(
                model="llama-3.3-70b-versatile",  # Groq'un en iyi ücretsiz modeli
                messages=[
                    {"role": "system", "content": SISTEM_PROMPTU},
                    *sohbet_gecmisi[kullanici_id]
                ],
                max_tokens=500,
                temperature=0.7
            )

        bot_yaniti = yanit.choices[0].message.content

        # Bot yanıtını geçmişe ekle
        sohbet_gecmisi[kullanici_id].append({
            "role": "assistant",
            "content": bot_yaniti
        })

        # Discord'a gönder (2000 karakter limiti var)
        if len(bot_yaniti) > 2000:
            bot_yaniti = bot_yaniti[:1997] + "..."

        await message.reply(bot_yaniti)

    except Exception as e:
        await message.reply(f"❌ Bir hata oluştu: {str(e)}")

# --- KOMUTLAR ---

@bot.command(name="sifirla")
async def sifirla(ctx):
    """Sohbet geçmişini sıfırla"""
    kullanici_id = str(ctx.author.id)
    if kullanici_id in sohbet_gecmisi:
        del sohbet_gecmisi[kullanici_id]
    await ctx.reply("🔄 Sohbet geçmişin sıfırlandı! Yeni bir sohbete başlayabiliriz.")

@bot.command(name="yardim")
async def yardim(ctx):
    """Yardım mesajı göster"""
    embed = discord.Embed(
        title="🤖 Bot Komutları",
        color=discord.Color.blue()
    )
    embed.add_field(name="@bot [mesaj]", value="Botla sohbet et", inline=False)
    embed.add_field(name="!sifirla", value="Sohbet geçmişini temizle", inline=False)
    embed.add_field(name="!yardim", value="Bu mesajı göster", inline=False)
    await ctx.reply(embed=embed)

# Botu çalıştır
bot.run(DISCORD_TOKEN)
