"""Arafat Febrian Dirza: dashboard interaktif sederhana, data peminjaman sintetis."""
import numpy as np
import pandas as pd
import streamlit as st
st.set_page_config(page_title="Dashboard Perpustakaan",layout="wide")
st.title("Dashboard Peminjaman Perpustakaan")
st.caption("Contoh studi IMK & visualisasi; semua angka bersifat simulasi.")
rng=np.random.default_rng(2026)
bulan=pd.date_range("2026-01-01",periods=12,freq="MS")
df=pd.DataFrame({"bulan":bulan,"Fiksi":rng.integers(40,100,12),"Sains":rng.integers(30,90,12),"Sejarah":rng.integers(20,75,12)})
jenis=st.multiselect("Pilih kategori buku",["Fiksi","Sains","Sejarah"],default=["Fiksi","Sains","Sejarah"])
if not jenis:
    st.info("Pilih minimal satu kategori untuk menampilkan grafik.")
else:
    d=df.set_index("bulan")[jenis]
    a,b=st.columns(2)
    a.metric("Total peminjaman",f"{int(d.sum().sum()):,}")
    b.metric("Kategori dipilih",len(jenis))
    st.line_chart(d)
    with st.expander("Tampilkan data tabel"):
        st.dataframe(d,use_container_width=True)
st.caption("Prinsip IMK: label jelas, filter mudah ditemukan, umpan balik saat pilihan kosong.")
