import streamlit as st
import os

# --- SAYFA AYARLARI ---
st.set_page_config(
    page_title="Parazitoloji Veri Bankası", 
    page_icon="🔬",
    layout="centered"
)

# --- STİL (CSS) ---
st.markdown("""
    <style>
    .main { background-color: #f5f5f5; }
    .stTextInput > div > div > input {
        border: 2px solid #8b0000;
        border-radius: 10px;
    }
    .result-card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #8b0000;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        color: #333;
    }
    </style>
    """, unsafe_allow_html=True)

# --- VERİ SETLERİ ---
parazit_verisi = {
    # --- AMİPLER (AMEBAE) ---
    "Entamoeba histolytica": "MORFOLOJİ: Trofozoit (merkezi endozom), Kist (1-4 çekirdek). | DÖNGÜ: Kist alımı -> Kalın bağırsak yerleşimi. | TANI: Dışkıda hematofaj trofozoit. | TEDAVİ: Metronidazol.",
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
    "Pneumocystis jiroveci": "KLİNİK: PCP (Pneumocystis pnömonisi). TANI: Gümüşleme boyama.",

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

# --- ARAYÜZ ---
col1, col2 = st.columns([1, 3])
with col1:
    if os.path.exists("logo.png"):
        st.image("logo.png", width=80)
with col2:
    st.markdown("<h3 style='margin-bottom:0;'>KAEÜ Tıp Fakültesi</h3>", unsafe_allow_html=True)
    st.markdown("<p style='color:gray;'>Tıbbi Parazitoloji AD</p>", unsafe_allow_html=True)

st.markdown("---")
st.markdown("#### 🔬 Parazit/Terim Sorgula")

sorgu = st.text_input("", placeholder="Örn: Entamoeba histolytica")

if st.button("BİLGİLERİ GETİR") or (sorgu != ""):
    if sorgu:
        found = False
        # Harfi harfine ancak büyük/küçük harf duyarsız kontrol
        for key, value in parazit_verisi.items():
            if key.lower() == sorgu.strip().lower():
                kategori = 'Tıbbi Parazit' if key in parazit_verisi else 'Akademik Terim'
                st.markdown(f"""
                <div class='result-card'>
                    <h3 style='color:#8b0000;'>{key.upper()}</h3>
                    <p><b>Kategori:</b> {kategori}</p>
                    <hr>
                    {value.replace(' | ', '<br><br>')}
                </div>
                """, unsafe_allow_html=True)
                found = True
                break
        
        if not found:
            st.error("❌ Kayıt bulunamadı. Lütfen yazımı kontrol edin.")
    elif st.button("BİLGİLERİ GETİR"): # Boş sorgu butonu basılırsa
        st.warning("Lütfen bir isim yazın.")

st.markdown("<br><br>", unsafe_allow_html=True)
st.caption("© 2026 Tıbbi Parazitoloji Akademik Rehberi")