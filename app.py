import streamlit as st
import json

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
# 📌 YARDIMCI FONKSİYON (BUTON)
# -------------------------------
def parazit_yazdir(isim):
    veri = parazit_verisi.get(isim)

    if veri:
        if st.button(isim, key=isim):
            parazit_kart(isim, veri)


# -------------------------------
# 📌 VERİ YÜKLE
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

parazit_verisi = st.session_state.veri


# -------------------------------
# 📌 SAYFA AYAR
# -------------------------------
st.set_page_config(
    page_title="KAEÜ Parazitoloji",
    page_icon="🔬",
    layout="wide"
)

st.title("🔬 KAEÜ Parazitoloji Veri Bankası")


# -------------------------------
# 📌 SEKMELER
# -------------------------------
tab1, tab2 = st.tabs(["🔍 Arama", "🗂️ Sınıflandırma"])


# -------------------------------
# 🔍 SEKME 1
# -------------------------------
with tab1:
    sorgu = st.text_input("Parazit ara")

    if sorgu:
        for isim, veri in parazit_verisi.items():
            if sorgu.lower() in isim.lower():
                st.subheader(isim)

                if st.button(f"Bilgi Aç: {isim}", key=f"sorgu_{isim}"):
                    parazit_kart(isim, veri)


# -------------------------------
# 🗂️ SEKME 2
# -------------------------------
with tab2:
    st.subheader("📚 Sistematik Sınıflandırma")

    col1, col2 = st.columns(2)

    # -------------------------------
    # PROTOZOONLAR
    # -------------------------------
    with col1:
        st.markdown("### 🧫 Protozoonlar")

        with st.expander("Amipler"):
            amipler = [
                "Entamoeba histolytica",
                "Entamoeba coli",
                "Entamoeba dispar"
            ]

            for p in amipler:
                parazit_yazdir(p)

    # -------------------------------
    # HELMİNTLER
    # -------------------------------
    with col2:
        st.markdown("### 🐛 Helmintler")

        with st.expander("Nematodlar"):
            nematodlar = [
                "Ascaris lumbricoides",
                "Enterobius vermicularis"
            ]

            for p in nematodlar:
                parazit_yazdir(p)
