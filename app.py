import streamlit as st
import json
import os

# -------------------------------
# 📌 PARAZİT KARTI (POPUP)
# -------------------------------
@st.dialog("📌 Parazit Bilgi Kartı")
def parazit_kart(isim, veri):
    if isinstance(veri, dict):
        icerik = veri.get("bilgi") or veri.get("BİLGİ") or "Bilgi yok"
    else:
        icerik = veri

    st.markdown(f"### 🧬 {isim}")
    st.write(icerik)


# -------------------------------
# 📌 BUTONLA AÇMA
# -------------------------------
def parazit_yazdir(isim):
    veri = parazit_verisi.get(isim)

    if veri:
        if st.button(isim, key=f"btn_{isim}"):
            parazit_kart(isim, veri)


# -------------------------------
# 📌 VERİ YÜKLE / KAYDET
# -------------------------------
def veri_yukle():
    with open("parazitler.json", "r", encoding="utf-8") as f:
        return json.load(f)

def veri_kaydet(data):
    with open("parazitler.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


# -------------------------------
# 📌 SESSION STATE
# -------------------------------
if "veri" not in st.session_state:
    st.session_state.veri = veri_yukle()

if "kayit_mesaj" not in st.session_state:
    st.session_state.kayit_mesaj = False

parazit_verisi = st.session_state.veri


# -------------------------------
# 📌 SAYFA AYAR
# -------------------------------
st.set_page_config(
    page_title="KAEÜ Parazitoloji Veri Bankası",
    page_icon="🔬",
    layout="wide"
)

# -------------------------------
# 🎨 STİL
# -------------------------------
st.markdown("""
<style>
.main { background-color: #f8f9fa; }
.stExpander { border: 1px solid #8b0000; border-radius: 10px; margin-bottom: 5px; }
</style>
""", unsafe_allow_html=True)


# -------------------------------
# 📌 ÜST BAŞLIK
# -------------------------------
col1, col2 = st.columns([1, 5])
with col1:
    st.markdown("# 🔬")
with col2:
    st.markdown("## KAEÜ Tıp Fakültesi")
    st.markdown("Tıbbi Parazitoloji AD")


# -------------------------------
# 📌 SEKMELER
# -------------------------------
sekme1, sekme2, sekme3, sekme4, sekme5 = st.tabs([
    "🔍 Hızlı Sorgu",
    "🗂️ Tıbbi Önemi Olan Parazitler",
    "🌳 Parazitoloji Ağacı",
    "📘 Temel Parazitoloji",
    "⚙️ Veri Düzenle"
])


# -------------------------------
# 🔍 SEKME 1
# -------------------------------
with sekme1:
    sorgu = st.text_input("Parazit ara")

    if sorgu:
        for isim, veri in parazit_verisi.items():
            if sorgu.lower() in isim.lower():
                st.markdown(f"### {isim}")

                if st.button(f"Bilgi Aç", key=f"sorgu_{isim}"):
                    parazit_kart(isim, veri)


# -------------------------------
# 🗂️ SEKME 2
# -------------------------------
with sekme2:
    st.markdown("### 📚 Sistematik Sınıflandırma")

    col1, col2, col3 = st.columns(3)

    # PROTOZOONLAR
    with col1:
        st.markdown("#### 🧫 Protozoonlar")

        with st.expander("Amipler"):
            amipler = [
                "Entamoeba histolytica",
                "Entamoeba coli",
                "Entamoeba dispar",
                "Endolimax nana",
                "Iodamoeba bütschlii"
            ]
            for p in amipler:
                parazit_yazdir(p)

        with st.expander("Kamçılılar"):
            for p in ["Giardia intestinalis", "Trichomonas vaginalis"]:
                parazit_yazdir(p)

    # HELMİNTLER
    with col2:
        st.markdown("#### 🐛 Helmintler")

        with st.expander("Nematodlar"):
            for p in ["Ascaris lumbricoides", "Enterobius vermicularis"]:
                parazit_yazdir(p)

        with st.expander("Sestodlar"):
            for p in ["Taenia saginata", "Echinococcus granulosus"]:
                parazit_yazdir(p)

    # ARTROPODLAR
    with col3:
        st.markdown("#### 🕷️ Artropodlar")

        with st.expander("Örnekler"):
            for p in ["Sarcoptes scabiei", "Pediculus humanus capitis"]:
                parazit_yazdir(p)


# -------------------------------
# 🌳 SEKME 3
# -------------------------------
with sekme3:
    st.markdown("### 🌳 Parazitoloji Ağacı")

    agac = {
        "Protozoonlar": ["Entamoeba histolytica", "Giardia intestinalis"],
        "Helmintler": ["Ascaris lumbricoides"],
    }

    for kat, liste in agac.items():
        with st.expander(kat):
            for p in liste:
                parazit_yazdir(p)


# -------------------------------
# 📘 SEKME 4
# -------------------------------
with sekme4:
    st.markdown("## 📘 Temel Parazitoloji")

    with st.expander("Parazit Nedir"):
        st.write("Parazit, başka canlıya bağımlı yaşayan organizmadır.")

    with st.expander("Bulaş Yolları"):
        st.write("Fekal-oral, vektör, temas")


# -------------------------------
# ⚙️ SEKME 5
# -------------------------------
with sekme5:
    st.markdown("## ⚙️ Veri Düzenle")

    secim = st.selectbox("Parazit seç", list(parazit_verisi.keys()))
    veri = parazit_verisi.get(secim)

    if isinstance(veri, dict):
        mevcut = veri.get("bilgi") or veri.get("BİLGİ") or ""
    else:
        mevcut = veri

    yeni = st.text_area("Bilgi", mevcut)

    if st.button("Kaydet"):
        if isinstance(veri, dict):
            parazit_verisi[secim]["bilgi"] = yeni
        else:
            parazit_verisi[secim] = yeni

        veri_kaydet(parazit_verisi)
        st.success("Kaydedildi")
        st.rerun()


# -------------------------------
# FOOTER
# -------------------------------
st.markdown("---")
st.caption("© 2026 KAEÜ")
