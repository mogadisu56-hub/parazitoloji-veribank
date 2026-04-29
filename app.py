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
    # --- AMİPLER (AMEBAE) ---
    "Entamoeba histolytica": {
        "bilgi": """Entamoeba histolytica ve Amoebiosis Entamoeba histolytica, dünya genelinde (özellikle tropikal bölgelerde) yaygın görülen, patojenik ve tek hücreli bir anaerop protozoondur. 
        İnsanlarda asemptomatik taşıyıcılıktan ölümcül dizanteriye ve karaciğer apselerine kadar geniş bir klinik yelpazeye neden olur. 
        1. Morfoloji ve Hayat Döngüsü Parazitin hayat döngüsü; trofozoit, prekist, kist, metakist ve metakistik trofozoit evrelerinden oluşur. 
        Trofozoit: Aktif hareket eden, beslenen ve çoğalan formdur. Lobopod adı verilen yalancı ayaklarla hareket eder. Sitoplazmasında fagosite edilmiş alyuvarlar (eritrosit) bulunabilir; bu özellik teşhiste önemlidir.
        Kist: Parazitin dış ortama ve mide asidine dirençli, enfektif formudur. Olgun kist 4 çekirdeklidir. İçerisinde uçları yuvarlak kromatoid cisimcikler bulunur (bu özellik E. coli'den ayrımını sağlar).
        Döngü: Ağız yoluyla alınan 4 çekirdekli olgun kistler, ince bağırsakta kist duvarının parçalanmasıyla metakistik trofozoitlere dönüşür. 
        Bunlar kalın bağırsağa (özellikle çekum ve rekto-sigmoidal bölgeye) yerleşerek kolonize olurlar. 2. Patogenez ve Klinik Belirtiler Parazit, yüzeyindeki Gal/GalNAc lektin aracılığıyla bağırsak epiteline yapışır. 
        Proteolitik enzimler salgılayarak dokuyu istila eder. Bağırsak Amoebiosisi: Amibik Dizanteri: Kanlı-mukuslu dışkılama, karın ağrısı ve tenesmus ile karakterizedir.
        Şişe Biçimli Ülserler: Parazit submukozaya yayılarak tipik kraterimsi, dar ağızlı ülserler oluşturur. 
        Ameboma: Kronik vakalarda bağırsak duvarında tümörle karışabilen inflamatuar kitleler oluşabilir. 
        Bağırsak Dışı (Ekstraintestinal) Amoebiosis: Parazitin portal dolaşımla diğer organlara yayılmasıdır. En sık karaciğerde (genellikle sağ lopta tek apse) görülür. Apse materyali tipik olarak "ançuez sosu" görünümündedir. 
        Bunu akciğer, beyin ve deri tutulumları izleyebilir. 3. Epidemiyoloji ve Bulaşma Bulaşma yolu fekal-oral (dışkı-ağız) yoldur. Kaynak, dışkısıyla kist atan asemptomatik taşıyıcılardır. 
        Kontamine su ve gıdaların tüketilmesi, İnsan dışkısının gübre olarak kullanılması, Karasinek ve hamamböceği gibi vektörler, Kişisel hijyen eksikliği bulaşmada ana rol oynar. 
        4. Tanı Yöntemleri Kesin tanı laboratuvar incelemelerine dayanır. Örneklerin (dışkı, apse materyali, biyopsi) taze incelenmesi kritiktir. 
        Mikroskopi: Dışkıda trofozoit (taze/sulu dışkıda) veya kist (şekilli dışkıda) aranır. Lugol veya kalıcı boyalar (Trikrom, Hematoksilen) kullanılır. Seroloji: Bağırsak dışı amoebiosis vakalarının %95'inde antikor testleri (ELISA, IHA) pozitiftir.
        Antijen ve Moleküler Testler: Dışkıda antijen arayan ELISA kitleri ve PCR yöntemleri, E. histolytica ile patojen olmayan E. dispar ayrımı için altın standarttır. 
        Görüntüleme: Karaciğer apsesi şüphesinde USG, BT ve MR kullanılır. 5. Tedavi ve Kontrol Tedavi, hastalığın şiddetine ve yerleşimine göre planlanır: 
        İlaç Tedavisi: İnvaziv Enfeksiyonlar: Metronidazol (en yaygın), tinidazol veya ornidazol. Luminal (Taşıyıcılık) Tedavisi: Paromomisin, iyodokinol veya diloksanid furoat. Gebelikte: Paromomisin güvenli bir seçenektir. 
        Cerrahi: Perforasyon, şiddetli kanama veya ilaç tedavisine yanıt vermeyen büyük karaciğer apselerinde (özellikle sol lop yerleşimli rüptür riski olanlar) drenaj veya cerrahi müdahale gerekebilir. 
        Korunma: Temiz içme suyu sağlanması, kanalizasyon altyapısının iyileştirilmesi, gıda sektöründe çalışanların periyodik kontrolü ve el yıkama alışkanlığının yaygınlaştırılması temel korunma yollarıdır.""",
        "resim": "parazit_program/Entamoeba_histolytica.png"},
    "Entamoeba hartmanni": "BİLGİ: Non-patojen amip. E. histolytica'ya benzer ancak daha küçüktür (<10µm).",
    "Entamoeba coli": "MORFOLOJİ: Kist 8 çekirdekli, eksantrik endozom. BİLGİ: Non-patojen bağırsak kommensali.",
    "Entamoeba polecki": "BİLGİ: Domuz/maymun amibi. TANI: Tek çekirdekli kist yapısı karakteristiktir.",
    "Endolimax nana": "BİLGİ: En küçük bağırsak amibi. Kisti 4 çekirdekli ve ovaldir. Non-patojen.",
    "Iodamoeba bütschlii": "BİLGİ: Kistinde iyot ile boyanan çok büyük bir glikojen vakuolü bulunur. Non-patojen.",
    "Entamoeba gingivalis": "BİLGİ: Sadece trofozoit formu vardır. Diş eti ve ağız hijyeni ile ilişkilidir.",
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

    with p_kat:
        with st.expander("🧫 PROTOZOONLAR"):
            with st.expander("Sarcomastigophora"):
                with st.expander("Sarcodina (Amipler)"):
                    with st.expander("Entamoeba histolytica"):
                        st.write("- Dünya genelinde (özellikle tropikal bölgelerde) yaygın görülen, patojenik ve tek hücreli bir anaerop protozoondur. İnsanlarda asemptomatik taşıyıcılıktan ölümcül dizanteriye ve karaciğer apselerine kadar geniş bir klinik yelpazeye neden olur. 1. Morfoloji ve Hayat Döngüsü Parazitin hayat döngüsü; trofozoit, prekist, kist, metakist ve metakistik trofozoit evrelerinden oluşur. Trofozoit: Aktif hareket eden, beslenen ve çoğalan formdur. Lobopod adı verilen yalancı ayaklarla hareket eder. Sitoplazmasında fagosite edilmiş alyuvarlar (eritrosit) bulunabilir; bu özellik teşhiste önemlidir. Kist: Parazitin dış ortama ve mide asidine dirençli, enfektif formudur. Olgun kist 4 çekirdeklidir. İçerisinde uçları yuvarlak kromatoid cisimcikler bulunur (bu özellik E. coli'den ayrımını sağlar). Döngü: Ağız yoluyla alınan 4 çekirdekli olgun kistler, ince bağırsakta kist duvarının parçalanmasıyla metakistik trofozoitlere dönüşür. Bunlar kalın bağırsağa (özellikle çekum ve rekto-sigmoidal bölgeye) yerleşerek kolonize olurlar. 2. Patogenez ve Klinik Belirtiler Parazit, yüzeyindeki Gal/GalNAc lektin aracılığıyla bağırsak epiteline yapışır. Proteolitik enzimler salgılayarak dokuyu istila eder. Bağırsak Amoebiosisi: Amibik Dizanteri: Kanlı-mukuslu dışkılama, karın ağrısı ve tenesmus ile karakterizedir. Şişe Biçimli Ülserler: Parazit submukozaya yayılarak tipik kraterimsi, dar ağızlı ülserler oluşturur. Ameboma: Kronik vakalarda bağırsak duvarında tümörle karışabilen inflamatuar kitleler oluşabilir. Bağırsak Dışı (Ekstraintestinal) Amoebiosis: Parazitin portal dolaşımla diğer organlara yayılmasıdır. En sık karaciğerde (genellikle sağ lopta tek apse) görülür. Apse materyali tipik olarak "ançuez sosu" görünümündedir. Bunu akciğer, beyin ve deri tutulumları izleyebilir. 3. Epidemiyoloji ve Bulaşma Bulaşma yolu fekal-oral (dışkı-ağız) yoldur. Kaynak, dışkısıyla kist atan asemptomatik taşıyıcılardır. Kontamine su ve gıdaların tüketilmesi, İnsan dışkısının gübre olarak kullanılması, Karasinek ve hamamböceği gibi vektörler, Kişisel hijyen eksikliği bulaşmada ana rol oynar. 4. Tanı Yöntemleri Kesin tanı laboratuvar incelemelerine dayanır. Örneklerin (dışkı, apse materyali, biyopsi) taze incelenmesi kritiktir. Mikroskopi: Dışkıda trofozoit (taze/sulu dışkıda) veya kist (şekilli dışkıda) aranır. Lugol veya kalıcı boyalar (Trikrom, Hematoksilen) kullanılır. Seroloji: Bağırsak dışı amoebiosis vakalarının %95'inde antikor testleri (ELISA, IHA) pozitiftir. Antijen ve Moleküler Testler: Dışkıda antijen arayan ELISA kitleri ve PCR yöntemleri, E. histolytica ile patojen olmayan E. dispar ayrımı için altın standarttır. Görüntüleme: Karaciğer apsesi şüphesinde USG, BT ve MR kullanılır. 5. Tedavi ve Kontrol Tedavi, hastalığın şiddetine ve yerleşimine göre planlanır: İlaç Tedavisi: İnvaziv Enfeksiyonlar: Metronidazol (en yaygın), tinidazol veya ornidazol. Luminal (Taşıyıcılık) Tedavisi: Paromomisin, iyodokinol veya diloksanid furoat. Gebelikte: Paromomisin güvenli bir seçenektir. Cerrahi: Perforasyon, şiddetli kanama veya ilaç tedavisine yanıt vermeyen büyük karaciğer apselerinde (özellikle sol lop yerleşimli rüptür riski olanlar) drenaj veya cerrahi müdahale gerekebilir. Korunma: Temiz içme suyu sağlanması, kanalizasyon altyapısının iyileştirilmesi, gıda sektöründe çalışanların periyodik kontrolü ve el yıkama alışkanlığının yaygınlaştırılması temel korunma yollarıdır ")
                    with st.expander("Entamoeba hartmanni"):
                        st.write("- abc")
                    with st.expander("Entamoeba coli"):
                        st.write("- abc")
                    with st.expander("Entamoeba polecki"):
                        st.write("- abc")
                    with st.expander("Entamoeba histolytica"):
                        st.write("- Balantidium coli")
                with st.expander("Serbest Yaşayanlar Amipler)"):
                    st.write("- Entamoeba histolytica / dispar\n- Entamoeba hartmanni\n- Entamoeba coli\n-Entamoeba polecki\n-Endolimax nana\n-Iodamoeba bütschlii\n-Entamoeba gingivalis")
                    st.write("- Naegleria fowleri\n- Acanthamoeba türleri\n-  Balamuthia\n- Sappinia pedata")
                with st.expander("Mastigophora (Kamçılılar)"):
                    st.markdown("**Sindirim:** Giardia, Chilomastix, Dientamoeba, Trichomonas hominis")
                    st.markdown("**Ürogenital:** Trichomonalis")
                    st.markdown("**Kan-Doku:** Leishmania türleri, Trypanosoma türleri")
            
            with st.expander("Apicomplexa (Sporozoonlar)"):
                st.write("- Plasmodium türleri\n- Babesia türleri\n- Toxoplasma gondii\n- Cryptosporidium, Cyclospora, Cystoisospora")
            
            with st.expander("Ciliophora"):
                st.write("- Balantidium coli")
            
            with st.expander("Diğer"):
                st.write("- Blastocystis hominis\n- Microsporidia\n- Pneumocystis jiroveci")

    with h_kat:
        with st.expander("🐛 HELMİNTLER"):
            with st.expander("Nematodlar (Yuvarlak)"):
                st.write("- Ascaris, Enterobius, Trichuris\n- Kancalı Kurtlar (Necator, Ancylostoma)\n- Strongyloides, Trichinella")
                st.caption("Filarialar: Wuchereria, Brugia, Loa loa, Onchocerca")
            with st.expander("Sestodlar (Şeritler)"):
                st.write("- Taenia saginata / solium\n- Hymenolepis nana / diminuta\n- Diphyllobothrium latum\n- Echinococcus granulosus")
            with st.expander("Trematodlar (Yassı)"):
                st.write("- Fasciola hepatica\n- Schistosoma türleri\n- Clonorchis sinensis\n- Paragonimus westermani")

    with a_kat:
        with st.expander("🕷️ ARTROPODLAR"):
            with st.expander("Insecta (Böcekler)"):
                st.write("- Bitler (Pediculus, Pthirus)\n- Pireler ve Tahtakuruları\n- Sinekler (Anopheles, Phlebotomus, Glossina)")
            with st.expander("Arachnida (Araknidler)"):
                st.write("- Sarcoptes scabiei (Uyuz)\n- Keneler (Ixodes, Rhipicephalus)\n- Demodex türleri")
            with st.expander("Crustacea"):
                st.write("- Cyclops türleri")

# --- SEKME 3: PARAZİTOLOJİ AĞACI ---
with ana_sekme3:
    st.markdown("### 🌳 Parazitoloji Akademik Soy Ağacı")
    st.info("Aşağıdaki liste, tüm tıbbi parazitoloji müfredatının dallanmış yapısını gösterir.")
    
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.markdown("<div class='category-header'>1. PROTOZOA</div>", unsafe_allow_html=True)
        st.markdown("""
        * **Sarcomastigophora**
            * *Sarcodina:* E. histolytica, E. coli, Naegleria fowleri...
            * *Mastigophora:* Giardia, Leishmania, Trypanosoma, T. vaginalis...
        * **Apicomplexa**
            * Plasmodium (Sıtma), Babesia, Toxoplasma, Cryptosporidium...
        * **Ciliophora**
            * Balantidium coli
        * **Diğer**
            * Blastocystis, Pneumocystis...
        """, unsafe_allow_html=True)

        st.markdown("<br><div class='category-header'>2. HELMİNTLER</div>", unsafe_allow_html=True)
        st.markdown("""
        * **Nematoda**
            * Bağırsak: Ascaris, Enterobius, Trichuris...
            * Doku/Kan: Wuchereria, Loa loa, Dracunculus...
        * **Platyhelminthes**
            * *Sestodlar:* Taenia, Echinococcus, H. nana...
            * *Trematodlar:* Fasciola, Schistosoma...
        """, unsafe_allow_html=True)

    with col_b:
        st.markdown("<div class='category-header'>3. ARTROPODLAR</div>", unsafe_allow_html=True)
        st.markdown("""
        * **Insecta**
            * Anopheles, Culex, Phlebotomus (Vektörler)
            * Pediculus (Bit), Cimex (Tahtakurusu)
        * **Arachnida**
            * Ixodes (Kene), Sarcoptes (Uyuz)
        * **Crustacea**
            * Cyclops
        """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("---")
st.caption("© 2026 Kırşehir Ahi Evran Üniversitesi Tıp Fakültesi - Tıbbi Parazitoloji Anabilim Dalı")
