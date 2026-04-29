import streamlit as st
import os

# --- SAYFA AYARLARI ---
st.set_page_config(
    page_title="KAEÜ Parazitoloji Veri Bankası", 
    page_icon="🔬",
    layout="wide"
)

# --- STİL (CSS) ---
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stExpander { border: 1px solid #8b0000; border-radius: 10px; margin-bottom: 5px; }
    .tree-node { 
        padding: 10px; 
        border-left: 3px solid #8b0000; 
        background-color: white; 
        margin-left: 20px;
        margin-top: 5px;
        border-radius: 5px;
    }
    .category-header {
        color: #8b0000;
        font-weight: bold;
        text-transform: uppercase;
        border-bottom: 2px solid #8b0000;
    }
    </style>
    """, unsafe_allow_html=True)

# --- GENİŞLETİLMİŞ VERİ SETİ ---
parazit_verisi = {
   # --- AMİPLER (AMEBAE) VERİ SETİ ---
    " : blue[Entamoeba histolytica]": {
        "bilgi": """Entamoeba histolytica, dünya genelinde (özellikle tropikal bölgelerde) yaygın görülen, patojenik ve tek hücreli bir anaerop protozoondur. İnsanlarda asemptomatik taşıyıcılıktan ölümcül dizanteriye ve karaciğer apselerine kadar geniş bir klinik yelpazeye neden olur.

**1. Morfoloji ve Hayat Döngüsü**
Parazitin hayat döngüsü; trofozoit, prekist, kist, metakist ve metakistik trofozoit evrelerinden oluşur.
**Trofozoit:** Aktif hareket eden, beslenen ve çoğalan formdur. Lobopod adı verilen yalancı ayaklarla hareket eder. Sitoplazmasında fagosite edilmiş alyuvarlar (eritrosit) bulunabilir; bu özellik teşhiste önemlidir.
**Kist:** Parazitin dış ortama ve mide asidine dirençli, enfektif formudur. Olgun kist 4 çekirdeklidir. İçerisinde uçları yuvarlak kromatoid cisimcikler bulunur.
**Döngü:** Ağız yoluyla alınan 4 çekirdekli olgun kistler, ince bağırsakta metakistik trofozoitlere dönüşerek kalın bağırsağa yerleşirler.

**2. Patogenez ve Klinik Belirtiler**
Parazit, Gal/GalNAc lektin aracılığıyla bağırsak epiteline yapışır.
**Amibik Dizanteri:** Kanlı-mukuslu dışkılama, karın ağrısı ve tenesmus ile karakterizedir.
**Şişe Biçimli Ülserler:** Parazit submukozaya yayılarak tipik kraterimsi, dar ağızlı ülserler oluşturur.
**Ekstraintestinal Amoebiosis:** En sık karaciğerde (sağ lopta tek apse) görülür. Akciğer, beyin ve deri tutulumları izleyebilir.

**3. Epidemiyoloji ve Bulaşma**
Bulaşma yolu fekal-oral (dışkı-ağız) yoldur. Kontamine su ve gıdalar, kirli eller ve vektörler (karasinek/hamamböceği) ana rol oynar.

**4. Tanı Yöntemleri**
**Mikroskopi:** Dışkıda trofozoit veya kist aranır. Lugol veya kalıcı boyalar (Trikrom) kullanılır.
**Seroloji:** Bağırsak dışı vakaların %95'inde antikor testleri (ELISA) pozitiftir.
**Antijen/Moleküler:** PCR yöntemleri, E. histolytica ile E. dispar ayrımı için altın standarttır.

**5. Tedavi ve Kontrol**
**İlaç Tedavisi:** İnvaziv vakalarda Metronidazol, tinidazol; luminal taşıyıcılıkta Paromomisin kullanılır.
**Korunma:** Temiz içme suyu, altyapı iyileştirmesi ve el yıkama alışkanlığı temeldir.""",
        "resim": "parazit_program/Entamoeba_histolytica.png"
    },
     "Entamoeba coli": {
           "BİLGİ": """İnsanın kalın bağırsağında kommensal olarak yaşayan, genellikle apatojen kabul edilen bir protozoondur. Klinik pratikte iki temel nedenden dolayı büyük önem taşır:
**Ayırıcı Tanı:** Morfolojik olarak patojen olan E. histolytica ile sıklıkla karıştırılması.

**Hijyen İndikatörü:** Saptanması, hastanın fekal kontaminasyona (sanitasyon eksikliği) maruz kaldığının kesin bir göstergesidir.

Trofozoit Dönemi Ayırıcı Özellikleri (20-40 µm)
**E. coli trofozoitini E. histolytica'dan ayıran temel farklar şunlardır:**
**Hareket:** Çok yavaştır; ektoplazma ve endoplazma ayrımı belirgin değildir.
**Sitoplazma İçeriği:** Endoplazmasında asla eritrosit bulunmaz (sadece bakteri ve artıklar görülür).
**Çekirdek Yapısı:** Boyalı preparatlarda karyozom (çekirdekçik) asantral (merkez dışı) yerleşimlidir. Çekirdek zarı üzerindeki kromatin tanecikleri düzensiz ve kaba dizilmiştir. Dört Çekirdekli Kistlerin Ayrımı

E. coli'nin olgunlaşmamış (4 çekirdekli) kistleri ile E. histolytica'nın olgun kistlerini karıştırmamak için şu **iki noktaya** bakılır:
Vakuol Varlığı: E. coli'nin 4 çekirdekli kistlerinde genellikle büyük bir glikojen vakuolü bulunur. E. histolytica'nın olgun kistinde ise bu vakuol tüketilmiştir.
Görülme Sıklığı: E. coli'nin 4 çekirdekli formu dışkıda nadir görülür; genellikle :red[8 çekirdekli] olgun form hakimdir.

**Bulaş ve Epidemiyoloji**
Bulaş Yolu: 8 veya 16 çekirdekli olgun kistlerin kontamine gıda, su veya kirli eller aracılığıyla (fekal-oral) ağızdan alınmasıyla gerçekleşir.
Çevresel Direnç: E. coli kistleri dış çevre koşullarına E. histolytica'dan çok daha dirençlidir. Bu nedenle saha taramalarında E. coli görülme sıklığı, E. histolytica'dan en az iki kat daha fazladır."""
    },
    "Entamoeba dispar": {
        "BİLGİ": """Entamoeba dispar, morfolojik açıdan E. histolytica ile birebir benzerlik gösterir ve mikroskobik incelemelerde ayırt edilemezler.

**Klinik Önem**
E. dispar nonpatojen (hastalık yapmayan) bir amip olarak kabul edilir. Yanlış tanı ve gereksiz tedaviyi önlemek için ayrımı kritiktir.

**Raporlama Standartları**
Sadece mikroskopiye dayanarak tür tanımı yapılamaz. Laboratuvar sonuçlarına "Entamoeba histolytica / Entamoeba dispar" (kompleks) şeklinde kaydedilmelidir.

**Ayırıcı Tanı Yöntemleri**
**ELISA (Antijen Tayini):** Adezin antijenine spesifik kitlerle ayrım yapılabilir.
**PCR (Moleküler Tanı):** Tür düzeyinde ayrım sağlayan altın standart yöntemdir."""
    },

    "Entamoeba hartmanni": {
        "BİLGİ": """Eskiden E. histolytica'nın "küçük formu" olarak tanımlanan bu tür, morfolojik olarak benzer olsa da boyutlarıyla ayrılır.

**Yerleşim:** Kalın bağırsak.
**Morfoloji:** Trofozoit 3-12 µm, kist 4-10 µm boyutundadır. Kistinde 2-4 adet çekirdek bulunur ve kromatoid cisimcikleri "puro" şeklindedir.
**Patojenite:** Apatojen kabul edilir ve genellikle tedavi gerektirmez."""
    },

    "Entamoeba polecki": {
        "BİLGİ": """Temel olarak domuz ve maymunlarda parazitlenen, ancak zoonotik bir geçişle insanlarda da yerleşebilen bir amip türüdür.

**Epidemiyoloji ve Konakçılık**
**Asıl Konakçı:** Domuzlar ve maymunlar. Kalın bağırsakta yerleşir. Papua Yeni Gine'de yüksek prevalans gösterir.

**Morfolojik Özellikler**
**Trofozoit:** E. coli'ye büyük benzerlik gösterir.
**Kist:** Tipik olarak tek çekirdeklidir (ayırıcı özellik).
**Kromatoid Cisimcikler:** E. histolytica ile benzerlik taşır.

**Klinik Durum**
İnsanlar için patojen kabul edilmektedir. Standart tedavi protokolleri henüz tam aydınlatılmamıştır."""
    },

    "Endolimax nana": {
        "BİLGİ": """İnsan kalın bağırsağında kommensal olarak yaşayan ve klinik olarak apatojen kabul edilen bir protozoondur.

**1. Trofozoit Dönemi**
**Boyut:** 5-12 µm. Oldukça yavaş hareket eder. Çekirdek içinde büyük ve merkezi bir karyozom bulunur. Endoplazmada asla eritrosit görülmez.

**2. Kist Dönemi**
**Şekil:** Genellikle ovaldir. Olgunlaşmış kistlerde dört adet çekirdek bulunur.

**Klinik Durum**
Apatojen olarak sınıflandırılır; ancak saptanması, hastanın hijyen eksikliğine veya fekal kontaminasyona maruz kaldığının göstergesidir."""
    },

    "Iodamoeba bütschlii": {
        "BİLGİ": """İnsan kalın bağırsağında yaşayan ve adını kist evresindeki belirgin iyot tutulumundan alan bir protozoondur.

**1. Kist Dönemi (En Tipik Formu)**
**Glikojen Vakuolü:** Kist içinde sitoplazmayı kaplayan büyük bir glikojen vakuolü bulunur. Lugol (İyot) ile boyandığında koyu kahverengi görünür.
**Boyut:** 6-16 µm. Genellikle tek çekirdeklidir ancak görülmesi zordur.

**2. Trofozoit Dönemi**
4-20 µm çapındadır. Hareketleri yavaştır. Boyalı incelemede ince bir çekirdek zarı ve büyük bir karyozom gözlemlenir.

**3. Klinik Önem**
Çoğunlukla apatojen kabul edilir. Dışkıda saptanması, hijyen standartlarının düşük olduğunu gösteren bir indikatördür."""
    },

    "Entamoeba gingivalis": {
        "BİLGİ": """İnsanda saptanan ilk amip olması nedeniyle tarihi öneme sahiptir. Ağız hijyeni zayıf bireylerde %95 prevalansa ulaşabilir.

**Yerleşim:** Diş ve diş eti boşlukları, bademcik kriptleri.
**Morfoloji:** Sadece trofozoit formu bulunur (kist formu yoktur). Hızlı hareket eder.
**İçerik:** Besin vakuolleri içinde bakteri, lökosit ve epitel hücresi bulunur.
**Patojenite:** Apatojen kabul edilir; diş çürümelerine zemin hazırlayabilir.
**Bulaş:** Öpüşme veya ortak mutfak eşyası kullanımı ile doğrudan bulaşır."""
    },
    "Naegleria fowleri": "BİLGİ: PAM (Primer Amibik Meningoensefalit) etkeni. Burun yoluyla MSS'ye girer.",
    "Acanthamoeba türleri": "BİLGİ: Keratit (lens kullanıcıları) ve GAE etkeni. Çift çeperli kist yapısı.",

    # --- KAMÇILILAR (FLAGELLATES) ---
    "Giardia intestinalis": "MORFOLOJİ: Vantuzlu trofozoit. | DÖNGÜ: Duodenum yerleşimi. | KLİNİK: Steatore. | TEDAVİ: Metronidazol.",
    "Chilomastix mesnili": "BİLGİ: Limon şeklinde kist yapısı tipiktir. Non-patojen bağırsak kamçılısı.",
    "Dientamoeba fragilis": "BİLGİ: Kisti yoktur. Trofozoit formu amip gibi görünse de kamçılıdır.",
    "Trichomonas hominis": "BİLGİ: Kalın bağırsak yerleşimli non-patojen kamçılı. Kisti yoktur.",
    "Enteromonas hominis": "BİLGİ: Küçük, non-patojen bağırsak kamçılısı.",
    "Retortamonas intestinalis": "BİLGİ: Nadir görülen, non-patojen bir bağırsak kamçılısıdır.",
    "Trichomonas tenax": "BİLGİ: Ağız boşluğu kommensali. Diş eti hastalıklarında görülür.",
    "Trichomonas vaginalis": "BİLGİ: Ürogenital patojen. STD etkeni. TANI: Akıntıda sıçrayıcı trofozoit.",

    # --- HEMOFLAGELLATLAR ---
    "Leishmania braziliensis kompleksi": "KLİNİK: Mukokutanöz Leishmaniasis (Espundia). Vektör: Phlebotomine.",
    "Leishmania donovani kompleksi": "KLİNİK: Viseral Leishmaniasis (Kala-azar). TANI: Kemik iliğinde LD cisimcikleri.",
    "Leishmania mexicana kompleksi": "KLİNİK: Yeni Dünya kutanöz leishmaniasis.",
    "Leishmania tropica kompleksi": "KLİNİK: Eski Dünya kutanöz leishmaniasis (Şark Çıbanı).",
    "Trypanosoma brucei gambiense": "KLİNİK: Batı Afrika Uyku Hastalığı. Vektör: Glossina.",
    "Trypanosoma brucei rhodesiense": "KLİNİK: Doğu Afrika Uyku Hastalığı. Daha akut seyir.",
    "Trypanosoma cruzi": "KLİNİK: Chagas Hastalığı. Vektör: Triatomine. C-şekilli tripomastigot.",
    "Trypanosoma rangeli": "BİLGİ: Güney Amerika'da yaygın, insan için non-patojen.",

    # --- SPOROZOONLAR ---
    "Plasmodium vivax": "KLİNİK: Tersiyana sıtması. Schüffner noktaları mevcuttur.",
    "Plasmodium ovale": "KLİNİK: Tersiyana benzeri sıtma. James noktaları görülür.",
    "Plasmodium malariae": "KLİNİK: Kuartana sıtması (72 saat). Bant formu trofozoit.",
    "Plasmodium falciparum": "KLİNİK: Malign sıtma. Muz şeklinde gametosit ve Maurer noktaları.",
    "Plasmodium knowlesi": "KLİNİK: Primat sıtması (24 saatlik döngü). Güneydoğu Asya.",
    "Babesia microti": "KLİNİK: Kene ile bulaş. Eritrosit içi 'Maltız Haçı' görünümü.",
    "Babesia divergens": "KLİNİK: Sığırlardan bulaşır, ağır seyreder.",

    # --- DİĞER PROTOZOONLAR ---
    "Balantidium coli": "KLİNİK: Patojen tek siliyat. Rezervuar: Domuz. Fasulye şeklinde makronükleus.",
    "Isospora belli": "BİLGİ: İnce bağırsak epiteli. TANI: Dışkıda eliptik ookistler.",
    "Sarcocystis türleri": "BİLGİ: İnsan hem ara konak hem son konak olabilir.",
    "Cryptosporidium parvum": "KLİNİK: HIV hastalarında ağır ishal. TANI: Modifiye Asit-Fast boyama.",
    "Blastocystis hominis": "BİLGİ: Vakuollü form en yaygın formdur.",
    "Cyclospora cayetanensis": "BİLGİ: Meyve/sebze ile bulaş. Asido-rezistan ookistler.",
    "Microsporidia": "BİLGİ: Hücre içi zorunlu parazit. Polar tüp içerir.",
    "Toxoplasma gondii": "BİLGİ: Son konak kedidir. Gebelerde teratojenik risk.",
    "Pneumocystis jirovecii": "KLİNİK: PCP (Pneumocystis pnömonisi). TANI: Gümüşleme boyama.",

    # --- NEMATODLAR ---
    "Enterobius vermicularis": "KLİNİK: Kıl kurdu. TANI: Selofan bant yöntemi (Yumurta asimetrik D harfi).",
    "Trichuris trichiura": "KLİNİK: Kamçı kurdu. TANI: Limon şeklinde, çift tıkaçlı yumurta.",
    "Ascaris lumbricoides": "KLİNİK: En büyük nematod. Akciğer göçü (Loeffler sendromu).",
    "Necator americanus": "KLİNİK: Yeni dünya kancalı kurdu. Kesici plaklar ile anemi yapar.",
    "Ancylostoma duodenale": "KLİNİK: Eski dünya kancalı kurdu. Dişli ağız yapısı.",
    "Strongyloides stercoralis": "KLİNİK: Larva akurens. Dışkıda rabditiform larva görülür.",
    "Trichinella spiralis": "KLİNİK: Kaslarda kist. Periorbital ödem ve kas ağrısı.",
    "Dracunculus medinensis": "KLİNİK: Medine solucanı. Ara konak: Cyclops.",

    # --- FİLARİALAR ---
    "Wuchereria bancrofti": "KLİNİK: Fil hastalığı. Gece periyodik mikrofilar. Vektör: Sivrisinek.",
    "Brugia malayi": "KLİNİK: Lenfatik filariyazis. Güneydoğu Asya.",
    "Loa loa": "KLİNİK: Göz solucanı. Calabar şişlikleri. Vektör: Chrysops.",
    "Onchocerca volvulus": "KLİNİK: Nehir körlüğü. Vektör: Simulium.",

    # --- SESTODLAR ---
    "Taenia saginata": "KLİNİK: Sığır şeridi. Skolekste çengel yok. Proglottidler hareketli.",
    "Taenia solium": "KLİNİK: Domuz şeridi. Sistiserkozis (beyin/göz yerleşimi).",
    "Hymenolepis nana": "KLİNİK: Cüce şerit. En sık görülen sestod.",
    "Hymenolepis diminuta": "KLİNİK: Fare şeridi. Ara konak (böcek) zorunludur.",
    "Diphyllobothrium latum": "KLİNİK: Balık şeridi. Vitamin B12 eksikliği anemisi.",
    "Echinococcus granulosus": "KLİNİK: Kist hidatik etkeni. Karaciğer ve akciğer tutulumu.",

    # --- TREMATODLAR ---
    "Fasciola hepatica": "KLİNİK: Karaciğer kelebeği. TANI: Operkulumlu büyük yumurta.",
    "Clonorchis sinensis": "KLİNİK: Çin karaciğer kelebeği. Safra yolları yerleşimi.",
    "Schistosoma mansoni": "KLİNİK: Kan fluku. Dışkıda lateral dikenli yumurta.",
    "Schistosoma haematobium": "KLİNİK: Üriner sistem. İdrarda terminal dikenli yumurta.",

    # --- ARTROPODLAR ---
    "Pediculus humanus capitis": "BİLGİ: Baş biti. Saçlı deri yerleşimi. Sirke tespiti.",
    "Pthirus pubis": "BİLGİ: Kasık biti. Mavi lekeler yapar.",
    "Lucilia sericata": "BİLGİ: Yeşil şişe sineği. MDT (Maggot Terapi) etkeni.",
    "Sarcoptes scabiei": "BİLGİ: Uyuz etkeni. Deride 'Sillon' tünelleri açar.",
    "Ixodes türleri": "BİLGİ: Sert kene. Lyme ve Babesiosis vektörü.",
    "Phlebotomus türleri": "BİLGİ: Tatarcık. Leishmaniasis vektörü.",
    "Glossina türleri": "BİLGİ: Çeçe sineği. Uyku hastalığı vektörü."
}

# --- ARAYÜZ ÜST KISIM ---
col1, col2 = st.columns([1, 5])
with col1:
    st.markdown("# 🔬")
with col2:
    st.markdown("<h2 style='margin-bottom:0;'>KAEÜ Tıp Fakültesi</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:gray;'>Tıbbi Parazitoloji Anabilim Dalı Akademik Rehberi</p>", unsafe_allow_html=True)

# --- ANA SEKMELER ---
ana_sekme1, ana_sekme2, ana_sekme3 = st.tabs(["🔍 Hızlı Sorgu", "🗂️ Tıbbi Önemi Olan Parazitler", "🌳 Parazitoloji Ağacı"])

# --- SEKME 1: SORGULAMA ---
with ana_sekme1:
    sorgu = st.text_input("Parazit veya Terim Adı Giriniz:", placeholder="Örn: Toxoplasma gondii")
    if sorgu:
        results = {k: v for k, v in parazit_verisi.items() if sorgu.lower() in k.lower()}
        
        if results:
            for isim, veri in results.items():
                # Kitap Başlığı gibi büyük isim
                st.markdown(f"## {isim}") 
                st.divider() # Araya ince bir çizgi çeker
                
                if isinstance(veri, dict):
                    # Kitap Düzeni: Yazı ve Resmi yan yana veya alt alta şık yerleştirme
                    col_metin, col_resim = st.columns([2, 1]) # Yazıya 2 birim, resme 1 birim yer ayır
                    
                    with col_metin:
                        st.markdown("### Genel Bilgiler")
                        st.write(veri["bilgi"])
                    
                    with col_resim:
                        # DOSYA YOLU KONTROLÜ
                        # Resim dosyasının adını ve yolunu tam kontrol et
                        resim_yolu = veri["resim"]
                        
                        if os.path.exists(resim_yolu):
                            st.image(resim_yolu, caption=f"{isim} Morfolojisi", use_container_width=True)
                        else:
                            # Resim yoksa neden olmadığını anlamak için hata mesajı gösterelim
                            st.error(f"⚠️ Resim Bulunamadı!\n\nAranan Yol: {resim_yolu}")
                            st.info("İpucu: Klasör isminin ve dosya uzantısının (.png / .jpg) birebir aynı olduğundan emin olun.")
                else:
                    st.write(veri)
        else:
            st.error("Kayıt bulunamadı.")

# --- SEKME 2: SINIFLANDIRMA (HIYERARŞİK) ---
with ana_sekme2:
    st.markdown("### 📚 Sistematik Sınıflandırma")
    
    p_kat, h_kat, a_kat = st.columns(3)

    # Yardımcı Fonksiyon: Veri tipine göre içeriği basar
    def parazit_yazdir(isim):
        veri = parazit_verisi.get(isim)
        if veri:
            with st.expander(isim):
                if isinstance(veri, dict):
                    # "bilgi" veya "BİLGİ" anahtarını kontrol et (küçük/büyük harf duyarlılığı için)
                    icerik = veri.get("bilgi") or veri.get("BİLGİ") or "Detaylı bilgi bulunamadı."
                    st.write(icerik)
                else:
                    st.write(veri)

    # 1. KOLON: PROTOZOONLAR (Görseldeki Hiyerarşiye Göre)
    with p_kat:
        st.markdown("<h4 style='color:#8b0000;'>🧫 PROTOZOONLAR</h4>", unsafe_allow_html=True)
        
        # --- 1- SARCOMASTIGOPHORA ---
        with st.expander("1- SARCOMASTIGOPHORA"):
            
            # A- SARCODINA
            st.markdown("<p style='font-weight:bold; color:#8b0000; margin-bottom:5px;'>A- SARCODINA</p>", unsafe_allow_html=True)
            with st.expander("Amipler"):
                amipler = ["Entamoeba histolytica", "Entamoeba dispari", "Entamoeba polecki", "Entamoeba coli", 
                           "Endolimax nana", "Iodamoeba bütschlii", "Entamoeba hartmanni", "Entamoeba gingivalis"]
                for p in amipler: parazit_yazdir(p)
            
            with st.expander("Serbest Yaşayan Amipler"):
                serbest = ["Naegleria fowleri", "Acanthamoeba türleri"] # Balamuthia ve Sappinia veride varsa eklenir
                for p in serbest: parazit_yazdir(p)
                st.caption("Not: Balamuthia türleri ve Sappinia pedata")

            st.divider()

            # B- MASTIGOPHORA
            st.markdown("<p style='font-weight:bold; color:#8b0000; margin-bottom:5px;'>B- MASTIGOPHORA (Kamçılılar)</p>", unsafe_allow_html=True)
            with st.expander("Sindirim Sistemi Kamçılıları"):
                sindirim = ["Giardia intestinalis", "Trichomonas tenax", "Trichomonas hominis", "Chilomastix mesnili", 
                            "Dientamoeba fragilis", "Retortamonas intestinalis", "Enteromonas hominis"]
                for p in sindirim: parazit_yazdir(p)
            
            with st.expander("Ürogenital Sistem Kamçılıları"):
                parazit_yazdir("Trichomonas vaginalis")
            
            with st.expander("Kan ve Doku Kamçılıları"):
                kandoku = ["Leishmania tropica kompleksi", "Leishmania donovani kompleksi", "Trypanosoma cruzi", "Trypanosoma brucei gambiense"]
                for p in kandoku: parazit_yazdir(p)

        # --- 2- APICOMPLEXA ---
        with st.expander("2- APICOMPLEXA"):
            sporo = ["Plasmodium vivax", "Plasmodium falciparum", "Babesia microti", "Toxoplasma gondii", 
                     "Isospora belli", "Cryptosporidium parvum", "Cyclospora cayetanensis", "Sarcocystis türleri"]
            for p in sporo: parazit_yazdir(p)
            st.caption("Cystoisospora türleri = Isospora belli")

        # --- 3- CILIOPHORA ---
        with st.expander("3- CILIOPHORA"):
            parazit_yazdir("Balantidium coli")
            
        # --- DİĞER ---
        with st.expander("DİĞER"):
            diger = ["Blastocystis hominis", "Microsporidia", "Pneumocystis jirovecii"]
            for p in diger: parazit_yazdir(p)

  # 2. KOLON: HELMİNTLER
    with h_kat:
        st.markdown("<h4 style='color:#8b0000;'>🐛 HELMİNTLER</h4>", unsafe_allow_html=True)
        
        # --- 1- NEMATODLAR ---
        with st.expander("1- NEMATODLAR (Yuvarlak Solucanlar)"):
            with st.expander("🔹 Bağırsak Nematodları"):
                b_nematod = [
                    "Ascaris lumbricoides", "Çengelli solucanlar", "Strongyloides stercoralis", 
                    "Trichostrongylus türleri", "Enterobius vermicularis", "Trichuris trichiura", 
                    "Capillaria philippinensis", "Gongylonema pulchrum", "Strongyloides fuelloborni", 
                    "Trichinella türleri"
                ]
                for p in b_nematod: parazit_yazdir(p)

            with st.expander("🔹 Dolaşım ve Doku Nematodları"):
                d_nematod = [
                    "Wuchereria bancrofti", "Brugia türleri", "Loa loa", "Mansonella türleri", 
                    "Onchocerca volvulus", "Dirofilaria repens", "Dirofilaria immitis", 
                    "Dracunculus medinensis", "Capillaria hepatica"
                ]
                for p in d_nematod: parazit_yazdir(p)

            with st.expander("🔹 Larva Migrans Etkenleri"):
                st.write("**Deri Larva Migrans:** Ancylostoma braziliense, A.caninum, Bunostomum, Strongyloides türleri")
                st.write("**İç Organlar Larva Migrans:** Toxocara canis, T.cati, Angiostrongylus, Gnathostoma, Anisakis")

        # --- 2- TREMATODLAR ---
        with st.expander("2- TREMATODLAR (Yassı Solucanlar)"):
            with st.expander("🔹 Karaciğer Trematodları"):
                t_karaciger = [
                    "Fasciola hepatica", "Fasciola gigantica", "Dicrocoelium dendriticum", 
                    "Clonorchis sinensis", "Opisthorchis felineus", "Opisthorchis viverrini"
                ]
                for p in t_karaciger: parazit_yazdir(p)

            with st.expander("🔹 Bağırsak Trematodları"):
                t_bagirsak = [
                    "Fasciolopsis buski", "Heterophyes heterophyes", "Metagonimus yokogawai", 
                    "Echinostoma türleri", "Gastrodiscoides hominis", "Watsonius watsoni"
                ]
                for p in t_bagirsak: parazit_yazdir(p)

            with st.expander("🔹 Akciğer Trematodları"):
                parazit_yazdir("Paragonimus westermani")

            with st.expander("🔹 Kan Trematodları"):
                t_kan = [
                    "Schistosoma haematobium", "Schistosoma mansoni", "Schistosoma japonicum", 
                    "Schistosoma intercalatum", "Schistosoma mekongi"
                ]
                for p in t_kan: parazit_yazdir(p)

        # --- 3- SESTODLAR ---
        with st.expander("3- SESTODLAR (Şeritler)"):
            with st.expander("🔹 Cyclophyllidea"):
                s_cyclo = ["Taenia saginata", "Taenia solium", "Hymenolepis nana", "Hymenolepis diminuta", "Dipylidium caninum", "Echinococcus türleri"]
                for p in s_cyclo: parazit_yazdir(p)
            
            with st.expander("🔹 Pseudophyllidea"):
                parazit_yazdir("Diphyllobothrium latum")

   # 3. KOLON: ARTROPODLAR (Genişletilmiş Akademik Liste)
    with a_kat:
        st.markdown("<h4 style='color:#8b0000;'>🕷️ ARTROPODLAR</h4>", unsafe_allow_html=True)

        # --- 1. SINIF: INSECTA (Böcekler) ---
        with st.expander("1- INSECTA (Böcekler)"):
            
            # Diptera
            st.markdown("<p style='font-weight:bold; color:#8b0000; margin-bottom:5px;'>Takım: Diptera (İki Kanatlılar)</p>", unsafe_allow_html=True)
            with st.expander("Sivrisinekler (Culicidae)"):
                culicidae = ["Anopheles gambiae", "Anopheles sacharovi", "Culex pipiens", "Aedes aegypti", "Aedes albopictus"]
                for p in culicidae: parazit_yazdir(p)
            
            with st.expander("Tatarcıklar (Psychodidae)"):
                tatarcik = ["Phlebotomus papatasi", "Phlebotomus sergenti"]
                for p in tatarcik: parazit_yazdir(p)

            with st.expander("Isıran Sinekler"):
                isiran = ["Glossina palpalis", "Simulium damnosum", "Chrysops silacea"]
                for p in isiran: parazit_yazdir(p)

            with st.expander("Mekanik Taşıyıcı / Miyaz"):
                miyaz = ["Musca domestica", "Dermatobia hominis", "Lucilia sericata"]
                for p in miyaz: parazit_yazdir(p)

            st.divider()

            # Phthiraptera
            st.markdown("<p style='font-weight:bold; color:#8b0000; margin-bottom:5px;'>Takım: Phthiraptera (Bitler)</p>", unsafe_allow_html=True)
            bitler = ["Pediculus humanus corporis", "Pediculus humanus capitis", "Pthirus pubis"]
            for p in bitler: parazit_yazdir(p)

            # Siphonaptera
            st.markdown("<p style='font-weight:bold; color:#8b0000; margin-top:10px; margin-bottom:5px;'>Takım: Siphonaptera (Pireler)</p>", unsafe_allow_html=True)
            pireler = ["Xenopsylla cheopis", "Pulex irritans", "Tunga penetrans"]
            for p in pireler: parazit_yazdir(p)

            # Hemiptera
            st.markdown("<p style='font-weight:bold; color:#8b0000; margin-top:10px; margin-bottom:5px;'>Takım: Hemiptera (Tahtakuruları)</p>", unsafe_allow_html=True)
            hemiptera = ["Triatoma infestans", "Rhodnius prolixus", "Cimex lectularius"]
            for p in hemiptera: parazit_yazdir(p)

        # --- 2. SINIF: ARACHNIDA (Örümcekgiller) ---
        with st.expander("2- ARACHNIDA (Örümcekgiller)"):
            
            with st.expander("Sert Keneler (Ixodidae)"):
                sert_kene = ["Ixodes ricinus", "Hyalomma marginatum", "Dermacentor variabilis"]
                for p in sert_kene: parazit_yazdir(p)

            with st.expander("Yumuşak Keneler (Argasidae)"):
                parazit_yazdir("Ornithodoros moubata")

            with st.expander("Akarlar (Acarina)"):
                akarlar = ["Sarcoptes scabiei", "Demodex folliculorum", "Dermatophagoides pteronyssinus"]
                for p in akarlar: parazit_yazdir(p)

            with st.expander("Akrepler (Scorpiones)"):
                akrepler = ["Androctonus crassicauda", "Leiurus quinquestriatus", "Mesobuthus gibbosus"]
                for p in akrepler: parazit_yazdir(p)

            with st.expander("Örümcekler (Araneae)"):
                orumcek = ["Latrodectus mactans", "Loxosceles reclusa"]
                for p in orumcek: parazit_yazdir(p)

        # --- 3. SINIF: CHILOPODA (Çok Ayaklılar) ---
        with st.expander("3- CHILOPODA (Çıyanlar)"):
            parazit_yazdir("Scolopendra gigantea")

        # --- 4. SINIF: CRUSTACEA (Kabuklular) ---
        with st.expander("4- CRUSTACEA (Ara Konaklar)"):
            st.info("Bu sınıftakiler genellikle paraziter hastalıkların ara konaklarıdır.")
            kabuklular = ["Cyclops strenuus", "Eriocheir sinensis"]
            for p in kabuklular: parazit_yazdir(p)

# --- FOOTER ---
st.markdown("---")
st.markdown("Bu bir <span style='color:red'>kırmızı kelime</span> ve bu bir <span style='color:blue'>mavi kelime</span> örneğidir.", unsafe_allow_html=True)
st.caption("© 2026 Kırşehir Ahi Evran Üniversitesi Tıp Fakültesi - Tıbbi Parazitoloji Anabilim Dalı")
