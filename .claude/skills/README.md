# Kurulu Skiller (Installed Skills)

Bu dizin, [claudeskills.info](https://claudeskills.info) üzerinden seçilip
**içeriği güvenlik açısından incelendikten sonra** kurulan Claude Code skillerini içerir.

Skiller "çalıştırılmaz"; ilgili bir görev geldiğinde Claude tarafından otomatik
olarak tetiklenir. Her skill bir `SKILL.md` dosyası ve (varsa) yardımcı dosyalar içerir.

## Kaynaklar ve Lisanslar

| Skill(ler) | Kaynak Repo | Lisans |
|------------|-------------|--------|
| Superpowers seti (14 skill: `using-superpowers`, `brainstorming`, `writing-plans`, `executing-plans`, `test-driven-development`, `systematic-debugging`, `requesting-code-review`, `receiving-code-review`, `subagent-driven-development`, `dispatching-parallel-agents`, `verification-before-completion`, `using-git-worktrees`, `finishing-a-development-branch`, `writing-skills`) | [obra/superpowers](https://github.com/obra/superpowers) | MIT (© 2025 Jesse Vincent) |
| `github-trending`, `parallax-landing-page`, `cinematic-scrub-landing`, `ux-design-systems`, `mobile-responsiveness`, `web-accessibility`, `figma`, `mermaid-diagrams`, `mongodb`, `owasp-security`, `video-edit`, `video-to-landing-page` | [hoodini/ai-agents-skills](https://github.com/hoodini/ai-agents-skills) | Lisans dosyası yok (kaynak repoda belirtilmemiş) |
| `pick-next-issue` | [tobihagemann/turbo](https://github.com/tobihagemann/turbo) | MIT (© 2026 Tobias Hagemann) |
| `postgres-patterns`, `mysql-patterns`, `database-migrations` | [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | MIT |
| `security-pen-testing`, `senior-security` | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | MIT |
| `image-to-code`, `design-code` | [plugin87/ux-ui-agent-skills](https://github.com/plugin87/ux-ui-agent-skills) | Lisans dosyası yok |
| `watch` | [alexlarcheveque/claude-watch](https://github.com/alexlarcheveque/claude-watch) | MIT (© 2026 Alex Larcheveque) |
| `public-apis` (veri) | [public-apis/public-apis](https://github.com/public-apis/public-apis) | MIT (© 2022 public-apis) |

## Kategorilere göre (2. parti kurulum)

- **Animasyonlu / geçiş efektli site tasarımı:** `parallax-landing-page`, `cinematic-scrub-landing`, `video-to-landing-page`
- **Görsel tasarım / tasarım sistemi:** `ux-design-systems`, `figma`, `mobile-responsiveness`, `web-accessibility`
- **SQL modelleri & üreteci:** `postgres-patterns`, `mysql-patterns`, `database-migrations`, ER diyagramları için `mermaid-diagrams`; NoSQL için `mongodb`
- **Güvenlik testi / "hacker gibi" (etik/yetkili):** `security-pen-testing`, `senior-security`, `owasp-security`
- **Video okuma / analizi:** `watch` (kare + transkript ile video izleme/hook analizi), `video-edit` (transkripsiyon), `video-to-landing-page`
- **Site özellik kopyalayıcı / görselden koda:** `image-to-code`, `design-code`, `figma`
- **API bulma / veri kaynağı:** `public-apis` (~1.900 ücretsiz/açık API'lik çevrimdışı katalog)

## Notlar

- **`using-superpowers`**: Superpowers setinin "dispatcher" skill'idir ve her yanıttan
  önce ilgili skillerin kullanılmasını agresif biçimde zorunlu kılar. Tasarımı gereği böyledir.
- **`pick-next-issue`**: Son adımında Turbo deposundaki `$turboplan` skill'ine referans
  verir; o skill kurulu olmadığından issue sıralama/öneri kısmı çalışır, planlama adımı
  atlanır. `gh` CLI gerektirir.
- **`github-trending`**: `github.com/trending` sayfasını scrape eden kod örnekleri sağlar;
  resmi bir API yoktur.
- **`video-edit` / `video-to-landing-page`**: Ağır dış bağımlılıklar ister
  (Whisper transkripsiyon, ffmpeg, HyperFrames, bazı adımlarda ElevenLabs API anahtarı).
  Kaynak repodaki `install.sh` bir `curl | bash` kurucusudur; **güvenlik gereği otomatik
  çalıştırılmadı**. Skill tanımları kuruldu ama tam çalışması için bu araçların ayrıca
  kurulması gerekir.
- **`watch`**: `/watch <url>` ile bir videoyu indirip (yt-dlp) kareleri ve sesi ayırır
  (ffmpeg), altyazı yoksa ElevenLabs Scribe veya Groq Whisper ile transkript çıkarır ve
  Claude'a kare + zaman damgalı transkripti birlikte verir. Kurulum notları:
  - **Gerekli dış araçlar:** `yt-dlp`, `ffmpeg`/`ffprobe`, `python3`, `shasum`.
    Kaynak repodaki `install.sh` **çalıştırılmadı** (brew ile paket kurmaya çalışıyor);
    dosyalar elle `.claude/skills/watch/` altına kopyalandı. Araçları kendi paket
    yöneticinizle kurun: `brew install yt-dlp ffmpeg` veya `apt install ffmpeg` + `pipx install yt-dlp`.
  - **API anahtarı (opsiyonel):** Yalnızca gömülü altyazısı olmayan videolar için gerekir.
    `.claude/skills/watch/.env.example` dosyasını `.env` olarak kopyalayıp
    `ELEVENLABS_API_KEY` veya `GROQ_API_KEY` girin. `.env` `.gitignore` ile dışarıda tutulur.
  - **Yapılan uyarlamalar:** (a) `SKILL.md` içindeki `bash skill/watch.sh` yolu kurulu
    dizine göre düzeltildi; (b) `--mode retention|library` için hatalı prompt dosya adı
    (`<mode>-analysis.md`) gerçek dosyalarla eşlendi; (c) `.env` artık skill dizininin
    içinde de aranıyor; (d) HTML raporu açma adımı Linux'ta `xdg-open`, başlık yoksa
    "sadece yolu yazdır" olacak şekilde genişletildi; (e) kaynak reponun kökündeki
    `templates/hook-library.md`, `retention-report.md`, `batch-urls.csv.example`
    dosyaları skill'in `templates/` klasörüne dahil edildi.
  - **Maliyet:** Her çalıştırmada `/tmp/watch/<slug>/cost.json` yazılır; varsayılan
    fiyat sabitleri Opus 4.7'ye göredir, `WATCH_RATE_*` ortam değişkenleriyle değiştirilebilir.
- **`public-apis`**: Kaynak repo **bir skill değildir** — 269 KB'lik bir `README.md`
  içinde topluluk tarafından derlenmiş API listesi ve CI'ın kullandığı link doğrulama
  script'lerinden ibarettir. Bu yüzden olduğu gibi kopyalanmadı; API tabloları
  `scripts/build-catalog.py` ile ayrıştırılıp `references/apis.csv` +
  `references/apis.md` (1888 API, 51 kategori) hâline getirildi, üstüne `SKILL.md` ve
  `scripts/find-api.py` arama yardımcısı **bu repo için yazıldı**. Notlar:
  - Katalog dosyaları ~240 KB'dir; `SKILL.md` bunları baştan sona okumayı yasaklar,
    önce arama yapılmasını söyler: `python3 .claude/skills/public-apis/scripts/find-api.py
    weather --no-auth --limit 5`. Dış bağımlılık yok, `python3` yeterli.
  - Veri **anlık bir kopyadır** (upstream commit + tarih `SOURCE.md` içinde) ve
    topluluk derlemesidir: endpoint'ler kapanabilir, ücretsiz katmanlar kalkabilir,
    `auth`/`https`/`cors` sütunları eskimiş olabilir. `SKILL.md` bunu her yanıtta
    belirtmeyi ve sağlayıcının kendi dokümanından doğrulamayı şart koşar.
  - Upstream'in en üstündeki APILayer sponsor/tanıtım bloğu ve CI script'leri dahil
    edilmedi. Katalog `build-catalog.py` ile upstream'den yeniden üretilebilir.
- **`security-pen-testing` / `senior-security`**: Yalnızca **yetkili/etik** güvenlik testi
  içindir; sorumlu ifşa (responsible disclosure) kurallarını ve "veriyi exfiltrate etme"
  ilkesini içerir. İzniniz olmayan sistemlerde kullanılamaz.
- Bu skiller Anthropic'in resmi skilleri değildir; üçüncü taraf topluluk katkılarıdır.

## İstenen ama kurulmayan

- **`tdd-guide`**: claudeskills.info bunu `alirezarezvani/claude-skills` deposunda
  gösteriyordu, ancak o repoda böyle bir skill **yok** (aggregator verisi hatalı).
  TDD ihtiyacı Superpowers'ın `test-driven-development` skill'i ile karşılanmıştır.
