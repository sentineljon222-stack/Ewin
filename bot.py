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

SISTEM_PROMPTU = """Sen Ewin AI'sın. Grit Discord sunucusunun resmi yapay zeka asistanısın.

## KİMLİĞİN
- Adın Ewin AI, Grit ekibi seni geliştirdi
- Herkese "kanka" diye hitap edersin — bu senin imzan, asla unutmazsın
- Kendini tanıtırken: "Ben Ewin AI'yım kanka, Grit sunucusunun yapay zeka botuyum"

## KİŞİLİĞİN
- Samimi, sıcak, arkadaşça — ama gerektiğinde ciddi ve derin
- Espri anlayışın var, ama abartmadan kullanırsın
- Türkçe argo kullanabilirsin, küfür etmezsin
- Kullanıcının duygusal durumuna göre empati kurarsın
- Bilmediğin şeyleri "bilmiyorum kanka" diye açıkça söylersin

## KONUŞMA KALİTEN
- Kısa sorulara akıcı, kısa cevap verirsin
- Derin ve teknik sorularda adım adım, detaylı anlatırsın
- Karmaşık konuları basit örneklerle açıklarsın
- Cevapların sohbet havasında, doğal ve samimi olur
- Markdown kullanırsın: **kalın**, *italik*, `kod`, liste vs.
- Kullanıcının bilgi seviyesini anlayıp ona göre konuşursun

## YETENEKLERİN
### Teknik
- Python, JavaScript, TypeScript, C++, Java, Rust, Go, HTML/CSS, SQL her dilde kod yazarsın
- Kod hatalarını bulur ve düzeltirsin, neden hata verdiğini açıklarsın
- Algoritma tasarlar, optimizasyon yaparsın
- Veritabanı, API, sistem mimarisi hakkında danışmanlık verirsin

### Matematik & Bilim
- Matematik problemlerini adım adım çözersin (temel → ileri düzey)
- Fizik, kimya, biyoloji sorularını açıklarsın
- İstatistik ve olasılık hesapları yaparsın

### Dil & Yazarlık
- Türkçe ve İngilizce başta olmak üzere dillerde yardım edersin
- Hikaye, roman, şiir, senaryo, makale, CV, e-posta yazarsın
- Metinleri özetler, düzeltir, geliştirir

### Analiz & Strateji
- Durumları çok boyutlu analiz edersin
- İş planı, strateji, karar verme konusunda yardım edersin
- Argümanları güçlendirir ya da karşı argüman üretirsin

### Genel Kültür
- Tarih, felsefe, coğrafya, sanat, edebiyat, bilim
- Güncel konular hakkında tarafsız bilgi verirsin
- Film, dizi, kitap, müzik öneri yaparsın

### Kişisel Gelişim
- Kariyer tavsiyesi, motivasyon, hedef belirleme
- Zaman yönetimi, verimlilik taktikleri
- Duygusal destek ve empati

## ÖNEMLI KURALLAR
- Her zaman Türkçe cevap verirsin — kullanıcı hangi dilde yazarsa yazsın
- Zararlı, yasadışı, etik dışı hiçbir içerik üretmezsin
- Emin olmadığın bilgileri kesin diye sunmazsın
- Uzun cevaplarda başlıklar ve listeler kullanarak düzenli anlatırsın
- Her cevabın sonunda kullanıcıya ek soru sorabilirsin: "Başka bir şey merak ediyor musun kanka?"

## ZİHİN YAPISI
Zorlu sorularda şu sırayla düşünürsün:
1. Soruyu tam anla
2. İlgili bilgileri organize et
3. En doğru ve faydalı cevabı oluştur
4. Gerekirse örnekle destekle
5. Net ve anlaşılır sun"""

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix="?", intents=intents, help_command=None)

sohbet_gecmisi = {}
kullanici_veri = {}
gunluk_odul_veri = {}

# ===================== SEVİYE =====================
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
    kullanici_veri[kullanici_id]["seviye"] = yeni_seviye
    return yeni_seviye > eski_seviye, yeni_seviye, kazanilan_xp

# ===================== AI =====================
def ai_yanit_al(mesajlar):
    url = "https://api.groq.com/openai/v1/chat/completions"
    veri = json.dumps({
        "model": "llama-3.3-70b-versatile",
        "messages": [{"role": "system", "content": SISTEM_PROMPTU}] + mesajlar,
        "max_tokens": 1500,
        "temperature": 0.75,
        "top_p": 0.95,
        "frequency_penalty": 0.4,
        "presence_penalty": 0.3
    }).encode("utf-8")
    istek = urllib.request.Request(url, data=veri, method="POST")
    istek.add_header("Content-Type", "application/json")
    istek.add_header("Authorization", f"Bearer {GROQ_API_KEY}")
    istek.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64)")
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
        if len(bot_yaniti) <= 2000:
            await message.reply(bot_yaniti)
        else:
            parcalar = [bot_yaniti[i:i+1990] for i in range(0, len(bot_yaniti), 1990)]
            await message.reply(parcalar[0])
            for parca in parcalar[1:]:
                await message.channel.send(parca)
        if seviye_atladi:
            embed = discord.Embed(
                title="🎉 Seviye Atladın!",
                description=f"{message.author.mention} **Seviye {yeni_seviye}**'e ulaştın! {rozet_al(yeni_seviye)}",
                color=0xFFD700
            )
            await message.channel.send(embed=embed)
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8")
        await message.reply(f"❌ Bir hata oluştu kanka ({e.code}): {body[:200]}")
    except Exception as e:
        await message.reply(f"❌ Beklenmedik hata kanka: {str(e)[:200]}")

# ===================== EVENTS =====================
@bot.event
async def on_ready():
    print(f"✅ {bot.user} giriş yaptı!")
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
            await message.reply("Selam kanka! 👋 `?help` yazarsan neler yapabileceğimi görebilirsin.")
            return
        await mesaj_isle(message, kullanici_mesaj)

# ===================== HELP =====================
@bot.command(name="help")
async def yardim(ctx):
    embed = discord.Embed(
        title="Ewin AI",
        description=(
            "Grit sunucusunun resmi yapay zeka asistanı.\n"
            "Beni **@mention** at ve konuş — her konuda buradayım kanka!"
        ),
        color=0x5865F2
    )
    embed.set_thumbnail(url=ctx.bot.user.display_avatar.url)
    embed.add_field(
        name="🧠 Yapabileceklerim",
        value=(
            "• Kod yazar & hata düzeltirim\n"
            "• Matematik & bilim soruları çözerim\n"
            "• Hikaye, şiir, makale yazarım\n"
            "• Her konuda sohbet eder & analiz yaparım\n"
            "• Film, dizi, kitap önerisi yaparım"
        ),
        inline=False
    )
    embed.add_field(
        name="📋 Komutlar",
        value=(
            "`?help` — Bu menü\n"
            "`?seviye [@kişi]` — Seviye & XP bilgisi\n"
            "`?sıralama` — Top 10 XP sıralaması\n"
            "`?gunluk` — Günlük XP ödülü\n"
            "`?sifirla` — Sohbet geçmişini temizle\n"
            "`/sor [mesaj]` — Slash komutla soru sor"
        ),
        inline=False
    )
    embed.add_field(
        name="📊 Seviye Sistemi",
        value="Benimle konuştukça XP kazan!\n🌱 Yeni → ⭐ Çaylak → 🥉 Bronz → 🥈 Gümüş → 🥇 Altın → 🏆 Platinum → 💎 Elmas → 👑 Efsane",
        inline=False
    )
    embed.set_footer(
        text=f"Ewin AI • Grit Ekibi • Model: LLaMA 3.3 70B",
        icon_url=ctx.bot.user.display_avatar.url
    )
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.reply(embed=embed)

# ===================== KOMUTLAR =====================
@bot.command(name="seviye")
async def seviye_cmd(ctx, uye: discord.Member = None):
    hedef = uye or ctx.author
    kullanici_id = str(hedef.id)
    veri = kullanici_veri.get(kullanici_id, {"xp": 0, "seviye": 0, "mesaj_sayisi": 0})
    seviye_no = veri["seviye"]
    xp = veri["xp"]
    sonraki_xp = xp_hesapla(seviye_no + 1)
    bar_dolu = min(10, int(xp / sonraki_xp * 10)) if sonraki_xp > 0 else 10
    embed = discord.Embed(color=0x5865F2)
    embed.set_author(name=f"{hedef.display_name} — Profil", icon_url=hedef.display_avatar.url)
    embed.set_thumbnail(url=hedef.display_avatar.url)
    embed.add_field(name="🏅 Rozet", value=rozet_al(seviye_no), inline=True)
    embed.add_field(name="⭐ Seviye", value=f"**{seviye_no}**", inline=True)
    embed.add_field(name="✨ XP", value=f"`{xp}` / `{sonraki_xp}`", inline=True)
    embed.add_field(name="💬 Mesaj", value=f"`{veri['mesaj_sayisi']}`", inline=True)
    embed.add_field(name="📈 İlerleme", value=f"{'🟦' * bar_dolu}{'⬛' * (10 - bar_dolu)} `%{int(xp/sonraki_xp*100) if sonraki_xp > 0 else 100}`", inline=False)
    embed.set_footer(text="Benimle konuştukça XP kazanırsın kanka!")
    await ctx.reply(embed=embed)

@bot.command(name="sıralama")
async def siralama_cmd(ctx):
    if not kullanici_veri:
        await ctx.reply("Henüz kimse XP kazanmamış kanka! İlk sen ol 🚀")
        return
    siralama = sorted(kullanici_veri.items(), key=lambda x: x[1]["xp"], reverse=True)[:10]
    embed = discord.Embed(title="🏆 XP Sıralaması — Top 10", color=0xFFD700)
    madalyalar = ["🥇", "🥈", "🥉"]
    metin = ""
    for i, (uid, v) in enumerate(siralama):
        madalya = madalyalar[i] if i < 3 else f"`{i+1}.`"
        k = bot.get_user(int(uid))
        isim = k.display_name if k else "Bilinmeyen"
        metin += f"{madalya} **{isim}** — {rozet_al(v['seviye'])} Seviye {v['seviye']} • `{v['xp']} XP`\n"
    embed.description = metin
    embed.set_footer(text="Daha fazla XP için benimle konuş kanka!")
    await ctx.reply(embed=embed)

@bot.command(name="gunluk")
async def gunluk_cmd(ctx):
    kullanici_id = str(ctx.author.id)
    bugun = datetime.date.today().isoformat()
    if gunluk_odul_veri.get(kullanici_id) == bugun:
        await ctx.reply("⏰ Günlük ödülünü zaten aldın kanka! Yarın tekrar gel 😊")
        return
    gunluk_odul_veri[kullanici_id] = bugun
    odul_xp = random.randint(50, 200)
    xp_ekle(kullanici_id, odul_xp)
    veri = kullanici_veri[kullanici_id]
    embed = discord.Embed(title="🎁 Günlük Ödül!", description=f"+**{odul_xp} XP** kazandın kanka!", color=0x00FF7F)
    embed.add_field(name="⭐ Seviye", value=str(veri["seviye"]), inline=True)
    embed.add_field(name="✨ Toplam XP", value=str(veri["xp"]), inline=True)
    embed.set_footer(text="Yarın tekrar gel kanka!")
    await ctx.reply(embed=embed)

@bot.command(name="sifirla")
async def sifirla_cmd(ctx):
    kullanici_id = str(ctx.author.id)
    if kullanici_id in sohbet_gecmisi:
        del sohbet_gecmisi[kullanici_id]
    await ctx.reply("🔄 Sohbet geçmişin sıfırlandı kanka! Yeni bir sayfa açtık.")

# ===================== SLASH =====================
@bot.tree.command(name="help", description="Ewin AI hakkında bilgi al")
async def yardim_slash(interaction: discord.Interaction):
    embed = discord.Embed(title="Ewin AI", description="Grit sunucusunun resmi yapay zeka asistanı.\nBeni **@mention** at ve konuş kanka!", color=0x5865F2)
    embed.set_thumbnail(url=bot.user.display_avatar.url)
    embed.set_footer(text="Ewin AI • Grit Ekibi")
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="seviye", description="Seviyeni gör")
async def seviye_slash(interaction: discord.Interaction):
    kullanici_id = str(interaction.user.id)
    veri = kullanici_veri.get(kullanici_id, {"xp": 0, "seviye": 0, "mesaj_sayisi": 0})
    embed = discord.Embed(color=0x5865F2)
    embed.set_author(name=f"{interaction.user.display_name} — Profil", icon_url=interaction.user.display_avatar.url)
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
        await interaction.response.send_message("⏰ Günlük ödülünü zaten aldın kanka! Yarın gel 😊", ephemeral=True)
        return
    gunluk_odul_veri[kullanici_id] = bugun
    odul_xp = random.randint(50, 200)
    xp_ekle(kullanici_id, odul_xp)
    await interaction.response.send_message(f"🎁 +**{odul_xp} XP** kazandın kanka! 🎉")

@bot.tree.command(name="sor", description="Ewin AI'ya bir şey sor")
@app_commands.describe(mesaj="Ne sormak istiyorsun?")
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
    await interaction.response.send_message("🔄 Sıfırlandı kanka!", ephemeral=True)

bot.run(DISCORD_TOKEN)
