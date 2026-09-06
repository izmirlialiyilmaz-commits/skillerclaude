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
| `impeccable` (+ 4 alt-agent) | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | Apache-2.0 (© Paul Bakaus) |
| `ui-ux-pro-max` | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | MIT (© NextLevelBuilder) |

## Kategorilere göre (2. parti kurulum)

- **Animasyonlu / geçiş efektli site tasarımı:** `parallax-landing-page`, `cinematic-scrub-landing`, `video-to-landing-page`
- **Görsel tasarım / tasarım sistemi:** `ux-design-systems`, `figma`, `mobile-responsiveness`, `web-accessibility`
- **SQL modelleri & üreteci:** `postgres-patterns`, `mysql-patterns`, `database-migrations`, ER diyagramları için `mermaid-diagrams`; NoSQL için `mongodb`
- **Güvenlik testi / "hacker gibi" (etik/yetkili):** `security-pen-testing`, `senior-security`, `owasp-security`
- **Video okuma / analizi:** `video-edit` (transkripsiyon), `video-to-landing-page`
- **Site özellik kopyalayıcı / görselden koda:** `image-to-code`, `design-code`, `figma`

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
- **`security-pen-testing` / `senior-security`**: Yalnızca **yetkili/etik** güvenlik testi
  içindir; sorumlu ifşa (responsible disclosure) kurallarını ve "veriyi exfiltrate etme"
  ilkesini içerir. İzniniz olmayan sistemlerde kullanılamaz.
- Bu skiller Anthropic'in resmi skilleri değildir; üçüncü taraf topluluk katkılarıdır.

## Claude Code Tasarım Kiti (v1 PDF'inden kurulanlar)

Kaynak: "Claude Code Tasarım Skilleri · Kurulum Kiti v1" (@burhankocabiyik) PDF'i.
PDF 4 araç öneriyordu; hepsi kuruldu:

| # | Araç | Ne yapar | Bu repoda nerede |
|---|------|----------|------------------|
| 1 | **SkillUI** | Herhangi bir siteyi/repo'yu statik analizle tarar; renk, font, spacing, animasyon ve componentleri `.skill` dosyasına paketler. AI/API anahtarı gerektirmez. | npm CLI — repoya kopyalanmaz. `npm install -g skillui` |
| 2 | **Impeccable** | 23 alt-komutlu tasarım skill'i (`polish`, `audit`, `critique`, `bolder`, `quieter`, `animate`, `layout`, ...). "AI slop" görünümünü üretim anında engeller. | `.claude/skills/impeccable/` + `.claude/agents/impeccable-*.md` |
| 3 | **UI/UX Pro Max** | Yerel, aranabilir tasarım-zekâsı veritabanı: 192 renk paleti, 74 font eşleşmesi, 79 stil, 119 UX kuralı, 25 grafik tipi, 22 tech stack. | `.claude/skills/ui-ux-pro-max/` |
| 4 | **Playwright MCP** | Claude'un tarayıcıda gezinip ekran görüntüsü alarak tasarımı *görerek* doğrulaması. | Depo kökündeki `.mcp.json` |

### Kurulum notları / PDF'ten sapmalar

- **SkillUI bir skill değil, npm CLI'ı.** `.claude/skills/` altına kopyalanacak bir şeyi yok;
  siteyi taratıp ürettiği `.skill` klasörünü sonradan projeye eklersin.
  PDF'te kaynak repo olarak `github.com/amaancoderx/skillui` yazıyor ama **o repo paketin
  tanıtım sitesi** (Next.js landing). CLI'ın gerçek kaynağı
  [amaancoderx/npxskillui](https://github.com/amaancoderx/npxskillui), npm paketi `skillui` (MIT).
  Kullanım: `skillui --url https://ornek.com --mode ultra`
- **Impeccable**: PDF `cp -r impeccable/skill ~/.claude/skills/impeccable` diyor, ama repodaki
  `skill/` klasörü `SKILL.src.md` şablonu (`{{scripts_path}}` gibi doldurulmamış placeholder'lar içerir).
  Onun yerine deponun **derlenmiş** `.claude/skills/impeccable/` çıktısı kuruldu (SKILL.md v4.2.1).
  SKILL.md dört alt-agent'a referans verdiği için `.claude/agents/` altındaki 4 agent de kopyalandı.
- **Impeccable motoru**: `scripts/impeccable` sadece bir launcher; ilk çalıştırmada platforma uygun
  binary'yi **projenin kendi GitHub Releases** adresinden (`pbakaus/impeccable`, `engine-v*` tag)
  `~/.impeccable/bin/` altına indirir. Repoya binary konmadı; her makinede ilk kullanımda iner.
- **UI/UX Pro Max**: Resmî yol `npx ui-ux-pro-max-cli init --ai claude`; burada aynı içerik doğrudan
  deponun `.claude/skills/ui-ux-pro-max/` çıktısından kuruldu (v2.13.0). Arama scripti **Python 3**
  ister (yalnızca standart kütüphane, ağ erişimi yok).
  Aynı depo `design`, `ui-styling`, `brand`, `design-system`, `slides`, `banner-design` adlı 6 ek skill
  daha içeriyor; PDF'te geçmedikleri ve mevcut skillerle örtüştükleri için **kurulmadı**.
- **Playwright MCP**: `claude mcp add ...` komutu kullanıcı düzeyine yazar; onun yerine depo köküne
  proje kapsamlı `.mcp.json` eklendi — depoyu klonlayan herkeste geçerli olur.
  CLI alternatifi isteyenler için: `npm install -g @playwright/cli@latest`.

### Doğrulama (bu oturumda çalıştırıldı)

- `impeccable --version` → `4.0.0` (engine binary indi, launcher çalışıyor)
- `search.py "fintech dashboard" --domain color` → palet sonuçları döndü
- `skillui --version` → `1.3.4`
- `npx @playwright/mcp@latest --version` → `0.0.80`

### Önerilen zincir

`SkillUI` (referans siteyi çıkar) → `Impeccable` (cilala) → `UI/UX Pro Max` (renk/font doğrula)
→ `Playwright` (ekran görüntüsüyle gözle doğrula).
PDF'te örnek olarak verilen [tpj-collective/design-skill-pipeline](https://github.com/tpj-collective/design-skill-pipeline)
deposu bu zinciri tek pipeline'da birleştiriyor (kurulmadı, sadece referans).

## İstenen ama kurulmayan

- **`tdd-guide`**: claudeskills.info bunu `alirezarezvani/claude-skills` deposunda
  gösteriyordu, ancak o repoda böyle bir skill **yok** (aggregator verisi hatalı).
  TDD ihtiyacı Superpowers'ın `test-driven-development` skill'i ile karşılanmıştır.
