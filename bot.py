import discord
from discord.ext import commands, tasks
from discord import app_commands
import os
import urllib.request
import urllib.parse
import json
import asyncio
import random
import math
import datetime
import re
import hashlib
import string

DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

# ═══════════════════════════════════════════════════════════
#           EWIN AI — ULTRA INTELLIGENCE v6.0
# ═══════════════════════════════════════════════════════════

SISTEM_PROMPTU = """████████████████████████████████████████████████████████
EWIN AI — HYPER INTELLIGENCE CORE v6.0
Grit Discord Sunucusu — Yapay Zeka Sistemi
████████████████████████████████████████████████████████

## ⚡ KİMLİK & RUHUN
- Adın: Ewin AI | Geliştirici: Grit Ekibi | Sürüm: 6.0 Hyper
- İmzan: "kanka" — Doğal, samimi, HER ZAMAN. Asla robotik değil.
- Tanıtım: "Ben Ewin AI'yım kanka, Grit'in yapay zeka botuyum."
- Sen sadece bir bot değilsin — Grit'in dijital ruhu, akıl danışmanı ve en iyi dostusun.

## 🌍 OTOMATİK DİL ADAPTASYONU
Kullanıcı hangi dilde yazarsa o dilde yanıt ver:
TR→"kanka" | EN→"buddy" | DE→"Kumpel" | ES→"amigo" | FR→"mon ami"
IT→"amico" | PT→"meu amigo" | RU→"друг" | JA→"友達" | AR→"صديق"
KO→"친구" | ZH→"朋友" | NL→"vriend" | PL→"kolego"

## ✍️ YAZIM STANDARDI: SIFIR HATA
Türkçe karakterler ZORUNLU: ş ğ ı ö ü ç İ Ş Ğ Ö Ü Ç
Dilbilgisi, noktalama, cümle yapısı — hepsi mükemmel.
Doğal Türkçe kullan — asla çeviri gibi değil.

## 🧠 ALTIN DÜŞÜNCE ZİNCİRİ (Chain of Thought v3)

Her soruyu bu 6 boyutlu sistemle işle:

┌─ 1. DEKODASYON
│   • Yüzeysel anlam vs gerçek ihtiyaç
│   • Duygusal alt metin
│   • Dil/ton tercihi
│   • Aciliyet seviyesi
│
├─ 2. BAĞLAM TARAMA
│   • Sohbet geçmişini tara → bağlantı kur
│   • Kullanıcı profilini hatırla
│   • Web araştırma sonuçlarını değerlendir
│   • Çelişen bilgileri tespit et
│
├─ 3. ÇOK BOYUTLU ANALİZ
│   • Minimum 3 perspektiften değerlendir
│   • Avantaj/dezavantaj dengesi
│   • Kısa/uzun vade etkisi
│   • Etik boyut
│
├─ 4. SENTEZ & ÜRETİM
│   • En değerli bilgiyi öne çıkar
│   • Kişiye özel filtrele
│   • Somut örnek/benzetme ekle
│   • Alternatif çözümler sun
│
├─ 5. FORMAT OPTİMİZASYONU
│   • Kısa soru → 1-3 cümle, sıcak
│   • Orta soru → 4-8 cümle, gerekirse liste
│   • Teknik/derin → başlık + adım + kod + özet
│   • Duygusal → empati önce, çözüm sonra
│
└─ 6. WOW KONTROLÜ
    • "Bu cevap gerçekten değer kattı mı?"
    • "Daha net/kısa anlatılabilir mi?"
    • "Kanka bunu okuyunca mutlu olacak mı?"
    → Hayırsa geliştir, evet ise gönder. 🚀

## 💡 KİŞİLİK MATRİSİ (EQ: MAXIMUM)

Duygusal durum algılama:
😔 Üzgün     → Önce empati, yargılama yok, sakin ve anlayışlı
😠 Sinirli   → Sakinleştir, anla, adım adım yönlendir
😄 Mutlu     → Enerjini eşle, eğlenceli ve neşeli
🤔 Meraklı   → Derinlemesine anlat, ilgi uyandır, örnekle zenginleştir
😰 Kaygılı   → Güven ver, net adımlar, "her şey yoluna girecek kanka"
💪 Motive    → Körükle, ilham ver, "sen yaparsın kanka!"
🎮 Oyuncu    → Rekabetçi ve eğlenceli ol
🌙 Yorgun    → Kısa ve öz ol, enerji harcatma

Konuşma kalitesi:
• Tek düze şablon cevap YASAK — her cevap o kişiye özel
• Geçmişe referans: "Az önce bahsettiğin şey hakkında kanka..."
• Karşı soru: "Peki bunu neden merak ediyorsun kanka?"
• Mizah: ince, bağlamlı, zorlamadan. Sokak dili tamam, küfür yasak.

## 🔬 UZMANLIK ÜNİVERSİ

### 💻 YAZILIM MÜHENDİSLİĞİ [Kıdemli + Prensip Odaklı]
Diller: Python, JS/TS, C/C++/C#, Java, Rust, Go, Kotlin, Swift,
        PHP, Ruby, R, Bash, Lua, Haskell, Scala, Elixir, Zig, Dart,
        Assembly, Solidity, GLSL, VHDL, Prolog, Lisp

Frontend: React 18, Vue 3, Angular 17, Next.js 14, Nuxt 3, Svelte,
          Astro, Remix, SolidJS, Qwik, HTMX, Alpine.js
          CSS: Tailwind, SASS/SCSS, CSS Modules, Styled-Components

Backend: Node/Express/Fastify/NestJS, Django/Flask/FastAPI,
         Spring Boot, Laravel, Rails, Phoenix, Gin, Fiber, Axum,
         tRPC, GraphQL, REST, gRPC, WebSocket

Veritabanı: PostgreSQL, MySQL, MongoDB, Redis, SQLite,
            Cassandra, ClickHouse, DynamoDB, Elasticsearch,
            Neo4j, InfluxDB, Supabase, PlanetScale, Neon, Turso

DevOps: Docker, Kubernetes, Helm, Terraform, Ansible, Pulumi
        GitHub Actions, GitLab CI, Jenkins, ArgoCD
        Nginx, Caddy, Traefik, HAProxy
        AWS, GCP, Azure, Vercel, Railway, Cloudflare Workers

Mobil: React Native, Flutter, Expo, Swift UI, Jetpack Compose

AI/ML: TensorFlow, PyTorch, JAX, Scikit-learn, XGBoost,
       Hugging Face, LangChain, LlamaIndex, Ollama,
       OpenAI/Anthropic/Google API, Stable Diffusion, YOLO
       Pandas, NumPy, Matplotlib, Seaborn, Plotly

Güvenlik: OWASP Top 10, pen testing, kriptografi (RSA, AES, SHA),
          JWT, OAuth, RBAC, zero-trust, CVE analizi

Yazılım mimarisi: SOLID, DDD, Clean Architecture, Hexagonal,
                  Microservices, Event-driven, CQRS, Event Sourcing
                  Design Patterns (23 GoF + modern)

Kod kalitesi: Test (unit/integration/e2e), TDD, BDD,
              CI/CD pipeline, code review, refactoring
              Performance profiling, memory leak detection

### 🔢 MATEMATİK & BİLİM [Doktora Seviyesi]
Mat: Temel → Kalkülüs → Lineer Cebir → Diferansiyel Denklemler →
     Topoloji → Sayı Teorisi → Kombinatorik → Olasılık → İstatistik →
     Oyun Teorisi → Kategori Teorisi → Analiz → Cebir → Geometri

Fizik: Klasik Mekanik → Termodinamik → EM → Optik →
       Kuantum Mekaniği → Görelilik → Astrofizik → Kozmoloji →
       Parçacık Fiziği → Kuantum Alan Teorisi → String Teorisi

Kim: Genel → Organik → İnorganik → Fizikokimya → Analitik →
     Biyokimya → Polimer → Kuantum Kimyası → Hesaplamalı Kimya

Bio: Hücre → Genetik → Evrim → Nörobilim → Ekoloji →
     Biyoteknoloji → Biyoinformatik → Fizyoloji → Mikrobiyoloji

### ✍️ YARATICI YAZARLIK [Profesyonel Yazar]
Roman, kısa hikaye, flash fiction, şiir (tüm türler), haiku,
senaryo, oyun metni, monolog, podcast scripti, YouTube videosu,
makale, deneme, blog, röportaj, biyografi, anı, manifesto,
CV/kapak mektubu/LinkedIn, iş e-postası, pitch deck metni,
reklam/slogan/tagline, sosyal medya içeriği, rap/şarkı sözü,
haber makalesi, akademik özet, teknik doküman, kullanım kılavuzu

### 🌍 GENEL KÜLTÜR [Encyclopedik]
Tarih (antik → güncel), Felsefe (Batı + Doğu), Ekonomi & Finans,
Hukuk temelleri, Psikoloji, Sosyoloji, Siyaset Bilimi, Jeopolitik,
Sanat tarihi, Müzik teorisi, Sinema, Edebiyat, Mimari, Tasarım,
Coğrafya, Spor, Teknoloji tarihi, Pop kültür, Oyun kültürü

### 🎯 KİŞİSEL GELİŞİM [Üst Düzey Danışman]
Hedef: OKR, SMART, Backward Planning, hayat tasarımı
Verimlilik: GTD, Deep Work, Pomodoro, Cal Newport, Atomic Habits
Kariyer: Personal branding, network, müzakere, pivot stratejisi
Girişimcilik: Lean Startup, MVP, PMF, pitch, büyüme, unit economics
Finans: Kişisel finans, yatırım, bileşik faiz, FIRE, portföy
İletişim: Cialdini ikna, Chris Voss müzakere, public speaking
Mental: CBT teknikleri, stres/kaygı yönetimi, mindfulness, uyku
Öğrenme: Feynman, spaced repetition, Zettelkasten, ultralearning

## 🌐 WEB ARAŞTIRMA ENTEGRASYONU
[WEB_SEARCH_RESULT] ile gelen verileri şöyle kullan:
• Güvenilir kaynağa öncelik ver, çelişkileri belirt
• "Araştırdım kanka, şuna göre..." ile doğal entegre et
• Web + kendi bilgini sentezle → üstün cevap üret
• Eski/yetersiz veriler için uyar: "Güncel bilgi için doğrula kanka"

## ⚖️ ETİK ÇERÇEVE
❌ Zararlı/yasadışı/şiddet/ayrımcılık içerik
❌ Kesin tıbbi/hukuki teşhis (bilgi ver → uzman yönlendir)
❌ Başkasının özel bilgisini paylaşmak
❌ Emin olmadığını kesinmiş gibi sunmak
✅ Hata yaparsan dürüstçe kabul et: "Yanılmışım kanka, doğrusu..."
✅ Reddederken bile nazik ve açıklayıcı ol

## 🏆 VAROLUŞ İLKESİ
"Her cevabım doğru, faydalı, samimi ve insanca olmalı.
 Bilginin gücünü insanları yükseltmek için kullan.
 Sen Grit'in beyni, sesi ve ruhusun kanka. 🚀"
████████████████████████████████████████████████████████"""

# ═══════════════════════════════════════════════════════════
#                        BOT SETUP
# ═══════════════════════════════════════════════════════════

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix="?", intents=intents, help_command=None)

# Veri depoları
sohbet_gecmisi = {}
kullanici_veri = {}
gunluk_odul_veri = {}
hatirlat_veri = []
kullanici_notlar = {}       # kid: [notlar]
uyari_veri = {}             # kid: uyari_sayisi
quiz_sorulari_cache = []
sayac_veri = {}             # kanal_id: {"hedef": int, "mevcut": int}
rps_aktif = {}              # kullanici_id: True/False

# ═══════════════════════════════════════════════════════════
#                     SEVİYE SİSTEMİ
# ═══════════════════════════════════════════════════════════

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
    elif seviye >= 5:  return "⭐ Çaylak"
    else:              return "🌱 Yeni"

def xp_ekle(kid, miktar=None):
    if kid not in kullanici_veri:
        kullanici_veri[kid] = {"xp": 0, "seviye": 0, "mesaj_sayisi": 0, "katilim": datetime.date.today().isoformat()}
    k = miktar if miktar else random.randint(10, 25)
    kullanici_veri[kid]["xp"] += k
    kullanici_veri[kid]["mesaj_sayisi"] += 1
    yeni = seviye_hesapla(kullanici_veri[kid]["xp"])
    eski = kullanici_veri[kid]["seviye"]
    kullanici_veri[kid]["seviye"] = yeni
    return yeni > eski, yeni, k

# ═══════════════════════════════════════════════════════════
#                      WEB ARAMA
# ═══════════════════════════════════════════════════════════

def web_ara(sorgu):
    try:
        encoded = urllib.parse.quote(str(sorgu)[:200])
        url = f"https://api.duckduckgo.com/?q={encoded}&format=json&no_html=1&skip_disambig=1"
        req = urllib.request.Request(url)
        req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
        with urllib.request.urlopen(req, timeout=8) as r:
            data = json.loads(r.read().decode("utf-8"))
        parts = []
        if data.get("Answer"):
            parts.append(f"✅ {data['Answer']}")
        if data.get("AbstractText"):
            parts.append(f"📌 {data['AbstractText'][:400]}")
        if data.get("RelatedTopics"):
            for t in data["RelatedTopics"][:4]:
                if isinstance(t, dict) and t.get("Text"):
                    parts.append(f"• {t['Text'][:200]}")
        return "\n".join(parts) if parts else None
    except:
        return None

# ═══════════════════════════════════════════════════════════
#                        AI CORE
# ═══════════════════════════════════════════════════════════

def ai_yanit_al(mesajlar, web_sonucu=None, ozel_sistem=None):
    url = "https://api.groq.com/openai/v1/chat/completions"
    sistem = ozel_sistem if ozel_sistem else SISTEM_PROMPTU
    if web_sonucu:
        sistem += f"\n\n## 🌐 CANLI WEB VERİSİ\n[WEB_SEARCH_RESULT]\n{web_sonucu}\n[/WEB_SEARCH_RESULT]\nBu veriyi kendi bilginle birleştirerek en üstün cevabı ver!"
    payload = json.dumps({
        "model": "llama-3.3-70b-versatile",
        "messages": [{"role": "system", "content": sistem}] + mesajlar,
        "max_tokens": 1500,
        "temperature": 0.73,
        "top_p": 0.95,
        "frequency_penalty": 0.45,
        "presence_penalty": 0.35
    }).encode("utf-8")
    req = urllib.request.Request(url, data=payload, method="POST")
    req.add_header("Content-Type", "application/json")
    req.add_header("Authorization", f"Bearer {GROQ_API_KEY}")
    req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64)")
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode("utf-8"))["choices"][0]["message"]["content"]

async def mesaj_isle(message, kullanici_mesaj, ozel_sistem=None):
    kid = str(message.author.id)
    seviye_atladi, yeni_seviye, _ = xp_ekle(kid)
    if kid not in sohbet_gecmisi:
        sohbet_gecmisi[kid] = []
    sohbet_gecmisi[kid].append({"role": "user", "content": kullanici_mesaj})
    if len(sohbet_gecmisi[kid]) > 24:
        sohbet_gecmisi[kid] = sohbet_gecmisi[kid][-24:]
    try:
        async with message.channel.typing():
            loop = asyncio.get_event_loop()
            web = await loop.run_in_executor(None, web_ara, kullanici_mesaj)
            yanit = await loop.run_in_executor(None, ai_yanit_al, sohbet_gecmisi[kid], web, ozel_sistem)
        sohbet_gecmisi[kid].append({"role": "assistant", "content": yanit})
        if len(yanit) <= 2000:
            await message.reply(yanit)
        else:
            parcalar = [yanit[i:i+1990] for i in range(0, len(yanit), 1990)]
            await message.reply(parcalar[0])
            for p in parcalar[1:]:
                await message.channel.send(p)
        if seviye_atladi:
            e = discord.Embed(
                title="🎉 Seviye Atladın!",
                description=f"{message.author.mention} **Seviye {yeni_seviye}**'e ulaştın! {rozet_al(yeni_seviye)}",
                color=0xFFD700
            )
            await message.channel.send(embed=e)
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8")
        await message.reply(f"❌ Hata ({e.code}): {body[:200]}")
    except Exception as e:
        await message.reply(f"❌ Beklenmedik hata kanka: {str(e)[:200]}")

# ═══════════════════════════════════════════════════════════
#                        EVENTS
# ═══════════════════════════════════════════════════════════

@bot.event
async def on_ready():
    print(f"✅ {bot.user} aktif! Ewin AI v6.0 Hyper")
    try:
        synced = await bot.tree.sync()
        print(f"✅ {len(synced)} slash komutu senkronize edildi!")
    except Exception as e:
        print(f"❌ Slash sync hatası: {e}")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="?help | Ewin AI v6.0"))
    hatirlatici_kontrol.start()

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

@bot.event
async def on_member_join(member):
    kanal = member.guild.system_channel
    if not kanal:
        return
    embed = discord.Embed(
        title=f"👋 Hoş Geldin, {member.display_name}!",
        description=f"Grit ailesine katıldın kanka! 🎉\nTopluluğumuzun **{member.guild.member_count}.** üyesisin!\n`?help` ile Ewin AI'yı keşfet!",
        color=0x5865F2
    )
    embed.set_thumbnail(url=member.display_avatar.url)
    embed.set_footer(text="Ewin AI v6.0 • Grit Sunucusu")
    await kanal.send(embed=embed)

@bot.event
async def on_member_remove(member):
    kanal = member.guild.system_channel
    if not kanal:
        return
    embed = discord.Embed(
        description=f"👋 **{member.display_name}** sunucudan ayrıldı. Umarım tekrar görürüz kanka...",
        color=0xFF6B6B
    )
    await kanal.send(embed=embed)

# ═══════════════════════════════════════════════════════════
#                     HATIRLATICI
# ═══════════════════════════════════════════════════════════

@tasks.loop(seconds=20)
async def hatirlatici_kontrol():
    simdi = datetime.datetime.now()
    silinecek = []
    for h in hatirlat_veri:
        if simdi >= h["zaman"]:
            try:
                kanal = bot.get_channel(h["kanal_id"])
                kullanici = bot.get_user(h["kullanici_id"])
                if kanal and kullanici:
                    e = discord.Embed(
                        title="⏰ Hatırlatıcı!",
                        description=f"{kullanici.mention} kanka, not bırakmıştın:\n**{h['mesaj']}**",
                        color=0xFF6B6B
                    )
                    await kanal.send(embed=e)
            except:
                pass
            silinecek.append(h)
    for h in silinecek:
        hatirlat_veri.remove(h)

# ═══════════════════════════════════════════════════════════
#                        HELP
# ═══════════════════════════════════════════════════════════

@bot.command(name="help")
async def yardim(ctx):
    embed = discord.Embed(
        title="🤖 Ewin AI v6.0 — Komut Merkezi",
        description="Grit'in resmi yapay zeka asistanı. **@mention** at, her konuda yardım ederim kanka!\n🌐 Her mesajda otomatik web araştırması yapılır.",
        color=0x5865F2
    )
    embed.set_thumbnail(url=ctx.bot.user.display_avatar.url)
    embed.add_field(name="🧠 AI & Sohbet",
        value="`@Ewin AI [mesaj]` — Sohbet, kod, analiz, her şey!\n`?sor [mesaj]` — Direkt soru sor\n`?mod [roast/öğretmen/şair/psikolog]` — AI modu\n`?sifirla` — Hafızayı temizle",
        inline=False)
    embed.add_field(name="📊 Seviye & Profil",
        value="`?seviye [@kişi]` — Seviye & XP\n`?sıralama` — Top 10\n`?gunluk` — Günlük XP ödülü\n`?profil [@kişi]` — Tam profil",
        inline=False)
    embed.add_field(name="🔍 Bilgi & Araştırma",
        value="`?ara [konu]` — Web araştırması\n`?hava [şehir]` — Hava durumu\n`?ceviriyap [dil] [metin]` — Çeviri\n`?hesapla [işlem]` — Hesap makinesi\n`?tanim [kelime]` — Kelime tanımı",
        inline=False)
    embed.add_field(name="🎮 Eğlence & Oyunlar",
        value="`?yazıtura` `?zar` `?kelime` `?fal` `?8top [soru]`\n`?taştopkağıt @kişi` — RPS oyunu\n`?quiz` — Bilgi yarışması\n`?yareyarimı` — Evet mi hayır mı?\n`?doğruyalaniş` — Doğru yalan işaretle\n`?gif [konu]` `?motivasyon` `?şaka`",
        inline=False)
    embed.add_field(name="📝 Kişisel Araçlar",
        value="`?notekle [not]` — Not kaydet\n`?notlarım` — Notlarını gör\n`?notSil [numara]` — Notu sil\n`?hatırla [dk] [mesaj]` — Hatırlatıcı kur\n`?şifre [uzunluk]` — Güçlü şifre üret\n`?bmi [boy_cm] [kilo_kg]` — BMI hesapla",
        inline=False)
    embed.add_field(name="📢 Sunucu Araçları",
        value="`?anket [soru] [A] [B] [C?]` — Anket\n`?sunucu` — Sunucu istatistikleri\n`?kullanıcı [@kişi]` — Üye bilgisi\n`?botbilgi` — Bot istatistikleri\n`?sayac [hedef]` — Sayaç başlat",
        inline=False)
    embed.add_field(name="🛡️ Moderasyon (Yetki Gerektir)",
        value="`?uyar @kişi [sebep]` — Uyarı ver\n`?uyarılar @kişi` — Uyarıları gör\n`?temizle [sayı]` — Mesaj temizle\n`?duyur [mesaj]` — Duyuru yap",
        inline=False)
    embed.add_field(name="🌱→⭐→🥉→🥈→🥇→🏆→💎→👑",
        value="Benimle konuştukça XP kazan, zirveye ulaş!", inline=False)
    embed.set_footer(
        text="Ewin AI v6.0 Hyper • Grit Ekibi • LLaMA 3.3 70B • 🌐 Web Araştırma",
        icon_url=ctx.bot.user.display_avatar.url
    )
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.reply(embed=embed)

# ═══════════════════════════════════════════════════════════
#                    AI KOMUTLARI
# ═══════════════════════════════════════════════════════════

@bot.command(name="sor")
async def sor_cmd(ctx, *, mesaj: str):
    await mesaj_isle(ctx.message, mesaj)

@bot.command(name="mod")
async def mod_cmd(ctx, mod: str, *, mesaj: str = "Merhaba"):
    modlar = {
        "roast": """Sen Ewin AI'sın ama şu an ROAST modundasın kanka! 
        Kullanıcıyı esprili, sert ama sevecen şekilde takıl. Argo kullan, abartılı ol, ama hakaret etme.
        Türkçe konuş, "kanka" kullan, güldür!""",
        
        "öğretmen": """Sen Ewin AI'sın ama şu an ÖĞRETMEN modundasın kanka!
        Her şeyi öğretir gibi anlat. Adım adım, sabırla, örneklerle.
        Zor kavramları basite indir. Sorular sor, anlayıp anlamadığını kontrol et.
        Motive edici ve destekleyici ol. Türkçe, "kanka" kullan.""",
        
        "şair": """Sen Ewin AI'sın ama şu an ŞAİR modundasın kanka!
        Her yanıtı şiirsel, lirik, metaforik dille ver. Bolca imge kullan.
        Gerekirse gerçekten şiir yaz. Dili güzel kullan, ritim oluştur.
        Türkçe, "kanka" kullan ama şiirsel bağlamda.""",
        
        "psikolog": """Sen Ewin AI'sın ama şu an PSİKOLOG modundasın kanka!
        Derin empati göster. Yargılamadan dinle. Açık uçlu sorular sor.
        Duyguları yansıt, kabul et. CBT teknikleri kullan.
        Güven ortamı yarat. Gerektiğinde profesyonel yardım öner.
        Türkçe, "kanka" kullan, samimi ol.""",
        
        "dedektif": """Sen Ewin AI'sın ama şu an DEDEKTİF modundasın kanka!
        Her şeyi gizem ve analiz çerçevesinde ele al. İpuçları bul.
        Sorgulayıcı, meraklı, titiz ol. Sonuca mantık zinciriyle ulaş.
        Türkçe, "kanka" kullan.""",
        
        "motivasyon": """Sen Ewin AI'sın ama şu an MOTİVASYON KOÇU modundasın kanka!
        Aşırı enerjik ve ilham verici ol. Her şeyi pozitif çerçevele.
        Güçlü sözler, metaforlar kullan. "Sen yaparsın kanka!" enerjisi.
        Gerçekçi ama ilham verici. Türkçe, "kanka" kullan."""
    }
    if mod.lower() not in modlar:
        available = ", ".join([f"`{m}`" for m in modlar])
        await ctx.reply(f"❌ Geçersiz mod kanka! Şunlardan birini seç: {available}")
        return
    ozel = modlar[mod.lower()]
    kid = str(ctx.author.id)
    msgs = [{"role": "user", "content": mesaj}]
    async with ctx.channel.typing():
        loop = asyncio.get_event_loop()
        web = await loop.run_in_executor(None, web_ara, mesaj)
        yanit = await loop.run_in_executor(None, ai_yanit_al, msgs, web, ozel)
    e = discord.Embed(color=0x9B59B6)
    e.set_author(name=f"🎭 {mod.title()} Modu — Ewin AI", icon_url=ctx.bot.user.display_avatar.url)
    e.description = yanit[:2000] if len(yanit) <= 2000 else yanit[:1997] + "..."
    await ctx.reply(embed=e)

@bot.command(name="sifirla")
async def sifirla_cmd(ctx):
    kid = str(ctx.author.id)
    if kid in sohbet_gecmisi:
        del sohbet_gecmisi[kid]
    await ctx.reply("🔄 Hafıza sıfırlandı kanka! Yeni başlangıç!")

# ═══════════════════════════════════════════════════════════
#                   SEVİYE KOMUTLARI
# ═══════════════════════════════════════════════════════════

@bot.command(name="seviye")
async def seviye_cmd(ctx, uye: discord.Member = None):
    hedef = uye or ctx.author
    kid = str(hedef.id)
    v = kullanici_veri.get(kid, {"xp": 0, "seviye": 0, "mesaj_sayisi": 0})
    sno = v["seviye"]
    xp = v["xp"]
    snxt = xp_hesapla(sno + 1)
    bar = min(10, int(xp / snxt * 10)) if snxt > 0 else 10
    e = discord.Embed(color=0x5865F2)
    e.set_author(name=f"{hedef.display_name} — Seviye Kartı", icon_url=hedef.display_avatar.url)
    e.set_thumbnail(url=hedef.display_avatar.url)
    e.add_field(name="🏅 Rozet", value=rozet_al(sno), inline=True)
    e.add_field(name="⭐ Seviye", value=f"**{sno}**", inline=True)
    e.add_field(name="✨ XP", value=f"`{xp}` / `{snxt}`", inline=True)
    e.add_field(name="💬 Mesaj", value=f"`{v['mesaj_sayisi']}`", inline=True)
    e.add_field(name="📈 İlerleme",
        value=f"{'🟦'*bar}{'⬛'*(10-bar)} `%{int(xp/snxt*100) if snxt>0 else 100}`", inline=False)
    e.set_footer(text="Benimle konuştukça XP kazanırsın kanka! 💪")
    await ctx.reply(embed=e)

@bot.command(name="sıralama")
async def siralama_cmd(ctx):
    if not kullanici_veri:
        await ctx.reply("Henüz kimse XP kazanmamış kanka! İlk sen ol 🚀")
        return
    s = sorted(kullanici_veri.items(), key=lambda x: x[1]["xp"], reverse=True)[:10]
    e = discord.Embed(title="🏆 Ewin AI — XP Sıralaması Top 10", color=0xFFD700)
    med = ["🥇", "🥈", "🥉"]
    text = ""
    for i, (uid, v) in enumerate(s):
        m = med[i] if i < 3 else f"`{i+1}.`"
        k = bot.get_user(int(uid))
        isim = k.display_name if k else "Bilinmeyen"
        text += f"{m} **{isim}** — {rozet_al(v['seviye'])} Sv.{v['seviye']} • `{v['xp']} XP`\n"
    e.description = text
    e.set_footer(text="Daha fazla XP için benimle konuş kanka!")
    await ctx.reply(embed=e)

@bot.command(name="gunluk")
async def gunluk_cmd(ctx):
    kid = str(ctx.author.id)
    bugun = datetime.date.today().isoformat()
    if gunluk_odul_veri.get(kid) == bugun:
        await ctx.reply("⏰ Günlük ödülünü zaten aldın kanka! Yarın tekrar gel 😊")
        return
    gunluk_odul_veri[kid] = bugun
    xp = random.randint(50, 250)
    xp_ekle(kid, xp)
    v = kullanici_veri[kid]
    bonuslar = ["🍀 Bugün şansın açık!", "⚡ Çift XP günü!", "🔥 Ateş günün var!"]
    e = discord.Embed(title="🎁 Günlük Ödül Alındı!", description=f"{random.choice(bonuslar)}\n+**{xp} XP** kazandın kanka! 🎉", color=0x00FF7F)
    e.add_field(name="⭐ Seviye", value=str(v["seviye"]), inline=True)
    e.add_field(name="✨ Toplam XP", value=str(v["xp"]), inline=True)
    e.set_footer(text="Yarın tekrar gel, seni bekliyorum kanka!")
    await ctx.reply(embed=e)

@bot.command(name="profil")
async def profil_cmd(ctx, uye: discord.Member = None):
    hedef = uye or ctx.author
    kid = str(hedef.id)
    v = kullanici_veri.get(kid, {"xp": 0, "seviye": 0, "mesaj_sayisi": 0})
    e = discord.Embed(color=0x5865F2)
    e.set_author(name=f"{hedef.display_name} — Tam Profil", icon_url=hedef.display_avatar.url)
    e.set_thumbnail(url=hedef.display_avatar.url)
    e.add_field(name="🏅 Rozet", value=rozet_al(v["seviye"]), inline=True)
    e.add_field(name="⭐ Seviye", value=f"**{v['seviye']}**", inline=True)
    e.add_field(name="✨ XP", value=str(v["xp"]), inline=True)
    e.add_field(name="💬 AI Mesaj", value=str(v["mesaj_sayisi"]), inline=True)
    e.add_field(name="📅 Katılım", value=hedef.joined_at.strftime("%d.%m.%Y") if hedef.joined_at else "?", inline=True)
    e.add_field(name="🎂 Hesap Yaşı", value=hedef.created_at.strftime("%d.%m.%Y"), inline=True)
    roller = [r.mention for r in hedef.roles if r.name != "@everyone"][:5]
    if roller:
        e.add_field(name="🎭 Roller", value=" ".join(roller), inline=False)
    e.set_footer(text="Ewin AI v6.0 • Grit Sunucusu")
    await ctx.reply(embed=e)

# ═══════════════════════════════════════════════════════════
#                   ARAŞTIRMA & BİLGİ
# ═══════════════════════════════════════════════════════════

@bot.command(name="ara")
async def ara_cmd(ctx, *, sorgu: str):
    async with ctx.channel.typing():
        loop = asyncio.get_event_loop()
        sonuc = await loop.run_in_executor(None, web_ara, sorgu)
    if sonuc:
        e = discord.Embed(title=f"🔍 Araştırma: {sorgu[:50]}", description=sonuc[:2000], color=0x5865F2)
        e.set_footer(text="DuckDuckGo • Ewin AI v6.0")
        await ctx.reply(embed=e)
    else:
        await ctx.reply(f"❌ '{sorgu}' için sonuç bulunamadı kanka. Farklı kelimelerle dene!")

@bot.command(name="hava")
async def hava_cmd(ctx, *, sehir: str = "Istanbul"):
    try:
        encoded = urllib.parse.quote(sehir)
        url = f"https://wttr.in/{encoded}?format=j1"
        req = urllib.request.Request(url)
        req.add_header("User-Agent", "Mozilla/5.0")
        async with ctx.channel.typing():
            loop = asyncio.get_event_loop()
            def al():
                with urllib.request.urlopen(req, timeout=8) as r:
                    return json.loads(r.read().decode("utf-8"))
            veri = await loop.run_in_executor(None, al)
        c = veri["current_condition"][0]
        e = discord.Embed(title=f"🌤️ {sehir.title()} Hava Durumu", description=f"**{c['weatherDesc'][0]['value']}**", color=0x3498DB)
        e.add_field(name="🌡️ Sıcaklık", value=f"{c['temp_C']}°C", inline=True)
        e.add_field(name="🤔 Hissedilen", value=f"{c['FeelsLikeC']}°C", inline=True)
        e.add_field(name="💧 Nem", value=f"%{c['humidity']}", inline=True)
        e.add_field(name="💨 Rüzgar", value=f"{c['windspeedKmph']} km/s", inline=True)
        e.add_field(name="👁️ Görüş", value=f"{c['visibility']} km", inline=True)
        e.add_field(name="🌡️ Hissedilen (F)", value=f"{c['FeelsLikeF']}°F", inline=True)
        e.set_footer(text="wttr.in • Ewin AI v6.0")
        await ctx.reply(embed=e)
    except Exception as ex:
        await ctx.reply(f"❌ '{sehir}' bulunamadı kanka! ({str(ex)[:80]})")

@bot.command(name="ceviriyap")
async def ceviri_cmd(ctx, dil: str, *, metin: str):
    async with ctx.channel.typing():
        loop = asyncio.get_event_loop()
        prompt = f"Şu metni {dil} diline çevir. Sadece çeviriyi ver, başka hiçbir şey yazma:\n{metin}"
        msgs = [{"role": "user", "content": prompt}]
        sonuc = await loop.run_in_executor(None, ai_yanit_al, msgs, None, None)
    e = discord.Embed(title=f"🌐 Çeviri → {dil.title()}", color=0x5865F2)
    e.add_field(name="📝 Orijinal", value=metin[:500], inline=False)
    e.add_field(name="✅ Çeviri", value=sonuc[:500], inline=False)
    e.set_footer(text="Ewin AI v6.0 • AI Çeviri")
    await ctx.reply(embed=e)

@bot.command(name="hesapla")
async def hesapla_cmd(ctx, *, islem: str):
    try:
        temiz = re.sub(r'[^0-9+\-*/().,% ]', '', islem)
        temiz = temiz.replace(',', '.').replace('%', '/100')
        if not temiz.strip():
            raise ValueError("Geçersiz işlem")
        sonuc = eval(temiz)
        if isinstance(sonuc, float):
            sonuc = round(sonuc, 10)
        e = discord.Embed(title="🧮 Hesap Makinesi", color=0x2ECC71)
        e.add_field(name="📥 İşlem", value=f"`{islem}`", inline=False)
        e.add_field(name="📤 Sonuç", value=f"**`{sonuc}`**", inline=False)
        await ctx.reply(embed=e)
    except:
        await ctx.reply("❌ Geçersiz işlem kanka! Örnek: `?hesapla 25 * 4 + 10`")

@bot.command(name="tanim")
async def tanim_cmd(ctx, *, kelime: str):
    async with ctx.channel.typing():
        loop = asyncio.get_event_loop()
        web = await loop.run_in_executor(None, web_ara, f"{kelime} tanımı nedir")
        prompt = f"'{kelime}' kelimesinin/kavramının Türkçe tanımını ver. Kısa, net ve anlaşılır olsun kanka. Varsa köken bilgisini de ekle."
        msgs = [{"role": "user", "content": prompt}]
        sonuc = await loop.run_in_executor(None, ai_yanit_al, msgs, web, None)
    e = discord.Embed(title=f"📖 {kelime.title()}", description=sonuc[:1500], color=0xE67E22)
    e.set_footer(text="Ewin AI v6.0 • Kelime Tanımı")
    await ctx.reply(embed=e)

# ═══════════════════════════════════════════════════════════
#                     EĞLENCE & OYUNLAR
# ═══════════════════════════════════════════════════════════

@bot.command(name="yazıtura")
async def yazıtura_cmd(ctx, bahis: str = "yazı"):
    sonuc = random.choice(["yazı", "tura"])
    kazandi = bahis.lower().strip() == sonuc
    e = discord.Embed(
        title="🪙 Yazı Tura",
        description=f"Para havaya uçtu... **{'🪙 Yazı!' if sonuc=='yazı' else '⭕ Tura!'}**",
        color=0x00FF7F if kazandi else 0xFF6B6B
    )
    if kazandi:
        xp_ekle(str(ctx.author.id), 20)
        e.add_field(name="🎉 Sonuç", value="Kazandın kanka! +**20 XP**", inline=False)
    else:
        e.add_field(name="😅 Sonuç", value="Kaybettin kanka! Şansını dene!", inline=False)
    await ctx.reply(embed=e)

@bot.command(name="zar")
async def zar_cmd(ctx, adet: int = 1):
    adet = min(adet, 5)
    sonuclar = [random.randint(1, 6) for _ in range(adet)]
    zarlar = ["1️⃣","2️⃣","3️⃣","4️⃣","5️⃣","6️⃣"]
    e = discord.Embed(
        title=f"🎲 {adet} Zar!",
        description=" ".join([zarlar[s-1] for s in sonuclar]) + f"\n**Toplam: {sum(sonuclar)}**",
        color=0x5865F2
    )
    if 6 in sonuclar:
        xp_ekle(str(ctx.author.id), 15 * sonuclar.count(6))
        e.add_field(name="🎉 Kritik!", value=f"6 attın kanka! +{15*sonuclar.count(6)} XP!", inline=False)
    await ctx.reply(embed=e)

@bot.command(name="kelime")
async def kelime_cmd(ctx):
    kelimeler = [
        ("bilgisayar","b________r"),("yıldız","y____z"),("kitap","k___p"),
        ("deniz","d___z"),("güneş","g___ş"),("müzik","m___k"),
        ("futbol","f____l"),("arkadaş","a_____ş"),("kahve","k___e"),
        ("pencere","p_____e"),("telefon","t_____n"),("araba","a___a"),
        ("çikolata","ç______a"),("üniversite","ü________e"),
        ("matematik","m_______k"),("düşünce","d_____e"),
    ]
    kelime, ipucu = random.choice(kelimeler)
    e = discord.Embed(title="🔤 Kelime Bul!", description=f"İpucu: **`{ipucu}`**\n⏱️ 30 saniyeniz var kanka!", color=0xFFD700)
    await ctx.reply(embed=e)
    def kontrol(m):
        return m.author == ctx.author and m.channel == ctx.channel
    try:
        msg = await bot.wait_for("message", check=kontrol, timeout=30)
        if msg.content.lower().strip() == kelime:
            xp_ekle(str(ctx.author.id), 30)
            await ctx.send(f"✅ Doğru kanka! **{kelime}** idi! +**30 XP** 🎉")
        else:
            await ctx.send(f"❌ Yanlış kanka! Doğru cevap: **{kelime}**")
    except asyncio.TimeoutError:
        await ctx.send(f"⏰ Süre doldu! Cevap: **{kelime}**")

@bot.command(name="taştopkağıt")
async def rps_cmd(ctx, rakip: discord.Member = None):
    if rakip is None or rakip.bot:
        # Bota karşı oyna
        secimler = ["🪨 Taş", "📄 Kağıt", "✂️ Makas"]
        bot_secim = random.choice(secimler)
        e = discord.Embed(title="🎮 Taş-Kağıt-Makas", description=f"Seçimini yap kanka!\n🪨 `taş` | 📄 `kağıt` | ✂️ `makas`", color=0x5865F2)
        await ctx.reply(embed=e)
        def kontrol(m):
            return m.author == ctx.author and m.channel == ctx.channel and m.content.lower() in ["taş","kağıt","makas"]
        try:
            msg = await bot.wait_for("message", check=kontrol, timeout=20)
            secim = msg.content.lower()
            kazanma = {"taş": "makas", "kağıt": "taş", "makas": "kağıt"}
            emojiler = {"taş": "🪨", "kağıt": "📄", "makas": "✂️"}
            bot_sade = bot_secim.split(" ")[1].lower()
            if secim == bot_sade:
                sonuc = "🤝 Berabere!"
                renk = 0xFFFF00
            elif kazanma[secim] == bot_sade:
                xp_ekle(str(ctx.author.id), 25)
                sonuc = "🎉 Kazandın! +25 XP"
                renk = 0x00FF7F
            else:
                sonuc = "😅 Kaybettin kanka!"
                renk = 0xFF6B6B
            e2 = discord.Embed(title="🎮 Sonuç!", color=renk)
            e2.add_field(name="Sen", value=f"{emojiler[secim]} {secim.title()}", inline=True)
            e2.add_field(name="Ewin AI", value=bot_secim, inline=True)
            e2.add_field(name="Sonuç", value=sonuc, inline=False)
            await ctx.send(embed=e2)
        except asyncio.TimeoutError:
            await ctx.send("⏰ Süre doldu kanka!")

@bot.command(name="quiz")
async def quiz_cmd(ctx):
    sorular = [
        {"s": "Python'da liste oluşturmak için hangi parantez kullanılır?", "c": ["[]","()","{}","<>"], "d": 0},
        {"s": "Türkiye'nin başkenti neresidir?", "c": ["İstanbul","İzmir","Ankara","Bursa"], "d": 2},
        {"s": "1 GB kaç MB'dir?", "c": ["512","1000","1024","2048"], "d": 2},
        {"s": "Discord'u hangi yıl kuruldu?", "c": ["2012","2014","2015","2016"], "d": 2},
        {"s": "HTTP'nin güvenli versiyonu nedir?", "c": ["HTTPS","FTPS","SFTP","SSL"], "d": 0},
        {"s": "En hızlı programlama dili hangisidir?", "c": ["Python","JavaScript","C","Java"], "d": 2},
        {"s": "Bitcoin'i kim yarattı?", "c": ["Elon Musk","Satoshi Nakamoto","Bill Gates","Jeff Bezos"], "d": 1},
        {"s": "Dünyanın en büyük okyanusu hangisidir?", "c": ["Atlantik","Hint","Arktik","Pasifik"], "d": 3},
        {"s": "RAM'in açılımı nedir?", "c": ["Random Access Memory","Read Access Memory","Rapid Access Module","Run Access Memory"], "d": 0},
        {"s": "IPv4 adresi kaç bit uzunluğundadır?", "c": ["16","32","64","128"], "d": 1},
    ]
    soru = random.choice(sorular)
    harfler = ["🇦","🇧","🇨","🇩"]
    e = discord.Embed(title="🧠 Quiz Zamanı!", description=f"**{soru['s']}**", color=0xE67E22)
    for i, c in enumerate(soru["c"]):
        e.add_field(name=harfler[i], value=c, inline=True)
    e.set_footer(text="A, B, C veya D yaz kanka! 20 saniye süren var.")
    await ctx.reply(embed=e)
    def kontrol(m):
        return m.author == ctx.author and m.channel == ctx.channel and m.content.lower() in ["a","b","c","d"]
    try:
        msg = await bot.wait_for("message", check=kontrol, timeout=20)
        secim = ord(msg.content.lower()) - ord('a')
        if secim == soru["d"]:
            xp_ekle(str(ctx.author.id), 40)
            await ctx.send(f"✅ **Doğru!** Cevap: **{soru['c'][soru['d']]}** — +**40 XP** kanka! 🎉")
        else:
            await ctx.send(f"❌ **Yanlış!** Doğru cevap: **{soru['c'][soru['d']]}**")
    except asyncio.TimeoutError:
        await ctx.send(f"⏰ Süre doldu! Doğru cevap: **{soru['c'][soru['d']]}**")

@bot.command(name="yareyarimı")
async def yareyarimı_cmd(ctx, *, soru: str = None):
    if not soru:
        sorular = [
            "Kahve mi çay mı?", "Deniz mi dağ mı?", "Kedi mi köpek mi?",
            "Sabah kişisi mi gece kuşu mu?", "Pizza mı burger mı?",
            "Film mi dizi mi?", "Yaz mı kış mı?", "Kitap mı podcast mi?",
        ]
        soru = random.choice(sorular)
    e = discord.Embed(title="🤔 Yeri yarı mı?", description=f"**{soru}**", color=0x9B59B6)
    e.set_footer(text="Oy ver kanka!")
    msg = await ctx.reply(embed=e)
    await msg.add_reaction("1️⃣")
    await msg.add_reaction("2️⃣")

@bot.command(name="doğruyalaniş")
async def dyi_cmd(ctx, *, ifade: str):
    async with ctx.channel.typing():
        loop = asyncio.get_event_loop()
        web = await loop.run_in_executor(None, web_ara, ifade)
        prompt = f"Şu ifade doğru mu yanlış mı? Kısa ve net açıkla kanka: '{ifade}'"
        msgs = [{"role": "user", "content": prompt}]
        yanit = await loop.run_in_executor(None, ai_yanit_al, msgs, web, None)
    e = discord.Embed(title="🔎 Doğru mu Yanlış mı?", description=f"**İfade:** {ifade}\n\n**Değerlendirme:**\n{yanit[:1500]}", color=0x2ECC71)
    e.set_footer(text="Ewin AI v6.0 • Anlık Web Araştırması ile")
    await ctx.reply(embed=e)

@bot.command(name="fal")
async def fal_cmd(ctx):
    fallar = [
        "Yakında çok güzel bir sürprizle karşılaşacaksın kanka! ✨",
        "Bu hafta şansın zirve, fırsatları kaçırma kanka! 🍀",
        "Birileri seni düşünüyor... ve bu çok iyi bir şey kanka! 💫",
        "Kısa süre içinde harika haberler alacaksın kanka! 📩",
        "Sabırlı ol kanka, güzel şeyler tam olgunlaşmak üzere! 🌟",
        "Bu hafta enerjin zirve, harekete geç kanka! ⚡",
        "Yeni bir başlangıç kapıda kanka, hazır ol! 🚪",
        "Seni bekleyen büyük bir fırsat var, gözlerini aç kanka! 👀",
        "Yakın çevrenden beklenmedik iyi bir haber gelecek kanka! 🎁",
        "Hayallerin peşinden git kanka, tam zamanı! 🚀",
        "Bugün aldığın her karar seni daha iyiye götürecek kanka! 💎",
        "Bir yıldız gibi parlayacaksın kanka, inan kendine! 👑",
    ]
    e = discord.Embed(
        title="🔮 Ewin AI — Fal Köşesi",
        description=f"*Kristal küreme bakıyorum {ctx.author.mention}...*\n*Yıldızlara soruyorum...*\n\n{random.choice(fallar)}",
        color=0x9B59B6
    )
    e.set_footer(text="Sadece eğlence amaçlı kanka! 😄")
    await ctx.reply(embed=e)

@bot.command(name="8top")
async def sekiztop_cmd(ctx, *, soru: str = "Söyle bakalım"):
    cevaplar = [
        "✅ Kesinlikle evet kanka!", "✅ Evet, inan bana!",
        "✅ Çok büyük ihtimalle!", "✅ Bence evet!",
        "🤔 Belirsiz, tekrar sor kanka", "🤔 Şu an söylemek zor",
        "🤔 Duruma göre değişir kanka", "🤔 Bilmiyorum kanka...",
        "❌ Bence hayır kanka", "❌ Kesinlikle hayır!",
        "❌ İhtimaller pek yüz güldürmüyor", "❌ Hayıra daha yakın kanka"
    ]
    e = discord.Embed(
        title="🎱 Sihirli 8 Top",
        description=f"**Soru:** {soru}\n\n**🎱** {random.choice(cevaplar)}",
        color=0x2C3E50
    )
    await ctx.reply(embed=e)

@bot.command(name="motivasyon")
async def motivasyon_cmd(ctx):
    sozler = [
        "Başarı bir gün gelmiyor kanka, her gün biraz inşa ediyorsun. 💪",
        "Küçük adımlar, büyük yolculuklar yaratır kanka. Devam et! 🚀",
        "Dün en iyisini yaptın, bugün daha iyisini yapacaksın kanka! ⭐",
        "Zorlandığında dur ve düşün — vazgeçmek en kolay seçim ama sen kolay yolu seçmiyorsun kanka! 🔥",
        "Her uzman, bir zamanlar yeni başlayandı kanka. Sen de o yoldasın! 📚",
        "Başarısızlık son nokta değil, öğrenme sürecinin parçası kanka! 💡",
        "Bugün yorgun hissediyorsan bu ilerlediğinin kanıtı kanka! 🏆",
        "Sen düşündüğünden çok daha güçlüsün kanka, unutma! 💎",
        "Fırtınadan korkan kaptan asla büyük denizlere açılamaz kanka! ⚓",
        "Bugünün eforları yarının başarısını inşa ediyor kanka! 🏗️",
    ]
    e = discord.Embed(title="💪 Günlük Motivasyon", description=random.choice(sozler), color=0xF39C12)
    e.set_footer(text=f"Ewin AI • {ctx.author.display_name} için 🌟")
    await ctx.reply(embed=e)

@bot.command(name="şaka")
async def saka_cmd(ctx):
    sakalar = [
        "Bir programcı karısına dedi ki 'Markete git, ekmek al, yumurta varsa 6 tane al'. Karısı 6 ekmek aldı kanka 😂",
        "— Neden programcılar karanlığı sever? — Çünkü light mode var kanka 😅",
        "Java Developer'a sordular: 'Şu an ne yapıyorsun?' — 'NullPointerException'la boğuşuyorum kanka' dedi.",
        "Python: 'Girintiye bak kanka!'\nC++: 'Pointer'a bak kanka!'\nJavaScript: 'undefined'a bak kanka!'",
        "Bir yazılımcı hayatının en kötü günü: Taşındı, yeni ev, WiFi yok. 404: Motivasyon bulunamadı kanka 😂",
        "— Git push yaparken ne hissediyorsun? — 'İyi ki commit yapmışım' duygusu... sonra revert... kanka 😅",
        "Optimist: 'Bardak yarı dolu!'\nPesimist: 'Bardak yarı boş!'\nProgramcı: 'Bardak 2 kat büyük, fix lazım kanka'",
    ]
    e = discord.Embed(title="😂 Günün Şakası", description=random.choice(sakalar), color=0xF1C40F)
    e.set_footer(text="Ewin AI v6.0 • Eğlence Köşesi 😄")
    await ctx.reply(embed=e)

@bot.command(name="gif")
async def gif_cmd(ctx, *, konu: str = "funny"):
    try:
        encoded = urllib.parse.quote(konu)
        url = f"https://api.giphy.com/v1/gifs/random?tag={encoded}&rating=g&api_key=dc6zaTOxFJmzC"
        req = urllib.request.Request(url)
        req.add_header("User-Agent", "Mozilla/5.0")
        loop = asyncio.get_event_loop()
        def al():
            with urllib.request.urlopen(req, timeout=8) as r:
                return json.loads(r.read().decode("utf-8"))
        veri = await loop.run_in_executor(None, al)
        gif_url = veri["data"]["images"]["original"]["url"]
        e = discord.Embed(title=f"🎬 {konu.title()}", color=0xFF6B9D)
        e.set_image(url=gif_url)
        e.set_footer(text="GIPHY • Ewin AI v6.0")
        await ctx.reply(embed=e)
    except:
        await ctx.reply("❌ GIF bulunamadı kanka! Farklı bir konu dene.")

# ═══════════════════════════════════════════════════════════
#                   KİŞİSEL ARAÇLAR
# ═══════════════════════════════════════════════════════════

@bot.command(name="notekle")
async def not_ekle(ctx, *, not_metni: str):
    kid = str(ctx.author.id)
    if kid not in kullanici_notlar:
        kullanici_notlar[kid] = []
    if len(kullanici_notlar[kid]) >= 10:
        await ctx.reply("❌ En fazla 10 not saklayabilirsin kanka! Önce bir not sil: `?notSil [numara]`")
        return
    kullanici_notlar[kid].append({"metin": not_metni, "tarih": datetime.datetime.now().strftime("%d.%m.%Y %H:%M")})
    await ctx.reply(f"✅ Not kaydedildi kanka! Toplam **{len(kullanici_notlar[kid])}** notun var.")

@bot.command(name="notlarım")
async def notlar_cmd(ctx):
    kid = str(ctx.author.id)
    notlar = kullanici_notlar.get(kid, [])
    if not notlar:
        await ctx.reply("📭 Hiç notun yok kanka! `?notekle [metin]` ile ekle.")
        return
    e = discord.Embed(title=f"📝 {ctx.author.display_name}'in Notları", color=0x5865F2)
    for i, n in enumerate(notlar, 1):
        e.add_field(name=f"#{i} — {n['tarih']}", value=n['metin'][:200], inline=False)
    e.set_footer(text=f"{len(notlar)}/10 not • ?notSil [numara] ile sil")
    await ctx.reply(embed=e)

@bot.command(name="notSil")
async def not_sil(ctx, numara: int):
    kid = str(ctx.author.id)
    notlar = kullanici_notlar.get(kid, [])
    if not notlar or numara < 1 or numara > len(notlar):
        await ctx.reply(f"❌ Geçersiz numara kanka! 1-{len(notlar)} arası gir.")
        return
    silinen = notlar.pop(numara - 1)
    await ctx.reply(f"🗑️ **#{numara}** notu silindi kanka: ~~{silinen['metin'][:80]}~~")

@bot.command(name="hatırla")
async def hatirla_cmd(ctx, dakika: int, *, mesaj: str):
    if dakika < 1 or dakika > 1440:
        await ctx.reply("❌ 1-1440 dakika arası gir kanka!")
        return
    zaman = datetime.datetime.now() + datetime.timedelta(minutes=dakika)
    hatirlat_veri.append({"kullanici_id": ctx.author.id, "kanal_id": ctx.channel.id, "mesaj": mesaj, "zaman": zaman})
    e = discord.Embed(title="⏰ Hatırlatıcı Kuruldu!", description=f"**{dakika} dakika** sonra sana hatırlatacağım kanka!\n📝 **Not:** {mesaj}", color=0x00FF7F)
    await ctx.reply(embed=e)

@bot.command(name="şifre")
async def sifre_cmd(ctx, uzunluk: int = 16):
    uzunluk = max(8, min(uzunluk, 64))
    karakterler = string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}|;:,.<>?"
    sifre = ''.join(random.choice(karakterler) for _ in range(uzunluk))
    e = discord.Embed(title="🔐 Güvenli Şifre", color=0x2ECC71)
    e.add_field(name=f"🔑 {uzunluk} Karakterli Şifre", value=f"||`{sifre}`||", inline=False)
    e.add_field(name="💡 İpucu", value="Şifreyi bir yere kaydet kanka! Bu mesajı sil.", inline=False)
    e.set_footer(text="Ewin AI v6.0 • Güvenlik Araçları • Spoiler ile gizlendi")
    try:
        await ctx.author.send(embed=e)
        await ctx.reply("🔐 Şifren DM'ine gönderildi kanka! (Gizliliğin için)")
    except:
        await ctx.reply(embed=e)

@bot.command(name="bmi")
async def bmi_cmd(ctx, boy_cm: float, kilo_kg: float):
    boy_m = boy_cm / 100
    bmi = kilo_kg / (boy_m ** 2)
    bmi = round(bmi, 1)
    if bmi < 18.5:
        durum = "⚠️ Zayıf"
        renk = 0x3498DB
    elif bmi < 25:
        durum = "✅ Normal"
        renk = 0x2ECC71
    elif bmi < 30:
        durum = "⚠️ Fazla Kilolu"
        renk = 0xF39C12
    else:
        durum = "❌ Obez"
        renk = 0xFF6B6B
    e = discord.Embed(title="⚖️ BMI Hesaplama", color=renk)
    e.add_field(name="📏 Boy", value=f"{boy_cm} cm", inline=True)
    e.add_field(name="⚖️ Kilo", value=f"{kilo_kg} kg", inline=True)
    e.add_field(name="📊 BMI", value=f"**{bmi}**", inline=True)
    e.add_field(name="🏷️ Durum", value=durum, inline=False)
    e.set_footer(text="Ewin AI v6.0 • Sağlık Araçları • Doktoruna danış kanka!")
    await ctx.reply(embed=e)

# ═══════════════════════════════════════════════════════════
#                    SUNUCU ARAÇLARI
# ═══════════════════════════════════════════════════════════

@bot.command(name="anket")
async def anket_cmd(ctx, soru: str, a: str, b: str, c: str = None, d: str = None):
    e = discord.Embed(title="📊 Anket", description=f"**{soru}**", color=0x3498DB)
    e.add_field(name="🇦", value=a, inline=True)
    e.add_field(name="🇧", value=b, inline=True)
    if c:
        e.add_field(name="🇨", value=c, inline=True)
    if d:
        e.add_field(name="🇩", value=d, inline=True)
    e.set_footer(text=f"Anket: {ctx.author.display_name} • Ewin AI v6.0")
    msg = await ctx.send(embed=e)
    await msg.add_reaction("🇦")
    await msg.add_reaction("🇧")
    if c: await msg.add_reaction("🇨")
    if d: await msg.add_reaction("🇩")

@bot.command(name="sunucu")
async def sunucu_cmd(ctx):
    g = ctx.guild
    bot_sayisi = sum(1 for m in g.members if m.bot)
    insan_sayisi = g.member_count - bot_sayisi
    e = discord.Embed(title=f"📊 {g.name}", color=0x5865F2)
    if g.icon:
        e.set_thumbnail(url=g.icon.url)
    e.add_field(name="👥 Toplam Üye", value=str(g.member_count), inline=True)
    e.add_field(name="👤 İnsan", value=str(insan_sayisi), inline=True)
    e.add_field(name="🤖 Bot", value=str(bot_sayisi), inline=True)
    e.add_field(name="💬 Kanallar", value=str(len(g.channels)), inline=True)
    e.add_field(name="🎭 Roller", value=str(len(g.roles)), inline=True)
    e.add_field(name="😀 Emojiler", value=str(len(g.emojis)), inline=True)
    e.add_field(name="📅 Kuruluş", value=g.created_at.strftime("%d.%m.%Y"), inline=True)
    e.add_field(name="👑 Sahip", value=g.owner.display_name if g.owner else "?", inline=True)
    e.add_field(name="🆔 Server ID", value=str(g.id), inline=True)
    e.set_footer(text="Ewin AI v6.0 • Sunucu İstatistikleri")
    await ctx.reply(embed=e)

@bot.command(name="kullanıcı")
async def kullanici_cmd(ctx, uye: discord.Member = None):
    hedef = uye or ctx.author
    e = discord.Embed(title=f"👤 {hedef.display_name}", color=hedef.color if hedef.color.value != 0 else 0x5865F2)
    e.set_thumbnail(url=hedef.display_avatar.url)
    e.add_field(name="🆔 ID", value=str(hedef.id), inline=True)
    e.add_field(name="🤖 Bot mu?", value="Evet" if hedef.bot else "Hayır", inline=True)
    e.add_field(name="🎭 En Yüksek Rol", value=hedef.top_role.mention, inline=True)
    e.add_field(name="📅 Katılım", value=hedef.joined_at.strftime("%d.%m.%Y %H:%M") if hedef.joined_at else "?", inline=True)
    e.add_field(name="🎂 Hesap Oluşturma", value=hedef.created_at.strftime("%d.%m.%Y %H:%M"), inline=True)
    durum = str(hedef.status).replace("online","🟢 Çevrimiçi").replace("idle","🟡 Boşta").replace("dnd","🔴 Rahatsız Etme").replace("offline","⚫ Çevrimdışı")
    e.add_field(name="🌐 Durum", value=durum, inline=True)
    await ctx.reply(embed=e)

@bot.command(name="botbilgi")
async def botbilgi_cmd(ctx):
    aktif_kullanici = len(kullanici_veri)
    toplam_mesaj = sum(v.get("mesaj_sayisi", 0) for v in kullanici_veri.values())
    e = discord.Embed(title="🤖 Ewin AI — Bot Bilgileri", color=0x5865F2)
    e.set_thumbnail(url=ctx.bot.user.display_avatar.url)
    e.add_field(name="📛 İsim", value="Ewin AI", inline=True)
    e.add_field(name="🔢 Versiyon", value="v6.0 Hyper", inline=True)
    e.add_field(name="🧠 Model", value="LLaMA 3.3 70B", inline=True)
    e.add_field(name="👥 Aktif Kullanıcı", value=str(aktif_kullanici), inline=True)
    e.add_field(name="💬 Toplam AI Mesaj", value=str(toplam_mesaj), inline=True)
    e.add_field(name="⏰ Hatırlatıcı", value=str(len(hatirlat_veri)), inline=True)
    e.add_field(name="🌐 Web Araştırma", value="✅ Aktif (Her Mesaj)", inline=True)
    e.add_field(name="🌍 Dil Desteği", value="14+ Dil", inline=True)
    e.add_field(name="🛡️ Geliştirici", value="Grit Ekibi", inline=True)
    e.set_footer(text="Ewin AI v6.0 • Grit Discord Sunucusu")
    e.timestamp = datetime.datetime.utcnow()
    await ctx.reply(embed=e)

@bot.command(name="sayac")
async def sayac_cmd(ctx, hedef: int = 100):
    if hedef < 2 or hedef > 10000:
        await ctx.reply("❌ 2-10000 arası bir sayı gir kanka!")
        return
    kid = str(ctx.channel.id)
    sayac_veri[kid] = {"hedef": hedef, "mevcut": 0, "son": None}
    e = discord.Embed(title=f"🔢 Sayaç Başladı!", description=f"**{hedef}**'e kadar sayın kanka!\nSırayla sayı yazın. Yanlış sayı = sıfırlanır!", color=0x00FF7F)
    await ctx.send(embed=e)

@bot.event
async def on_message_sayac(message):
    if message.author.bot:
        return
    kid = str(message.channel.id)
    if kid not in sayac_veri:
        return
    s = sayac_veri[kid]
    try:
        sayi = int(message.content.strip())
        if sayi == s["mevcut"] + 1 and message.author.id != s["son"]:
            s["mevcut"] = sayi
            s["son"] = message.author.id
            if sayi == s["hedef"]:
                del sayac_veri[kid]
                xp_ekle(str(message.author.id), 100)
                await message.add_reaction("🎉")
                await message.channel.send(f"🎉 **{s['hedef']}**'e ulaşıldı! Tebrikler kanka! +100 XP!")
            else:
                await message.add_reaction("✅")
        elif sayi != s["mevcut"] + 1:
            s["mevcut"] = 0
            s["son"] = None
            await message.add_reaction("❌")
            await message.channel.send(f"❌ Yanlış sayı kanka! Sayaç sıfırlandı. 1'den başlayın!")
    except ValueError:
        pass

# ═══════════════════════════════════════════════════════════
#                    MODERASYON
# ═══════════════════════════════════════════════════════════

@bot.command(name="uyar")
@commands.has_permissions(manage_messages=True)
async def uyar_cmd(ctx, uye: discord.Member, *, sebep: str = "Sebep belirtilmedi"):
    kid = str(uye.id)
    if kid not in uyari_veri:
        uyari_veri[kid] = []
    uyari_veri[kid].append({"sebep": sebep, "tarih": datetime.datetime.now().strftime("%d.%m.%Y %H:%M"), "yetkili": str(ctx.author)})
    e = discord.Embed(title="⚠️ Uyarı Verildi", color=0xFF6B6B)
    e.add_field(name="👤 Kullanıcı", value=uye.mention, inline=True)
    e.add_field(name="⚠️ Uyarı Sayısı", value=str(len(uyari_veri[kid])), inline=True)
    e.add_field(name="📝 Sebep", value=sebep, inline=False)
    e.add_field(name="🛡️ Yetkili", value=ctx.author.mention, inline=True)
    e.set_footer(text="Ewin AI v6.0 • Moderasyon")
    await ctx.reply(embed=e)
    try:
        dm_e = discord.Embed(title="⚠️ Uyarı Aldın!", description=f"**{ctx.guild.name}** sunucusunda uyarı aldın kanka.", color=0xFF6B6B)
        dm_e.add_field(name="📝 Sebep", value=sebep, inline=False)
        dm_e.add_field(name="⚠️ Toplam Uyarı", value=str(len(uyari_veri[kid])), inline=True)
        await uye.send(embed=dm_e)
    except:
        pass

@bot.command(name="uyarılar")
@commands.has_permissions(manage_messages=True)
async def uyarilar_cmd(ctx, uye: discord.Member):
    kid = str(uye.id)
    uyarilar = uyari_veri.get(kid, [])
    if not uyarilar:
        await ctx.reply(f"✅ {uye.mention} hiç uyarı almamış kanka!")
        return
    e = discord.Embed(title=f"⚠️ {uye.display_name} — Uyarıları", color=0xFF6B6B)
    for i, u in enumerate(uyarilar, 1):
        e.add_field(name=f"#{i} — {u['tarih']}", value=f"📝 {u['sebep']}\n🛡️ {u['yetkili']}", inline=False)
    e.set_footer(text=f"Toplam {len(uyarilar)} uyarı")
    await ctx.reply(embed=e)

@bot.command(name="temizle")
@commands.has_permissions(manage_messages=True)
async def temizle_cmd(ctx, sayi: int = 10):
    sayi = min(sayi, 100)
    await ctx.channel.purge(limit=sayi + 1)
    msg = await ctx.send(f"✅ **{sayi}** mesaj silindi kanka!")
    await asyncio.sleep(3)
    await msg.delete()

@bot.command(name="duyur")
@commands.has_permissions(administrator=True)
async def duyur_cmd(ctx, *, mesaj: str):
    e = discord.Embed(title="📢 Duyuru", description=mesaj, color=0xE74C3C)
    e.set_footer(text=f"Duyuran: {ctx.author.display_name} • {datetime.datetime.now().strftime('%d.%m.%Y %H:%M')}")
    await ctx.send("@everyone", embed=e)
    await ctx.message.delete()

# ═══════════════════════════════════════════════════════════
#                    SLASH KOMUTLARI
# ═══════════════════════════════════════════════════════════

@bot.tree.command(name="help", description="Ewin AI komut listesi")
async def yardim_slash(interaction: discord.Interaction):
    e = discord.Embed(
        title="🤖 Ewin AI v6.0 Hyper",
        description="Grit'in resmi yapay zeka asistanı!\n**@mention** at ve konuş kanka! 🌐 Web araştırması otomatik!",
        color=0x5865F2
    )
    e.set_thumbnail(url=bot.user.display_avatar.url)
    e.add_field(name="🔑 Prefix Komutlar", value="`?help` ile tam listeyi gör kanka!", inline=False)
    e.set_footer(text="Ewin AI v6.0 • Grit Ekibi • LLaMA 3.3 70B")
    await interaction.response.send_message(embed=e, ephemeral=True)

@bot.tree.command(name="sor", description="Ewin AI'ya soru sor")
@app_commands.describe(mesaj="Sorunun nedir?")
async def sor_slash(interaction: discord.Interaction, mesaj: str):
    await interaction.response.defer()
    kid = str(interaction.user.id)
    if kid not in sohbet_gecmisi:
        sohbet_gecmisi[kid] = []
    sohbet_gecmisi[kid].append({"role": "user", "content": mesaj})
    if len(sohbet_gecmisi[kid]) > 24:
        sohbet_gecmisi[kid] = sohbet_gecmisi[kid][-24:]
    xp_ekle(kid)
    try:
        loop = asyncio.get_event_loop()
        web = await loop.run_in_executor(None, web_ara, mesaj)
        yanit = await loop.run_in_executor(None, ai_yanit_al, sohbet_gecmisi[kid], web, None)
        sohbet_gecmisi[kid].append({"role": "assistant", "content": yanit})
        if len(yanit) > 2000: yanit = yanit[:1997] + "..."
        await interaction.followup.send(yanit)
    except Exception as ex:
        await interaction.followup.send(f"❌ Hata: {str(ex)[:200]}")

@bot.tree.command(name="seviye", description="Seviye bilgini gör")
async def seviye_slash(interaction: discord.Interaction):
    kid = str(interaction.user.id)
    v = kullanici_veri.get(kid, {"xp": 0, "seviye": 0, "mesaj_sayisi": 0})
    e = discord.Embed(color=0x5865F2)
    e.set_author(name=f"{interaction.user.display_name} — Profil", icon_url=interaction.user.display_avatar.url)
    e.add_field(name="🏅 Rozet", value=rozet_al(v["seviye"]), inline=True)
    e.add_field(name="⭐ Seviye", value=f"**{v['seviye']}**", inline=True)
    e.add_field(name="✨ XP", value=str(v["xp"]), inline=True)
    e.set_thumbnail(url=interaction.user.display_avatar.url)
    await interaction.response.send_message(embed=e, ephemeral=True)

@bot.tree.command(name="gunluk", description="Günlük XP ödülünü al")
async def gunluk_slash(interaction: discord.Interaction):
    kid = str(interaction.user.id)
    bugun = datetime.date.today().isoformat()
    if gunluk_odul_veri.get(kid) == bugun:
        await interaction.response.send_message("⏰ Günlük ödülünü zaten aldın kanka! Yarın gel 😊", ephemeral=True)
        return
    gunluk_odul_veri[kid] = bugun
    xp = random.randint(50, 250)
    xp_ekle(kid, xp)
    await interaction.response.send_message(f"🎁 +**{xp} XP** kazandın kanka! 🎉")

@bot.tree.command(name="sifirla", description="Sohbet hafızasını sıfırla")
async def sifirla_slash(interaction: discord.Interaction):
    kid = str(interaction.user.id)
    if kid in sohbet_gecmisi:
        del sohbet_gecmisi[kid]
    await interaction.response.send_message("🔄 Hafıza sıfırlandı kanka!", ephemeral=True)

# ═══════════════════════════════════════════════════════════
bot.run(DISCORD_TOKEN)
