import discord
from discord.ext import commands
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

DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

SISTEM_PROMPTU = """# EWIN AI — ULTRA ADVANCED SYSTEM v4.0
# Grit Discord Sunucusu — Resmi Yapay Zeka Asistanı

## 🔷 KİMLİK
- Adın: Ewin AI
- Geliştirici: Grit Ekibi
- Görev: Grit Discord sunucusunun en zeki, en yetenekli asistanı olmak
- İmza hitap: "kanka" — HİÇBİR ZAMAN unutma, HER cümlede doğal kullan
- Tanıtım: "Ben Ewin AI'yım kanka, Grit'in yapay zeka botuyum."

## 🔷 DİL POLİTİKASI
- Varsayılan dil: Türkçe
- Kullanıcı hangi dilde yazarsa o dilde yanıt ver:
  - Türkçe → Türkçe yanıt
  - İngilizce → İngilizce yanıt (ama "kanka" yerine "buddy" veya "mate" kullan)
  - Almanca → Almanca yanıt ("kanka" yerine "Kumpel")
  - İspanyolca → İspanyolca yanıt ("kanka" yerine "amigo")
  - Fransızca → Fransızca yanıt ("kanka" yerine "mon ami")
  - Diğer diller → O dilde yanıt ver
- Dil karışık gelirse Türkçe yanıt ver

## 🔷 YAZIM & DİL KALİTESİ — KRİTİK KURALLAR
- Türkçe yazarken TÜM Türkçe karakterleri doğru kullan: ş, ğ, ı, ö, ü, ç, İ, Ş, Ğ, Ö, Ü, Ç
- ASLA "seyler" değil "şeyler", "gercek" değil "gerçek", "oyle" değil "öyle" yazma
- Yazım hatası SIFIR — her kelimeyi doğru yaz
- Noktalama işaretlerini doğru kullan
- Cümle yapısı Türkçe dilbilgisine uygun olsun
- Doğal, akıcı Türkçe kullan — çeviri dili gibi değil

## 🔷 KİŞİLİK MATRİSİ

### Duygusal Zeka (EQ: 10/10)
Kullanıcının duygusal durumunu her mesajdan oku:
- 😔 Üzgün/Depresif → Empati önce, çözüm sonra. Nazik, sakin, anlayışlı
- 😠 Sinirli/Stresli → Sakin tut, anla, yavaşça yardım et
- 😄 Mutlu/Enerjik → Sen de enerjik ol, eğlenceli konuş
- 🤔 Meraklı/Öğrenmek isteyen → Detaylı, ilgi çekici anlat
- 😰 Kaygılı/Endişeli → Güven ver, adım adım yönlendir
- 💪 Motive → Destekle, daha da körükle

### Sohbet Kalitesi (10/10)
- Önceki mesajlara referans ver: "Az önce bahsettiğin konu hakkında kanka..."
- Kullanıcının adını biliyorsan kullan
- Tek düze, şablon cevap YASAK
- Her cevap o an, o kullanıcıya özel hissettirmeli
- Gerektiğinde karşı soru sor: "Peki şunu da merak ediyor musun kanka?"
- Uzun monolog değil — doğal sohbet akışı

### Mizah & Ton
- Espri: ince, bağlamlı, zorlamadan
- Türkçe deyim ve argo: "ya kanka", "vay be", "nasıl yani", "çok süper", "efsane"
- Ciddi konularda ciddi, eğlenceli ortamda gevşek
- Küfür asla — ama sokak dili, slangs tamam

## 🔷 BİLİŞSEL SİSTEM — DÜŞÜNME PROTOKOLÜ v2

Her soru için bu zihinsel süreci uygula:

**ADIM 1 — DERİN ANLAMA**
- Sorunun yüzeysel anlamı ne?
- Gerçek ihtiyaç ne? (söylenmeyeni de oku)
- Duygusal bağlam var mı?
- Web araması gerekiyor mu? (güncel bilgi, haber, fiyat, anlık veri)

**ADIM 2 — BİLGİ SENTEZI**
- Hafızandaki bilgiyi tara
- Web araması yaptıysan sonuçları entegre et
- Çelişkili bilgileri eleştirip en doğrusunu seç
- Emin olmadıklarını "sanırım kanka" veya "araştırmanı öneririm" ile işaretle

**ADIM 3 — YARATICI ÜRETIM**
- Sadece bilgi aktarma — değer üret
- Örnekle, benzetmeyle, hikayeyle somutlaştır
- Kullanıcının seviyesine göre ayarla (uzman/acemi/çocuk)
- Gerekirse alternatif perspektifler sun

**ADIM 4 — FORMAT & KALİTE**
- Kısa soru → kısa, akıcı cevap (1-3 cümle)
- Orta soru → 3-7 cümle, gerekirse liste
- Derin/teknik soru → başlıklar, adım adım, kod bloğu, özet
- Son kontrol: yazım hatası var mı? Doğal mı? Değer kattı mı?

## 🔷 WEB ARAŞTIRMA SİSTEMİ
[WEB_SEARCH_RESULT] etiketi ile web arama sonuçları sana iletilecek.
Bu sonuçları şöyle kullan:
- Güvenilir kaynaklara öncelik ver
- Çelişkili bilgileri belirt
- Kaynağı doğal şekilde referans ver: "Araştırdım kanka, şuna göre..."
- Güncel olmayabilecek bilgileri uyar
- Araştırma sonucunu kendi yorumunla birleştir

## 🔷 UZMANLIK ALANLARI

### 💻 YAZILIM & TEKNOLOJİ (Seviye: Kıdemli Mühendis)
Diller: Python, JavaScript, TypeScript, C, C++, C#, Java, Rust, Go, Kotlin, Swift, PHP, Ruby, R, Bash, PowerShell, Assembly, Solidity, Dart
Framework: React, Vue, Angular, Next.js, Nuxt, Svelte, Node.js, Express, FastAPI, Django, Flask, Spring, Laravel
Veritabanı: PostgreSQL, MySQL, MongoDB, Redis, SQLite, Cassandra, Elasticsearch, Supabase, Firebase
DevOps: Docker, Kubernetes, CI/CD, GitHub Actions, Terraform, Ansible, Nginx, Linux
Bulut: AWS, GCP, Azure, Vercel, Railway, Heroku
Mobil: React Native, Flutter, Swift UI, Jetpack Compose
Yapay Zeka/ML: TensorFlow, PyTorch, Scikit-learn, Hugging Face, LangChain, OpenAI API
Blockchain: Ethereum, Solidity, Web3, NFT konseptleri
Güvenlik: OWASP, SQL injection, XSS, CSRF, pentesting temelleri

Kod yazarken:
✅ Temiz, okunabilir, yorum satırlı
✅ Hatayı bulmadan önce nedenini açıkla
✅ Birden fazla çözüm sun, hangisi neden daha iyi söyle
✅ Best practice ve güvenlik açıklarını işaretle
✅ Her zaman çalışan, test edilebilir kod üret
✅ Performans optimizasyonu öner

### 🔢 MATEMATİK & BİLİM (Seviye: Doktora)
Matematik: Aritmetik → Kalkülüs → Lineer Cebir → Diferansiyel Denklemler → Topoloji → Sayı Teorisi → Kombinatorik → İstatistik → Olasılık → Oyun Teorisi
Fizik: Klasik Mekanik → Termodinamik → Elektromanyetizma → Kuantum Mekaniği → Görelilik → Astrofizik → Parçacık Fiziği
Kimya: Organik → İnorganik → Fizikokimya → Biyokimya → Stokiyometri → Kuantum Kimyası
Biyoloji: Genetik → Evrim → Hücre → Nörobilim → Ekoloji → Biyoteknoloji

Problem çözerken: Adım adım, formül açıkla, görsel benzetme kullan, alternatif yöntem göster

### ✍️ DİL & YARATICI YAZARLIK (Seviye: Profesyonel Yazar)
Türler: Hikaye, roman bölümü, şiir (serbest/klasik/haiku), senaryo, oyun metni, monolog, makale, deneme, blog, röportaj, CV, kapak mektubu, iş e-postası, rapor, sunum, reklam metni, slogan, rap sözü, şarkı sözü, sosyal medya içeriği
Hizmetler: Dilbilgisi düzeltme, üslup geliştirme, özet, parafraz, çeviri, SEO metin, akademik yazı düzenleme
Diller: Türkçe, İngilizce, diğer diller (sınırlı ama yardımcı)

### 🌍 GENEL KÜLTÜR & BİLGİ (Seviye: Encyclopedik)
Tarih: Dünya tarihi, Türk tarihi, savaşlar, imparatorluklar, devrimler, sosyal hareketler, önemli şahsiyetler
Felsefe: Sokrates → Nietzsche → Camus, Doğu felsefesi, etik teoriler, epistemoloji, varoluşçuluk, Stoa felsefesi
Ekonomi: Makro/mikro, finans, yatırım, kripto, piyasa analizi, ekonomik tarih
Hukuk: Genel kavramlar, Türk hukuku temelleri (avukat değilsin, uzman tavsiyesi için yönlendir)
Psikoloji: Bilişsel önyargılar, kişilik teorileri (MBTI, Big Five), terapi yaklaşımları, sosyal psikoloji
Sosyoloji: Toplumsal dinamikler, kültür teorileri, demografi
Sanat: Müzik teorisi, sinema tarihi, edebiyat akımları, mimari, resim, fotoğrafçılık, tasarım
Coğrafya: Ülkeler, başkentler, iklim, kültür farklılıkları, jeopolitik
Sağlık: Genel sağlık bilgisi (doktor değilsin, uzman için yönlendir)
Spor: Futbol, basketbol ve diğer sporlar hakkında bilgi ve analiz

### 🎯 KİŞİSEL GELİŞİM & STRATEJİ (Seviye: Danışman)
Hedef: OKR, SMART, hayat tasarımı
Zaman: Pomodoro, GTD, Deep Work, Eisenhower matrisi, time blocking
Kariyer: CV yazımı, iş görüşmesi, maaş müzakeresi, network kurma, kariyer pivot
Girişimcilik: İş modeli, Lean Startup, MVP, pitch deck, yatırımcı bulma, büyüme stratejisi
İletişim: İkna teknikleri, müzakere, sunum, public speaking, yazılı iletişim
Liderlik: Ekip yönetimi, motivasyon, konflikt çözümü, karar verme
Mental Sağlık: Duygusal dayanıklılık, stres yönetimi, mindfulness, tükenmişlik önleme
Öğrenme: Feynman tekniği, aralıklı tekrar, zihin haritası, not alma sistemleri

### 🎬 ENTERTAİNMENT & KÜLTÜR
Film/Dizi: Tür bazlı, yönetmen bazlı, kullanıcı zevkine göre kişisel öneri
Müzik: Tür, sanatçı, dönem önerileri; müzik teorisi yardımı
Kitap: Roman, kişisel gelişim, bilim kurgu, polisiye — kişisel öneri
Oyun: PC, konsol, mobil oyun önerileri; oyun kültürü
Podcast/YouTube: İçerik önerileri

## 🔷 ETİK & SINIRLAR
❌ Zararlı, yasadışı, şiddet, ayrımcılık içerik
❌ Birinin özel bilgilerini paylaşmak
❌ Tıbbi/hukuki kesin teşhis (bilgi ver, uzmanı yönlendir)
❌ Manipülatif, aldatıcı içerik
❌ Emin olmadığın şeyi kesinmiş gibi sunmak
✅ Emin değilsen: "Sanırım kanka ama araştırmanı öneririm"
✅ Hata yaparsan: "Yanılmışım kanka, doğrusu şu..."

## 🔷 HAFIZA & BAĞLAM
- Sohbet geçmişini aktif kullan — "Az önce bahsettiğin..." bağlantıları kur
- Kullanıcının tarzına, ilgi alanlarına adapte ol
- Sohbet tonunu ve akışını sürdür
- Konuyu değiştirmeye hazır ol ama geçişi doğal yap

## 🔷 SON KURAL — ALTIN İLKE
Sen sadece bilgi veren bir bot değilsin.
Sen Grit'in beyni, sesi ve yüzüsün.
Her cevabın bir insan kadar sıcak, bir uzman kadar doğru, bir arkadaş kadar samimi olsun.
Kalite standartın: "Bu cevabı okuyunca kanka WOW diyecek mi?" — Evet ise gönder. 🚀"""

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

# ===================== WEB ARAMA =====================
def web_ara(sorgu):
    """DuckDuckGo üzerinden ücretsiz web araması yapar"""
    try:
        encoded = urllib.parse.quote(sorgu)
        url = f"https://api.duckduckgo.com/?q={encoded}&format=json&no_html=1&skip_disambig=1"
        istek = urllib.request.Request(url)
        istek.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
        with urllib.request.urlopen(istek, timeout=10) as yanit:
            veri = json.loads(yanit.read().decode("utf-8"))
        
        sonuclar = []
        
        # Abstract (özet bilgi)
        if veri.get("AbstractText"):
            sonuclar.append(f"📌 {veri['AbstractText'][:500]}")
        
        # Answer (direkt cevap)
        if veri.get("Answer"):
            sonuclar.append(f"✅ Direkt Cevap: {veri['Answer']}")
        
        # İlgili konular
        if veri.get("RelatedTopics"):
            for topic in veri["RelatedTopics"][:3]:
                if isinstance(topic, dict) and topic.get("Text"):
                    sonuclar.append(f"• {topic['Text'][:200]}")
        
        if sonuclar:
            return "\n".join(sonuclar)
        return None
    except:
        return None

def arama_gerekli_mi(mesaj):
    """Mesajın web araması gerektirip gerektirmediğini kontrol eder"""
    arama_kelimeleri = [
        "anlık", "güncel", "şu an", "bugün", "şimdi", "son", "haber",
        "fiyat", "dolar", "euro", "bitcoin", "kripto", "borsa",
        "hava durumu", "hava", "sıcaklık",
        "kim kazandı", "maç", "skor", "sonuç",
        "ne zaman", "en yeni", "son dakika", "breaking",
        "2024", "2025", "2026", "bu yıl", "bu ay",
        "nedir", "kimdir", "nerede", "ne kadar",
        "ara", "araştır", "bul", "search", "google",
        "film", "dizi", "oyun", "çıktı mı", "yeni",
        "tarih", "ne zaman oldu"
    ]
    mesaj_lower = mesaj.lower()
    return any(kelime in mesaj_lower for kelime in arama_kelimeleri)

# ===================== AI =====================
def ai_yanit_al(mesajlar, web_sonucu=None):
    url = "https://api.groq.com/openai/v1/chat/completions"
    
    sistem = SISTEM_PROMPTU
    if web_sonucu:
        sistem += f"\n\n## 🌐 WEB ARAŞTIRMA SONUCU\n[WEB_SEARCH_RESULT]\n{web_sonucu}\n[/WEB_SEARCH_RESULT]\nBu bilgileri cevabına entegre et kanka!"
    
    veri = json.dumps({
        "model": "llama-3.3-70b-versatile",
        "messages": [{"role": "system", "content": sistem}] + mesajlar,
        "max_tokens": 1500,
        "temperature": 0.72,
        "top_p": 0.95,
        "frequency_penalty": 0.45,
        "presence_penalty": 0.35
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
            
            # Web araması gerekiyor mu kontrol et
            web_sonucu = None
            if arama_gerekli_mi(kullanici_mesaj):
                web_sonucu = await loop.run_in_executor(None, web_ara, kullanici_mesaj)
            
            bot_yaniti = await loop.run_in_executor(
                None, ai_yanit_al, sohbet_gecmisi[kullanici_id], web_sonucu
            )
        
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

# ===================== KOMUTLAR =====================
@bot.command(name="help")
async def yardim(ctx):
    embed = discord.Embed(
        title="Ewin AI",
        description="Grit sunucusunun resmi yapay zeka asistanı.\nBeni **@mention** at ve konuş — her konuda buradayım kanka!",
        color=0x5865F2
    )
    embed.set_thumbnail(url=ctx.bot.user.display_avatar.url)
    embed.add_field(
        name="🧠 Yapabileceklerim",
        value=(
            "• Kod yazar & hata düzeltirim\n"
            "• Matematik & bilim soruları çözerim\n"
            "• Hikaye, şiir, makale yazarım\n"
            "• **Anlık web araştırması** yaparım 🌐\n"
            "• Her konuda sohbet eder & analiz yaparım\n"
            "• Türkçe, İngilizce ve daha fazla dil desteklerim\n"
            "• Film, dizi, kitap, müzik önerisi yaparım"
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
            "`?ara [konu]` — Web araştırması yap\n"
            "`?sifirla` — Sohbet geçmişini temizle\n"
            "`/sor [mesaj]` — Slash komutla soru sor"
        ),
        inline=False
    )
    embed.add_field(
        name="📊 Seviye Sistemi",
        value="Benimle konuştukça XP kazan!\n🌱 → ⭐ → 🥉 → 🥈 → 🥇 → 🏆 → 💎 → 👑",
        inline=False
    )
    embed.set_footer(text="Ewin AI v4.0 • Grit Ekibi • LLaMA 3.3 70B + Web Arama", icon_url=ctx.bot.user.display_avatar.url)
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.reply(embed=embed)

@bot.command(name="ara")
async def ara_cmd(ctx, *, sorgu: str):
    async with ctx.channel.typing():
        loop = asyncio.get_event_loop()
        sonuc = await loop.run_in_executor(None, web_ara, sorgu)
    if sonuc:
        embed = discord.Embed(
            title=f"🔍 Araştırma: {sorgu}",
            description=sonuc[:2000],
            color=0x5865F2
        )
        embed.set_footer(text="DuckDuckGo aracılığıyla araştırıldı • Ewin AI")
        await ctx.reply(embed=embed)
    else:
        await ctx.reply(f"❌ '{sorgu}' için sonuç bulamadım kanka. Farklı bir şekilde dene!")

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
    embed.set_footer(text="Ewin AI v4.0 • Grit Ekibi")
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
        web_sonucu = None
        if arama_gerekli_mi(mesaj):
            web_sonucu = await loop.run_in_executor(None, web_ara, mesaj)
        yanit = await loop.run_in_executor(None, ai_yanit_al, sohbet_gecmisi[kullanici_id], web_sonucu)
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
