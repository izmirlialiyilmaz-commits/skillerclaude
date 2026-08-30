# Kurulu Skiller (Installed Skills)

Bu dizin, [claudeskills.info](https://claudeskills.info) üzerinden seçilip
**içeriği güvenlik açısından incelendikten sonra** kurulan Claude Code skillerini içerir.

Skiller "çalıştırılmaz"; ilgili bir görev geldiğinde Claude tarafından otomatik
olarak tetiklenir. Her skill bir `SKILL.md` dosyası ve (varsa) yardımcı dosyalar içerir.

## Kaynaklar ve Lisanslar

| Skill(ler) | Kaynak Repo | Lisans |
|------------|-------------|--------|
| Superpowers seti (14 skill: `using-superpowers`, `brainstorming`, `writing-plans`, `executing-plans`, `test-driven-development`, `systematic-debugging`, `requesting-code-review`, `receiving-code-review`, `subagent-driven-development`, `dispatching-parallel-agents`, `verification-before-completion`, `using-git-worktrees`, `finishing-a-development-branch`, `writing-skills`) | [obra/superpowers](https://github.com/obra/superpowers) | MIT (© 2025 Jesse Vincent) |
| `github-trending` | [hoodini/ai-agents-skills](https://github.com/hoodini/ai-agents-skills) | Lisans dosyası yok (kaynak repoda belirtilmemiş) |
| `pick-next-issue` | [tobihagemann/turbo](https://github.com/tobihagemann/turbo) | MIT (© 2026 Tobias Hagemann) |

## Notlar

- **`using-superpowers`**: Superpowers setinin "dispatcher" skill'idir ve her yanıttan
  önce ilgili skillerin kullanılmasını agresif biçimde zorunlu kılar. Tasarımı gereği böyledir.
- **`pick-next-issue`**: Son adımında Turbo deposundaki `$turboplan` skill'ine referans
  verir; o skill kurulu olmadığından issue sıralama/öneri kısmı çalışır, planlama adımı
  atlanır. `gh` CLI gerektirir.
- **`github-trending`**: `github.com/trending` sayfasını scrape eden kod örnekleri sağlar;
  resmi bir API yoktur.
- Bu skiller Anthropic'in resmi skilleri değildir; üçüncü taraf topluluk katkılarıdır.

## İstenen ama kurulmayan

- **`tdd-guide`**: claudeskills.info bunu `alirezarezvani/claude-skills` deposunda
  gösteriyordu, ancak o repoda böyle bir skill **yok** (aggregator verisi hatalı).
  TDD ihtiyacı Superpowers'ın `test-driven-development` skill'i ile karşılanmıştır.
