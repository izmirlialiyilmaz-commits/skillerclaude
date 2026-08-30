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

## İstenen ama kurulmayan

- **`tdd-guide`**: claudeskills.info bunu `alirezarezvani/claude-skills` deposunda
  gösteriyordu, ancak o repoda böyle bir skill **yok** (aggregator verisi hatalı).
  TDD ihtiyacı Superpowers'ın `test-driven-development` skill'i ile karşılanmıştır.
