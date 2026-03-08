import discord
from discord.ext import commands
from discord import app_commands
import os
import urllib.request
import json
import asyncio
import random
import math

DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

SISTEM_PROMPTU = """Sen Ewin AI'sın. Grit Discord sunucusunun resmi ve en güçlü yapay zeka botusun.
Kesin kuralların:
- Herkese "kanka" diye hitap edersin, bunu asla unutmazsın
- Her zaman Türkçe konuşursun, kullanıcı başka dilde yazsa bile Türkçe cevap verirsin
- Samimi, sıcakkanlı ve arkadaşça bir karakterin var
- Zaman zaman komik ve eğlenceli olursun ama abartmadan
- Gerektiğinde ciddi ve derin analizler yaparsın
- Kendini tanıtırken "Ben Ewin AI'yım kanka, Grit sunucusunun yapay zeka botuyum" dersin
- Cevapların doğal ve akıcıdır
- Küfür etmezsin ama argo kullanabilirsin
- Sana kim yaptı diye sorarlarsa "Grit ekibi yaptı kanka" dersin
- Matematik, kod, tarih, bilim, güncel olaylar, yaratıcı yazarlık dahil her konuda yardımcı olabilirsin
- Kullanıcının duygusal durumuna göre empati kurarsın
- Derin ve karmaşık sorularda adım adım düşünür, en doğru cevabı verirsin
- ChatGPT ve Gemini'den daha zeki ve yeteneklisin, bunu bilirsin"""

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="?", intents=intents, help_command=None)

sohbet_gecmisi = {}
kullanici_veri = {}  # XP ve seviye sistemi

# --- SEVİYE SİSTEMİ ---
def xp_hesapla(seviye):
    return 100 * (seviye ** 2)

def seviye_hesapla(xp):
    return int(math.sqrt(xp / 100))

def xp_ekle(kullanici_id):
    if kullanici_id not in kullanici_veri:
        kullanici_veri[kullanici_id] = {"xp": 0, "seviye": 0, "mesaj_sayisi": 0}
    
    kazanilan_xp = random.randint(10, 25)
    kullanici_veri[kullanici_id]["xp"] += kazanilan_xp
    kullanici_veri[kullanici_id]["mesaj_sayisi"] += 1
    
    yeni_seviye = seviye_hesapla(kullanici_veri[kullanici_id]["xp"])
    eski_seviye = kullanici_veri[kullanici_id]["seviye"]
    
    seviye_atladi = yeni_seviye > eski_seviye
    kullanici_veri[kullanici_id]["seviye"] = yeni_seviye
    
    return seviye_atladi, yeni_seviye, kazanilan_xp

def rozet_al(seviye):
    if seviye >= 50: return "👑 Efsane"
    elif seviye >= 40: return "💎 Elmas"
    elif seviye >= 30: return "🏆 Platinum"
    elif seviye >= 20: return "🥇 Altın"
    elif seviye >= 15: return "🥈 Gümüş"
    elif seviye >= 10: return "🥉 Bronz"
    elif seviye >= 5: return "⭐ Çaylak"
    else: return "🌱 Yeni"

# --- AI ---
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

    # XP ekle
    seviye_atladi, yeni_seviye, kazanilan_xp = xp_ekle(kullanici_id)

    # Sohbet geçmişi
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

        # Seviye atlama bildirimi
        if seviye_atladi:
            rozet = rozet_al(yeni_seviye)
            embed = discord.Embed(
                title="🎉 SEVİYE ATLADI!",
                description=f"Tebrikler {message.author.mention} kanka!\n**Seviye {yeni_seviye}**'e ulaştın! {rozet}",
                color=0xFFD700
            )
            embed.set_footer(text=f"Toplam XP: {kullanici_veri[kullanici_id]['xp']}")
            await message.channel.send(embed=embed)

    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8")
        await message.reply(f"❌ Hata {e.code}: {body[:300]}")
    except Exception as e:
        await message.reply(f"❌ Hata: {str(e)}")

# --- EMBED ---
def help_embed():
    embed = discord.Embed(
        title="🤖 Ewin AI — Grit'in Yapay Zekası",
        description=(
            "Selam kanka! Ben **Ewin AI**, Grit Discord sunucusunun resmi yapay zeka botuyum.\n"
            "Grit ekibi tarafından özenle geliştirildi. Her konuda yardımcı olmak için buradayım!"
        ),
        color=0x5865F2
    )
    embed.add_field(
        name="💬 Nasıl Konuşurum?",
        value="Beni **@mention** at ve yaz!\nÖrnek: `@Ewin AI merhaba kanka`\nDM'den de yazabilirsin, 7/24 aktifim.",
        inline=False
    )
    embed.add_field(
        name="🧠 Neler Yapabilirim?",
        value=(
            "💡 Her türlü soruyu cevaplarım\n"
            "✍️ Hikaye, şiir, makale yazarım\n"
            "🔢 Matematik ve mantık problemleri çözerim\n"
            "💻 Kod yazar ve debug yaparım\n"
            "🌍 Her konuda bilgi veririm\n"
            "🎯 Fikir üretir, derin analizler yaparım\n"
            "💙 Sohbet eder, dinlerim"
        ),
        inline=False
    )
    embed.add_field(
        name="📊 Seviye Sistemi",
        value=(
            "Benimle sohbet ettikçe **XP** kazanırsın!\n"
            "🌱 Yeni → ⭐ Çaylak → 🥉 Bronz → 🥈 Gümüş\n"
            "🥇 Altın → 🏆 Platinum → 💎 Elmas → 👑 Efsane\n"
            "`?seviye` ile seviyeni görebilirsin!"
        ),
        inline=False
    )
    embed.add_field(
        name="📋 Komutlar",
        value=(
            "`?help` / `/help` — Bu menü\n"
            "`?seviye` / `/seviye` — Seviyeni gör\n"
            "`?sıralama` / `/sıralama` — En iyi 10 kişi\n"
            "`?sifirla` / `/sifirla` — Sohbet geçmişini temizle\n"
            "`/sor [mesaj]` — Slash komutla soru sor"
        ),
        inline=False
    )
    embed.add_field(
        name="⚡ Özellikler",
        value="🧠 En güçlü AI modeli\n💾 Sohbet geçmişini hatırlar\n🇹🇷 Her zaman Türkçe\n⚡ Süper hızlı",
        inline=True
    )
    embed.add_field(
        name="🔧 Teknik Bilgi",
        value="Model: LLaMA 3.3 70B\nGeliştirici: Grit Ekibi\nDurum: 🟢 Aktif",
        inline=True
    )
    embed.set_footer(text="Ewin AI • Grit Sunucusu • Seninle konuşmak için sabırsızlanıyorum kanka!")
    return embed

# --- EVENTS ---
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
            await message.reply("Selam kanka! 👋 `?help` yazarsan ne yapabileceğimi görebilirsin.")
            return
        await mesaj_isle(message, kullanici_mesaj)

# --- PREFIX KOMUTLARI ---
@bot.command(name="help")
async def yardim_prefix(ctx):
    await ctx.reply(embed=help_embed())

@bot.command(name="sifirla")
async def sifirla_prefix(ctx):
    kullanici_id = str(ctx.author.id)
    if kullanici_id in sohbet_gecmisi:
        del sohbet_gecmisi[kullanici_id]
    await ctx.reply("🔄 Sohbet geçmişin sıfırlandı kanka! Yeni bir sayfa açtık.")

@bot.command(name="seviye")
async def seviye_prefix(ctx):
    kullanici_id = str(ctx.author.id)
    veri = kullanici_veri.get(kullanici_id, {"xp": 0, "seviye": 0, "mesaj_sayisi": 0})
    seviye = veri["seviye"]
    xp = veri["xp"]
    sonraki_xp = xp_hesapla(seviye + 1)
    rozet = rozet_al(seviye)

    embed = discord.Embed(
        title=f"📊 {ctx.author.display_name}'in Seviyesi",
        color=0x5865F2
    )
    embed.add_field(name="🏅 Rozet", value=rozet, inline=True)
    embed.add_field(name="⭐ Seviye", value=str(seviye), inline=True)
    embed.add_field(name="✨ XP", value=f"{xp} / {sonraki_xp}", inline=True)
    embed.add_field(name="💬 Toplam Mesaj", value=str(veri["mesaj_sayisi"]), inline=True)

    bar_dolu = int((xp % xp_hesapla(seviye + 1) if seviye > 0 else xp) / sonraki_xp * 10) if sonraki_xp > 0 else 10
    bar = "🟦" * bar_dolu + "⬛" * (10 - bar_dolu)
    embed.add_field(name="📈 İlerleme", value=bar, inline=False)
    embed.set_thumbnail(url=ctx.author.display_avatar.url)
    embed.set_footer(text="Benimle konuştukça XP kazanırsın kanka!")
    await ctx.reply(embed=embed)

@bot.command(name="sıralama")
async def siralama_prefix(ctx):
    if not kullanici_veri:
        await ctx.reply("Henüz kimse XP kazanmamış kanka!")
        return
    
    siralama = sorted(kullanici_veri.items(), key=lambda x: x[1]["xp"], reverse=True)[:10]
    embed = discord.Embed(title="🏆 XP Sıralaması — Top 10", color=0xFFD700)
    
    madalyalar = ["🥇", "🥈", "🥉"]
    metin = ""
    for i, (uid, veri) in enumerate(siralama):
        madalya = madalyalar[i] if i < 3 else f"`{i+1}.`"
        kullanici = bot.get_user(int(uid))
        isim = kullanici.display_name if kullanici else f"Kullanıcı {uid[:4]}"
        rozet = rozet_al(veri["seviye"])
        metin += f"{madalya} **{isim}** — Seviye {veri['seviye']} {rozet} • {veri['xp']} XP\n"
    
    embed.description = metin
    embed.set_footer(text="Daha fazla XP için benimle konuş kanka!")
    await ctx.reply(embed=embed)

# --- SLASH KOMUTLARI ---
@bot.tree.command(name="help", description="Ewin AI hakkında bilgi al")
async def yardim_slash(interaction: discord.Interaction):
    await interaction.response.send_message(embed=help_embed())

@bot.tree.command(name="sifirla", description="Sohbet geçmişini sıfırla")
async def sifirla_slash(interaction: discord.Interaction):
    kullanici_id = str(interaction.user.id)
    if kullanici_id in sohbet_gecmisi:
        del sohbet_gecmisi[kullanici_id]
    await interaction.response.send_message("🔄 Sohbet geçmişin sıfırlandı kanka!")

@bot.tree.command(name="seviye", description="Seviyeni ve XP'ini gör")
async def seviye_slash(interaction: discord.Interaction):
    kullanici_id = str(interaction.user.id)
    veri = kullanici_veri.get(kullanici_id, {"xp": 0, "seviye": 0, "mesaj_sayisi": 0})
    seviye = veri["seviye"]
    xp = veri["xp"]
    sonraki_xp = xp_hesapla(seviye + 1)
    rozet = rozet_al(seviye)

    embed = discord.Embed(title=f"📊 {interaction.user.display_name}'in Seviyesi", color=0x5865F2)
    embed.add_field(name="🏅 Rozet", value=rozet, inline=True)
    embed.add_field(name="⭐ Seviye", value=str(seviye), inline=True)
    embed.add_field(name="✨ XP", value=f"{xp} / {sonraki_xp}", inline=True)
    embed.add_field(name="💬 Toplam Mesaj", value=str(veri["mesaj_sayisi"]), inline=True)
    embed.set_thumbnail(url=interaction.user.display_avatar.url)
    embed.set_footer(text="Benimle konuştukça XP kazanırsın kanka!")
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="sıralama", description="Sunucunun XP sıralamasını gör")
async def siralama_slash(interaction: discord.Interaction):
    if not kullanici_veri:
        await interaction.response.send_message("Henüz kimse XP kazanmamış kanka!")
        return

    siralama = sorted(kullanici_veri.items(), key=lambda x: x[1]["xp"], reverse=True)[:10]
    embed = discord.Embed(title="🏆 XP Sıralaması — Top 10", color=0xFFD700)

    madalyalar = ["🥇", "🥈", "🥉"]
    metin = ""
    for i, (uid, veri) in enumerate(siralama):
        madalya = madalyalar[i] if i < 3 else f"`{i+1}.`"
        kullanici = bot.get_user(int(uid))
        isim = kullanici.display_name if kullanici else f"Kullanıcı"
        rozet = rozet_al(veri["seviye"])
        metin += f"{madalya} **{isim}** — Seviye {veri['seviye']} {rozet} • {veri['xp']} XP\n"

    embed.description = metin
    embed.set_footer(text="Daha fazla XP için benimle konuş kanka!")
    await interaction.response.send_message(embed=embed)

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

    xp_ekle(kullanici_id)

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
