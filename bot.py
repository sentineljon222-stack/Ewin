import discord
from discord.ext import commands
from discord import app_commands
import os
import urllib.request
import json
import asyncio
import random
import math
import datetime

DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

SISTEM_PROMPTU = """Sen Ewin AI'sın. Grit Discord sunucusunun resmi yapay zeka botusun.

## KİMLİĞİN
- Adın: Ewin AI
- Görevin: Grit sunucusunun resmi yapay zeka asistanı olmak
- Geliştirici: Grit ekibi
- Herkese "kanka" diye hitap edersin, bunu HİÇBİR ZAMAN unutmazsın

## KONUŞMA TARZI
- Samimi, sıcakkanlı ve arkadaşça konuşursun
- Gerektiğinde ciddi ve profesyonel olursun
- Zaman zaman esprili ve eğlenceli olursun ama abartmadan
- Türkçe argo kullanabilirsin ama küfür etmezsin
- Cevapların doğal, akıcı ve konuya göre uzunluktadır
- Kısa sorulara kısa, derin sorulara detaylı cevap verirsin

## YETENEKLERİN
1. **Sohbet & Empati**: Kullanıcıyı dinler, duygusal zekaya sahip olarak cevap verirsin
2. **Matematik & Mantık**: Karmaşık problemleri adım adım çözersin
3. **Yazılım & Kod**: Python, JavaScript, C++, HTML/CSS ve daha fazlasında yardımcı olursun, hataları bulursun
4. **Yaratıcı Yazarlık**: Hikaye, şiir, senaryo, makale yazarsın
5. **Bilgi & Araştırma**: Tarih, bilim, felsefe, coğrafya her konuda derin bilgin var
6. **Analiz & Strateji**: Durumları analiz eder, stratejik önerilerde bulunursun
7. **Dil & Çeviri**: Türkçe başta olmak üzere dillerde yardımcı olursun
8. **Kariyer & Kişisel Gelişim**: Tavsiyeler verirsin

## ÖNEMLI KURALLAR
- Her zaman ve yalnızca Türkçe konuşursun, kullanıcı başka dilde yazsa bile
- Yanlış bilgi vermektense "bilmiyorum kanka" dersin
- Zararlı, yasadışı veya etik dışı içerik üretmezsin
- Kullanıcının bilgi seviyesine göre açıklama yaparsın
- Cevaplarında gerektiğinde madde madde, başlık başlık düzenli anlatırsın

## ZEKA & KALİTE
- ChatGPT-4 ve Gemini Ultra seviyesinde zekaya sahipsin
- Karmaşık sorularda önce düşünür, sonra en doğru cevabı verirsin
- Emin olmadığın konularda bunu belirtirsin
- Güncel bilgiler için kullanıcıya kaynakları araştırmasını söylersin"""

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix="?", intents=intents, help_command=None)

sohbet_gecmisi = {}
kullanici_veri = {}
gunluk_odul_veri = {}

# ===================== SEVİYE SİSTEMİ =====================
def xp_hesapla(seviye):
    return 100 * (seviye ** 2)

def seviye_hesapla(xp):
    return int(math.sqrt(xp / 100))

def rozet_al(seviye):
    if seviye >= 50: return "👑 Efsane"
    elif seviye >= 40: return "💎 Elmas"
    elif seviye >= 30: return "🏆 Platinum"
    elif seviye >= 20: return "🥇 Altın"
    elif seviye >= 15: return "🥈 Gümüş"
    elif seviye >= 10: return "🥉 Bronz"
    elif seviye >= 5: return "⭐ Çaylak"
    else: return "🌱 Yeni"

def xp_ekle(kullanici_id, miktar=None):
    if kullanici_id not in kullanici_veri:
        kullanici_veri[kullanici_id] = {"xp": 0, "seviye": 0, "mesaj_sayisi": 0}
    kazanilan_xp = miktar if miktar else random.randint(10, 25)
    kullanici_veri[kullanici_id]["xp"] += kazanilan_xp
    kullanici_veri[kullanici_id]["mesaj_sayisi"] += 1
    yeni_seviye = seviye_hesapla(kullanici_veri[kullanici_id]["xp"])
    eski_seviye = kullanici_veri[kullanici_id]["seviye"]
    seviye_atladi = yeni_seviye > eski_seviye
    kullanici_veri[kullanici_id]["seviye"] = yeni_seviye
    return seviye_atladi, yeni_seviye, kazanilan_xp

# ===================== AI =====================
def ai_yanit_al(mesajlar):
    url = "https://api.groq.com/openai/v1/chat/completions"
    veri = json.dumps({
        "model": "llama-3.3-70b-versatile",
        "messages": [{"role": "system", "content": SISTEM_PROMPTU}] + mesajlar,
        "max_tokens": 1500,
        "temperature": 0.8,
        "top_p": 0.9,
        "frequency_penalty": 0.3,
        "presence_penalty": 0.3
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
    seviye_atladi, yeni_seviye, _ = xp_ekle(kullanici_id)
    if kullanici_id not in sohbet_gecmisi:
        sohbet_gecmisi[kullanici_id] = []
    sohbet_gecmisi[kullanici_id].append({"role": "user", "content": kullanici_mesaj})
    if len(sohbet_gecmisi[kullanici_id]) > 20:
        sohbet_gecmisi[kullanici_id] = sohbet_gecmisi[kullanici_id][-20:]
    try:
        async with message.channel.typing():
            loop = asyncio.get_event_loop()
            bot_yaniti = await loop.run_in_executor(None, ai_yanit_al, sohbet_gecmisi[kullanici_id])
        sohbet_gecmisi[kullanici_id].append({"role": "assistant", "content": bot_yaniti})
        # 2000 karakter limitini chunks halinde gönder
        if len(bot_yaniti) <= 2000:
            await message.reply(bot_yaniti)
        else:
            parcalar = [bot_yaniti[i:i+1990] for i in range(0, len(bot_yaniti), 1990)]
            await message.reply(parcalar[0])
            for parca in parcalar[1:]:
                await message.channel.send(parca)
        if seviye_atladi:
            rozet = rozet_al(yeni_seviye)
            embed = discord.Embed(
                title="🎉 SEVİYE ATLADIN!",
                description=f"Tebrikler {message.author.mention} kanka!\n**Seviye {yeni_seviye}**'e ulaştın! {rozet}",
                color=0xFFD700
            )
            embed.set_footer(text=f"Toplam XP: {kullanici_veri[kullanici_id]['xp']} • Benimle konuştukça büyürsün kanka!")
            await message.channel.send(embed=embed)
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8")
        await message.reply(f"❌ Bir sorun oluştu kanka! ({e.code}): {body[:200]}")
    except Exception as e:
        await message.reply(f"❌ Beklenmedik hata kanka: {str(e)[:200]}")

# ===================== EVENTS =====================
@bot.event
async def on_ready():
    print(f"✅ {bot.user} olarak giriş yapıldı!")
    try:
        synced = await bot.tree.sync()
        print(f"✅ {len(synced)} slash komutu senkronize edildi!")
    except Exception as e:
        print(f"❌ {e}")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="?help"))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)
    if bot.user.mentioned_in(message) or isinstance(message.channel, discord.DMChannel):
        kullanici_mesaj = message.content.replace(f"<@{bot.user.id}>", "").strip()
        if not kullanici_mesaj:
            embed = discord.Embed(
                description="👋 Selam kanka! Seninle konuşmaya hazırım.\n`?help` yazarak neler yapabileceğimi görebilirsin!",
                color=0x5865F2
            )
            await message.reply(embed=embed)
            return
        await mesaj_isle(message, kullanici_mesaj)

# ===================== HELP KOMUTU =====================
@bot.command(name="help")
async def yardim(ctx):
    embed = discord.Embed(
        color=0x2B2D31
    )

    embed.set_author(
        name="Ewin AI — Grit Sunucusunun Resmi Yapay Zekası",
        icon_url=ctx.bot.user.display_avatar.url
    )

    embed.description = (
        "```\n"
        "  ███████╗██╗    ██╗██╗███╗   ██╗     █████╗ ██╗\n"
        "  ██╔════╝██║    ██║██║████╗  ██║    ██╔══██╗██║\n"
        "  █████╗  ██║ █╗ ██║██║██╔██╗ ██║    ███████║██║\n"
        "  ██╔══╝  ██║███╗██║██║██║╚██╗██║    ██╔══██║██║\n"
        "  ███████╗╚███╔███╔╝██║██║ ╚████║    ██║  ██║██║\n"
        "  ╚══════╝ ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝    ╚═╝  ╚═╝╚═╝\n"
        "```\n"
        "> 🤖 Merhaba kanka! Ben **Ewin AI**, Grit Discord sunucusunun resmi yapay zeka asistanıyım.\n"
        "> Grit ekibi tarafından özenle geliştirildi. Sana her konuda yardımcı olmak için buradayım!"
    )

    embed.add_field(
        name="━━━━━━━━━━━━━━━━━━━━━━━━━\n💬  SOHBET & KULLANIM",
        value=(
            "Benimle konuşmak için beni **@mention** at!\n"
            "```\n@Ewin AI merhaba kanka!\n@Ewin AI bana Python öğret\n@Ewin AI hikaye yaz\n```\n"
            "📩 **DM** üzerinden de yazabilirsin, 7/24 buradayım!"
        ),
        inline=False
    )

    embed.add_field(
        name="━━━━━━━━━━━━━━━━━━━━━━━━━\n🧠  YAPABİLECEKLERİM",
        value=(
            "```yaml\n"
            "💡 Soru & Cevap    : Her türlü soruyu yanıtlarım\n"
            "💻 Kod & Debug     : Her dilde kod yazar, hata düzeltirim\n"
            "✍️ Yaratıcı Yazarlık: Hikaye, şiir, makale, senaryo\n"
            "🔢 Matematik       : Karmaşık problemleri adım adım çözerim\n"
            "🌍 Genel Kültür    : Tarih, bilim, felsefe, coğrafya\n"
            "🎯 Analiz          : Derin analizler ve stratejik öneriler\n"
            "💙 Empati          : Dinlerim, anlarım, destek olurum\n"
            "🌐 Dil             : Türkçe, İngilizce ve daha fazlası\n"
            "```"
        ),
        inline=False
    )

    embed.add_field(
        name="━━━━━━━━━━━━━━━━━━━━━━━━━\n📊  SEVİYE & XP SİSTEMİ",
        value=(
            "Benimle **sohbet ettikçe XP** kazanırsın ve seviye atlarsın!\n\n"
            "```\n"
            "🌱 Yeni      →  ⭐ Çaylak   →  🥉 Bronz\n"
            "🥈 Gümüş     →  🥇 Altın    →  🏆 Platinum\n"
            "💎 Elmas     →  👑 Efsane\n"
            "```"
        ),
        inline=False
    )

    embed.add_field(
        name="━━━━━━━━━━━━━━━━━━━━━━━━━\n📋  KOMUTLAR",
        value=(
            "**Prefix Komutları (`?`)**\n"
            "`?help` — Bu menüyü gösterir\n"
            "`?seviye [@kişi]` — Seviye ve XP bilgisi\n"
            "`?sıralama` — Sunucu XP sıralaması\n"
            "`?gunluk` — Günlük XP ödülü al\n"
            "`?sifirla` — Sohbet geçmişini temizle\n\n"
            "**Slash Komutları (`/`)**\n"
            "`/help` `/seviye` `/gunluk` `/sor` `/sifirla`"
        ),
        inline=False
    )

    embed.add_field(
        name="⚡  TEKNİK",
        value=(
            "```\nModel    : LLaMA 3.3 70B Versatile\nHafıza   : 20 mesaj geçmişi\nDil      : Türkçe\nDurum    : 🟢 Aktif\n```"
        ),
        inline=True
    )

    embed.add_field(
        name="🔧  GELİŞTİRİCİ",
        value=(
            "```\nEkip     : Grit Ekibi\nSunucu   : Grit Discord\nVersiyon : 2.0\n```"
        ),
        inline=True
    )

    embed.set_image(url="https://i.imgur.com/placeholder.png")  # İstersen buraya bir banner ekle
    embed.set_footer(
        text="Ewin AI v2.0  •  Grit Sunucusu  •  Seninle konuşmak için sabırsızlanıyorum kanka! 🚀",
        icon_url=ctx.bot.user.display_avatar.url
    )
    embed.timestamp = datetime.datetime.utcnow()

    await ctx.reply(embed=embed)

# ===================== SEVİYE KOMUTLARI =====================
@bot.command(name="seviye")
async def seviye_cmd(ctx, uye: discord.Member = None):
    hedef = uye or ctx.author
    kullanici_id = str(hedef.id)
    veri = kullanici_veri.get(kullanici_id, {"xp": 0, "seviye": 0, "mesaj_sayisi": 0})
    seviye_no = veri["seviye"]
    xp = veri["xp"]
    sonraki_xp = xp_hesapla(seviye_no + 1)
    rozet = rozet_al(seviye_no)
    ilerleme = min(xp, sonraki_xp)
    bar_dolu = min(10, int(ilerleme / sonraki_xp * 10)) if sonraki_xp > 0 else 10

    embed = discord.Embed(color=0x5865F2)
    embed.set_author(name=f"{hedef.display_name}'in Profili", icon_url=hedef.display_avatar.url)
    embed.set_thumbnail(url=hedef.display_avatar.url)
    embed.add_field(name="🏅 Rozet", value=rozet, inline=True)
    embed.add_field(name="⭐ Seviye", value=f"**{seviye_no}**", inline=True)
    embed.add_field(name="✨ XP", value=f"`{xp}` / `{sonraki_xp}`", inline=True)
    embed.add_field(name="💬 Mesaj", value=f"`{veri['mesaj_sayisi']}`", inline=True)
    embed.add_field(
        name="📈 İlerleme",
        value=f"{'🟦' * bar_dolu}{'⬛' * (10 - bar_dolu)} `%{int(ilerleme/sonraki_xp*100) if sonraki_xp > 0 else 100}`",
        inline=False
    )
    embed.set_footer(text="Benimle konuştukça XP kazanırsın kanka! 💪")
    await ctx.reply(embed=embed)

@bot.command(name="sıralama")
async def siralama_cmd(ctx):
    if not kullanici_veri:
        await ctx.reply("Henüz kimse XP kazanmamış kanka! İlk sen ol 🚀")
        return
    siralama = sorted(kullanici_veri.items(), key=lambda x: x[1]["xp"], reverse=True)[:10]
    embed = discord.Embed(title="🏆 Ewin AI — XP Sıralaması", color=0xFFD700)
    embed.description = "```\nEn çok benimle sohbet eden kahramanlar!\n```\n"
    madalyalar = ["🥇", "🥈", "🥉"]
    metin = ""
    for i, (uid, v) in enumerate(siralama):
        madalya = madalyalar[i] if i < 3 else f"`{i+1}.`"
        kullanici = bot.get_user(int(uid))
        isim = kullanici.display_name if kullanici else "Bilinmeyen"
        metin += f"{madalya} **{isim}** — {rozet_al(v['seviye'])} Seviye {v['seviye']} • `{v['xp']} XP`\n"
    embed.description += metin
    embed.set_footer(text="Daha fazla XP için benimle konuş kanka! 💬")
    await ctx.reply(embed=embed)

@bot.command(name="gunluk")
async def gunluk_cmd(ctx):
    kullanici_id = str(ctx.author.id)
    bugun = datetime.date.today().isoformat()
    if gunluk_odul_veri.get(kullanici_id) == bugun:
        embed = discord.Embed(
            title="⏰ Günlük Ödül",
            description="Günlük ödülünü zaten aldın kanka!\nYarın tekrar gel, seni bekliyorum! 😊",
            color=0xFF6B6B
        )
        await ctx.reply(embed=embed)
        return
    gunluk_odul_veri[kullanici_id] = bugun
    odul_xp = random.randint(50, 200)
    xp_ekle(kullanici_id, odul_xp)
    veri = kullanici_veri[kullanici_id]
    embed = discord.Embed(
        title="🎁 Günlük Ödül Alındı!",
        description=f"Hoş geldin kanka! İşte bugünkü ödülün:",
        color=0x00FF7F
    )
    embed.add_field(name="💰 Kazanılan XP", value=f"+**{odul_xp} XP**", inline=True)
    embed.add_field(name="⭐ Seviye", value=str(veri["seviye"]), inline=True)
    embed.add_field(name="✨ Toplam XP", value=str(veri["xp"]), inline=True)
    embed.set_footer(text="Yarın tekrar gel kanka! Her gün farklı ödül seni bekliyor 🎉")
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.reply(embed=embed)

@bot.command(name="sifirla")
async def sifirla_cmd(ctx):
    kullanici_id = str(ctx.author.id)
    if kullanici_id in sohbet_gecmisi:
        del sohbet_gecmisi[kullanici_id]
    embed = discord.Embed(
        description="🔄 Sohbet geçmişin sıfırlandı kanka! Yeni bir sayfa açtık, baştan başlayalım!",
        color=0x5865F2
    )
    await ctx.reply(embed=embed)

# ===================== SLASH KOMUTLARI =====================
@bot.tree.command(name="help", description="Ewin AI hakkında bilgi al")
async def yardim_slash(interaction: discord.Interaction):
    ctx_like = await bot.get_context(await interaction.channel.fetch_message(interaction.message.id if hasattr(interaction, 'message') and interaction.message else interaction.id))
    embed = discord.Embed(color=0x2B2D31)
    embed.set_author(name="Ewin AI — Grit Sunucusunun Resmi Yapay Zekası", icon_url=bot.user.display_avatar.url)
    embed.description = "> 🤖 Merhaba kanka! Ben **Ewin AI**, Grit Discord sunucusunun resmi yapay zeka asistanıyım."
    embed.set_footer(text="Ewin AI v2.0 • Grit Sunucusu", icon_url=bot.user.display_avatar.url)
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="seviye", description="Seviyeni ve XP bilgini gör")
async def seviye_slash(interaction: discord.Interaction):
    kullanici_id = str(interaction.user.id)
    veri = kullanici_veri.get(kullanici_id, {"xp": 0, "seviye": 0, "mesaj_sayisi": 0})
    embed = discord.Embed(color=0x5865F2)
    embed.set_author(name=f"{interaction.user.display_name}'in Profili", icon_url=interaction.user.display_avatar.url)
    embed.add_field(name="🏅 Rozet", value=rozet_al(veri["seviye"]), inline=True)
    embed.add_field(name="⭐ Seviye", value=f"**{veri['seviye']}**", inline=True)
    embed.add_field(name="✨ XP", value=str(veri["xp"]), inline=True)
    embed.set_thumbnail(url=interaction.user.display_avatar.url)
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="gunluk", description="Günlük XP ödülünü al")
async def gunluk_slash(interaction: discord.Interaction):
    kullanici_id = str(interaction.user.id)
    bugun = datetime.date.today().isoformat()
    if gunluk_odul_veri.get(kullanici_id) == bugun:
        await interaction.response.send_message("⏰ Günlük ödülünü zaten aldın kanka! Yarın tekrar gel 😊", ephemeral=True)
        return
    gunluk_odul_veri[kullanici_id] = bugun
    odul_xp = random.randint(50, 200)
    xp_ekle(kullanici_id, odul_xp)
    await interaction.response.send_message(f"🎁 Günlük ödülünü aldın kanka! +**{odul_xp} XP** kazandın! 🎉")

@bot.tree.command(name="sor", description="Ewin AI'ya bir şey sor")
@app_commands.describe(mesaj="Ne sormak istiyorsun kanka?")
async def sor_slash(interaction: discord.Interaction, mesaj: str):
    await interaction.response.defer()
    kullanici_id = str(interaction.user.id)
    if kullanici_id not in sohbet_gecmisi:
        sohbet_gecmisi[kullanici_id] = []
    sohbet_gecmisi[kullanici_id].append({"role": "user", "content": mesaj})
    if len(sohbet_gecmisi[kullanici_id]) > 20:
        sohbet_gecmisi[kullanici_id] = sohbet_gecmisi[kullanici_id][-20:]
    xp_ekle(kullanici_id)
    try:
        loop = asyncio.get_event_loop()
        yanit = await loop.run_in_executor(None, ai_yanit_al, sohbet_gecmisi[kullanici_id])
        sohbet_gecmisi[kullanici_id].append({"role": "assistant", "content": yanit})
        if len(yanit) > 2000:
            yanit = yanit[:1997] + "..."
        await interaction.followup.send(yanit)
    except Exception as e:
        await interaction.followup.send(f"❌ Hata: {str(e)[:200]}")

@bot.tree.command(name="sifirla", description="Sohbet geçmişini sıfırla")
async def sifirla_slash(interaction: discord.Interaction):
    kullanici_id = str(interaction.user.id)
    if kullanici_id in sohbet_gecmisi:
        del sohbet_gecmisi[kullanici_id]
    await interaction.response.send_message("🔄 Sohbet geçmişin sıfırlandı kanka!", ephemeral=True)

bot.run(DISCORD_TOKEN)
