---
name: connect-apps
description: Harici uygulamaları ve servisleri bir uygulamaya bağlamak için rehber. OAuth 2.0 / OpenID Connect ile yetkilendirme, API anahtarı ve token yönetimi, webhook kurulumu ve doğrulaması, REST/GraphQL çağrıları, hız sınırı (rate limit) ve yeniden deneme (retry) stratejileri, ve uygulamalar arası veri senkronizasyonu için kullanın. Slack, Google, GitHub, Stripe, Notion gibi üçüncü taraf servislerini entegre ederken; "uygulamayı bağla", "OAuth ekle", "webhook kur", "API entegrasyonu", "connect app", "integrate service" gibi ifadelerde tetiklenir.
---

# Connect Apps — Uygulama Bağlama Rehberi

Bu skill, bir uygulamayı harici bir servise (Slack, Google, GitHub, Stripe, Notion, vb.)
bağlarken izlenecek adımları ve güvenlik kurallarını tanımlar. Amaç: entegrasyonun
**güvenli**, **dayanıklı** (hatalara karşı) ve **bakımı kolay** olması.

## Ne zaman kullanılır

- Üçüncü taraf bir servisle OAuth/OIDC üzerinden kullanıcı yetkilendirmesi kurarken
- API anahtarı, gizli anahtar (secret) veya token saklarken ve yenilerken
- Bir servisten olay almak için webhook kurarken ve doğrularken
- REST/GraphQL API çağrıları yaparken (sayfalama, hız sınırı, yeniden deneme)
- İki uygulama arasında veri senkronize ederken

## 0. Önce netleştir

Kod yazmadan önce şunları belirle:

1. **Yön**: Veriyi biz mi çekiyoruz (pull), servis mi bize gönderiyor (push/webhook), yoksa çift yönlü mü?
2. **Kimlik doğrulama tipi**: Kullanıcı adına mı (OAuth) yoksa sunucu-sunucu mu (API key / service account)?
3. **Kapsam (scope)**: Servisin hangi izinleri gerekiyor? En az yetki (least privilege) ilkesini uygula.
4. **Ortam**: Geliştirme/üretim ayrı kimlik bilgileri (credentials) kullanmalı.

## 1. Kimlik doğrulama (Authentication)

### OAuth 2.0 / OIDC (kullanıcı adına erişim)

Kullanıcının verisine onun adına erişecekse **Authorization Code + PKCE** akışını kullan:

1. Kullanıcıyı servisin yetkilendirme URL'sine yönlendir (`client_id`, `redirect_uri`, `scope`, `state`, `code_challenge`).
2. `state` parametresini üret, oturumda sakla ve dönüşte **mutlaka doğrula** (CSRF koruması).
3. Dönen `code`'u backend'de access + refresh token ile takas et. Bu takas **asla tarayıcıda** yapılmaz.
4. Token'ı süresi dolduğunda `refresh_token` ile sessizce yenile.

> Implicit flow **kullanma** — güvenli değildir ve kullanımdan kaldırılmıştır.

### API anahtarı / servis hesabı (sunucu-sunucu)

- Anahtarları **koddan uzak tut**: ortam değişkeni (env var) veya bir gizli anahtar yöneticisi (Vault, AWS Secrets Manager, GCP Secret Manager) kullan.
- Anahtarları `.env` içine koy ve `.env`'i **`.gitignore`'a ekle**. Depoya sızmışsa hemen döndür (rotate).
- Mümkünse anahtarları IP veya kapsam ile kısıtla.

## 2. Token ve secret yönetimi

- Token'ları şifreli olarak (at-rest encryption) sakla; düz metin veritabanı alanında tutma.
- Refresh token'a access token'dan daha katı erişim uygula.
- Sızma durumuna karşı **döndürme (rotation)** ve **iptal (revocation)** yolunu baştan planla.
- Loglara token, secret veya `Authorization` header'ı **yazma** — maskele.

## 3. Webhook alma (servis → biz)

Bir servisten olay dinleyeceksen:

1. **İmza doğrula**: Gelen her isteği paylaşılan secret ile imzayla doğrula (ör. Stripe `Stripe-Signature`, GitHub `X-Hub-Signature-256` HMAC-SHA256). Doğrulanmayan isteği reddet.
2. **Ham gövdeyi (raw body) kullan**: İmza, gövdenin ayrıştırılmadan (parse edilmeden) önceki ham hâli üzerinden hesaplanır.
3. **Hızlı 2xx dön**: İşlemeyi kuyruğa (queue) al, senkron yapma; servisler zaman aşımında tekrar dener.
4. **Idempotent ol**: Aynı olay ID'si iki kez gelebilir; işlenmiş olay ID'lerini kaydet ve tekrarını yok say.
5. **Zaman damgası kontrolü**: Çok eski istekleri (replay saldırısı) reddet.

## 4. API çağrıları (biz → servis)

- **Hız sınırı (rate limit)**: `Retry-After` ve `X-RateLimit-*` header'larına uy. Sınıra takılınca bekle.
- **Yeniden deneme (retry)**: Yalnızca geçici hatalarda (429, 5xx, ağ hatası) **üstel geri çekilme (exponential backoff) + jitter** ile tekrar dene. 4xx (429 hariç) tekrar edilmez.
- **Zaman aşımı (timeout)**: Her isteğe makul bir timeout koy; sonsuz bekleme olmasın.
- **Sayfalama (pagination)**: Cursor veya offset tabanlı sayfalamayı sonuna kadar takip et.
- **Devre kesici (circuit breaker)**: Servis sürekli hata veriyorsa bir süre çağrıyı durdur.

## 5. Veri senkronizasyonu

- **Delta senkronizasyon**: Mümkünse her seferinde her şeyi değil, son senkrondan bu yana değişenleri çek (`updated_since`, cursor).
- **Çakışma çözümü (conflict resolution)**: İki tarafta da değişen kayıtlar için net bir kural belirle (son yazan kazanır, alan bazlı birleştirme, vb.).
- **Eşleme (mapping)**: Yerel kimlikler ile uzak kimlikler arasında bir eşleme tablosu tut.
- **Gözlemlenebilirlik**: Senkron durumu, son başarılı zaman ve hataları logla; başarısızlıkta uyarı ver.

## 6. Bitirmeden önce kontrol listesi

- [ ] Secret'lar koddan ve versiyon kontrolünden uzak, `.gitignore` güncel
- [ ] OAuth'ta `state` doğrulanıyor, token takası backend'de
- [ ] Webhook imzası ham gövde üzerinden doğrulanıyor, işleme idempotent
- [ ] API çağrılarında timeout, retry-with-backoff ve rate-limit uyumu var
- [ ] Token yenileme ve iptal yolu mevcut
- [ ] Hatalar loglanıyor ama secret'lar maskeleniyor
- [ ] Geliştirme ve üretim için ayrı kimlik bilgileri
