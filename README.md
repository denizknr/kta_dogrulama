# KTA Dogrulama — Frappe Custom App

**TEST ve FORM MASASI APARAT DOĞRULAMA KAYIT FORMU**  
Form No: PTR 07/222–02 | KTA Endüstri

---

## Içerik

Bu Frappe uygulaması 3 DocType içerir:

| DocType | Tür | Açıklama |
|---|---|---|
| `Test Masasi Dogrulama Kaydi` | Ana form | Tüm doğrulama kaydı |
| `Degerlendirme Kriteri` | Child Table | 12 sabit değerlendirme sorusu |
| `Baglanti Noktasi Satiri` | Child Table | 5 satırlı bağlantı noktası tablosu |

---

## Kurulum

### Gereksinimler

- Frappe Framework v14 veya v15
- ERPNext (isteğe bağlı)
- Çalışan bir `frappe-bench` ortamı

### Adım 1 — Uygulamayı bench'e ekle

```bash
cd /home/frappe/frappe-bench

# Replit'ten indirdiyseniz: frappe_app/kta_dogrulama klasörünü
# sunucunuza kopyalayın, ardından:
bench get-app kta_dogrulama /path/to/kta_dogrulama

# Veya git reposundan (bir git reposuna yüklediyseniz):
bench get-app kta_dogrulama https://github.com/KULLANICI_ADINIZ/kta_dogrulama
```

### Adım 2 — Siteye yükle

```bash
bench --site SITE_ADINIZ install-app kta_dogrulama
```

> `SITE_ADINIZ` yerine kendi sitenizi yazın, örneğin: `mysite.localhost`

### Adım 3 — Migrate et

```bash
bench --site SITE_ADINIZ migrate
```

### Adım 4 — Sunucuyu yeniden başlat

```bash
bench restart
```

---

## Kullanım

Kurulum tamamlandıktan sonra:

1. ERPNext / Frappe arayüzüne giriş yapın
2. Sol menüde **KTA Dogrulama** modülünü bulun
3. **Test Masasi Dogrulama Kaydi** → **New** butonuna tıklayın
4. Formu doldurun:
   - Kayıt bilgilerini girin (Test Masası No, Ürün No, vb.)
   - **Bağlantı Noktası Tablosu** otomatik olarak 5 satırla açılır → Görüyor / Görmüyor seçin
   - **Değerlendirme Kriterleri** tablosu 12 sabit soruyla otomatik dolar → Evet / Hayır seçin
   - Fotoğraf eklemek için "Fotoğraflar" bölümünden dosya yükleyin
5. **Save** ile kaydedin

---

## DocType Alanları — Ana Form

| Alan | Tip | Zorunlu | Açıklama |
|---|---|---|---|
| test_masasi_no | Data | ✓ | Belgenin adı (otomatik ID) |
| urun_no | Data | ✓ | Ürün numarası |
| urun_siparis_no | Data | ✓ | Sipariş numarası |
| baglanti_nokta_sayisi | Int | ✓ | Bağlantı nokta sayısı |
| revizyon_no | Data | ✓ | Revizyon numarası |
| test_cihaz_no | Data | ✓ | Test cihazı numarası |
| test_cihazi | Data | — | Test cihazı adı/modeli |
| dogrulama_nedeeni | Select | ✓ | İlk Devreye Alma / Proses Doğrulama / Revizyon |
| tarih | Datetime | ✓ | Kayıt tarihi (varsayılan: şimdiki an) |
| sayfa_no | Data | — | Sayfa numarası |
| toplam_sayfa | Data | — | Toplam sayfa sayısı |
| baglanti_noktasi_tablosu | Table | — | Bağlantı Noktası Satiri child table |
| baglanti_noktasi_notlari | Small Text | — | Bağlantı noktası notları |
| degerlendirme_kriterleri | Table | — | Degerlendirme Kriteri child table |
| resimler | Attach Multiple | — | Fotoğraf ekleri |
| uygulama_metni | Long Text | — | Sabit UYGULAMA açıklaması (salt okunur) |

---

## Değerlendirme Kriterleri (12 Sabit Soru)

Yeni kayıt oluşturulduğunda aşağıdaki sorular otomatik eklenir:

1. Test masası elektriksel bağlantıları uygun mu?
2. Test masası üstünde, işin doğru ve çabuk yapılabilmesi için anlaşılabilir işaretler ve uyarıcı yazılar kullanılmış mı?
3. Test masası üzerinde test masası numarası var mı?
4. Yapılan işaretler ve yazılar anlaşılır ve okunaklı mı?
5. Tüm Soket ve Komponentler için gerekli 3D yazıcıyla POKE-YOKE ler yapılmış mı?
6. Varlık kontrollü var mı ve switchler yaylı pim olarak mevcut mu?
7. Soket ve komponentlerin takılacağı yuva ve pimler sağlam bir şekilde monte edilmiş ve işin yapılması sırasında gevşememesi sağlanmış mı?
8. Test masasında kullanılan pimlerin kablo, kontak ve soket gibi üründe kullanılan parçalara zarar vermeyecek şekilde olmasına dikkat edilmiş mi?
9. Test masası üzerinde hedef noktalarda kablo renkleri belirtilmiş mi?
10. Renk kodlamaları ve etiketler doğru mu?
11. Test masası üzerinde hedef noktalar birbirinden farklı olarak numaralandırılmış mı?
12. Test masasındaki yazılı tanımlandırmaların, uygulama ve uyarı şekillerinin üstü kullanım sırasında yıpranmaya karşı şeffaf bir bant ile korunmaya alınmış mı?

---

## Bağlantı Noktası Tablosu (5 Sabit Satır)

| Nr. | Tanımı |
|---|---|
| 1 | Kilit Sistemi |
| 2 | Uç Sayısı |
| 3 | Poke-Yoke |
| 4 | Board Görsel |
| 5 | Board Çizim |

---

## Dosya Yapısı

```
kta_dogrulama/
├── README.md
├── requirements.txt
├── setup.py
├── MANIFEST.in
└── kta_dogrulama/
    ├── __init__.py
    ├── hooks.py
    ├── modules.txt
    ├── setup.py
    └── doctype/
        ├── test_masasi_dogrulama_kaydi/
        │   ├── __init__.py
        │   ├── test_masasi_dogrulama_kaydi.json   ← Ana DocType tanımı
        │   └── test_masasi_dogrulama_kaydi.py     ← Python controller
        ├── degerlendirme_kriteri/
        │   ├── __init__.py
        │   ├── degerlendirme_kriteri.json
        │   └── degerlendirme_kriteri.py
        └── baglanti_noktasi_satiri/
            ├── __init__.py
            ├── baglanti_noktasi_satiri.json
            └── baglanti_noktasi_satiri.py
```

---

## Lisans

MIT — KTA Endüstri
