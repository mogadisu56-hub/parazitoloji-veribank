import streamlit as st

# ---------------- DIALOG ----------------
@st.dialog("📌 Parazit Bilgi Kartı")
def parazit_kart(isim, veri):
    if isinstance(veri, dict):
        icerik = veri.get("bilgi") or veri.get("BİLGİ") or "Bilgi yok"
    else:
        icerik = veri

    st.markdown(f"### {isim}")
    st.write(icerik)


# ---------------- YARDIMCI FONKSİYON ----------------
def parazit_yazdir(isim):
    if isim in parazit_verisi:
        if st.button(isim, key=isim):
            parazit_kart(isim, parazit_verisi[isim])
    else:
        st.write(f"{isim} (veri yok)")


# ---------------- VERİ ----------------
parazit_verisi = {
    "Entamoeba histolytica": {
        "bilgi": "Patojen amip. Dizanteri ve karaciğer apsesi yapar."
    },
    "Entamoeba coli": {
        "BİLGİ": "Non-patojen. Hijyen göstergesidir."
    },
    "Entamoeba dispar": {
        "BİLGİ": "Non-patojen. E. histolytica ile ayırt edilmelidir."
    },
    "Giardia intestinalis": "İnce bağırsakta yaşar. Yağlı ishal yapar.",
    "Trichomonas vaginalis": "Cinsel yolla bulaşır.",
    "Ascaris lumbricoides": "En büyük bağırsak nematodu.",
    "Enterobius vermicularis": "Kıl kurdu.",
    "Taenia saginata": "Sığır şeridi.",
    "Fasciola hepatica": "Karaciğer kelebeği.",
    "Sarcoptes scabiei": "Uyuz etkeni."
}

# ---------------- SAYFA ----------------
st.set_page_config(page_title="Parazitoloji", layout="wide")

tab1, tab2 = st.tabs(["🔍 Sorgu", "🗂️ Parazitler"])

# ---------------- TAB 1 ----------------
with tab1:
    sorgu = st.text_input("Ara")

    if sorgu:
        for isim, veri in parazit_verisi.items():
            if sorgu.lower() in isim.lower():
                if st.button(isim, key=f"arama_{isim}"):
                    parazit_kart(isim, veri)

# ---------------- TAB 2 ----------------
with tab2:
    st.subheader("Protozoonlar")

    with st.expander("Amipler"):
        parazit_yazdir("Entamoeba histolytica")
        parazit_yazdir("Entamoeba coli")
        parazit_yazdir("Entamoeba dispar")

    with st.expander("Kamçılılar"):
        parazit_yazdir("Giardia intestinalis")
        parazit_yazdir("Trichomonas vaginalis")

    st.subheader("Helmintler")

    with st.expander("Nematodlar"):
        parazit_yazdir("Ascaris lumbricoides")
        parazit_yazdir("Enterobius vermicularis")

    with st.expander("Sestodlar"):
        parazit_yazdir("Taenia saginata")

    with st.expander("Trematodlar"):
        parazit_yazdir("Fasciola hepatica")

    st.subheader("Artropodlar")

    with st.expander("Akarlar"):
        parazit_yazdir("Sarcoptes scabiei")
