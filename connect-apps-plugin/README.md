# connect-apps-plugin

Harici uygulamaları ve servisleri güvenli şekilde bağlamak için bir Claude Code eklentisi.
İçinde `connect-apps` skill'i bulunur: OAuth/OIDC, API anahtarı & token yönetimi, webhook
kurulumu ve doğrulaması, hız sınırı/yeniden deneme stratejileri ve uygulamalar arası veri
senkronizasyonu için rehber.

## Yükleme

```bash
claude --plugin-dir ./connect-apps-plugin
```

## İçerik

```
connect-apps-plugin/
├── .claude-plugin/
│   └── plugin.json          # Eklenti manifesti
├── skills/
│   └── connect-apps/
│       └── SKILL.md         # "Uygulama bağlama rehberi" skill'i
└── README.md
```

## Kullanım

Eklenti yüklendikten sonra, bir servisi entegre ederken skill otomatik olarak devreye girer;
ya da doğrudan çağırmak için "uygulama bağla", "OAuth ekle", "webhook kur", "API entegrasyonu"
gibi ifadeler kullanın.
