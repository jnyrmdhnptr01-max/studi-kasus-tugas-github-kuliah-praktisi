# 6 Studi Kasus Informatics Practitioner Lecture Series 2026 — Versi Teman

Paket **berbeda dari versi pertama**, disusun berdasarkan enam topik pemateri. Data seluruhnya **sintetis / ilustratif**, sehingga hasil latihan tidak boleh ditafsirkan sebagai temuan penelitian nyata.

| No | Materi pemateri | Studi kasus versi ini | File |
|---|---|---|---|
| 1 | Andrea Arisal — Data Analytics & AI | Mengevaluasi kekurangan stok toko | `cases/01_analisis_persediaan.py` |
| 2 | Dr. Warawan — HPC | Simulasi antrean loket multi-skenario | `cases/02_simulasi_antrian_hpc.py` |
| 3 | Widi Prima Depa — GIS | Prioritas penanganan titik sampah | `cases/03_gis_prioritas_sampah.py` |
| 4 | Dr. Taniza Tajudin — Machine Learning | Prediksi kelulusan (data simulasi) | `cases/04_ml_kelulusan.py` |
| 5 | Arafat Febrian Dirza — HCI & Data Visualization | Dashboard peminjaman perpustakaan | `cases/05_dashboard_perpustakaan.py` |
| 6 | Dr. Bart Slachter — Satellite & AI for Forests | Deteksi perubahan vegetasi lewat NDVI sintetis | `cases/06_deteksi_perubahan_vegetasi.py` |

## Cara menjalankan

Gunakan Python 3.10 atau lebih baru, lalu buka terminal pada folder proyek.

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
# source .venv/bin/activate
pip install -r requirements.txt
python cases/01_analisis_persediaan.py
python cases/02_simulasi_antrian_hpc.py
python cases/03_gis_prioritas_sampah.py
python cases/04_ml_kelulusan.py
python cases/06_deteksi_perubahan_vegetasi.py
streamlit run cases/05_dashboard_perpustakaan.py
```

Hasil CSV dan gambar untuk lima skrip akan disimpan di `outputs/`. Dashboard Streamlit dijalankan melalui browser dan tidak memerlukan dataset eksternal.

## Penjelasan dan pembahasan singkat

**01. Stok toko.** Pertanyaan: produk mana paling sering kekurangan stok? Proses: buat data permintaan-stok → hitung kekurangan → bandingkan rasio antarkategori. Keterbatasan: belum memperhitungkan ongkos restok, margin, dan faktor musiman. Sesuai konsep data → informasi → insight → keputusan.

**02. Antrean loket.** Pertanyaan: bagaimana jumlah loket memengaruhi rata-rata waktu tunggu? Proses: simulasi acak kedatangan dan pelayanan, mengulang 50 kali per konfigurasi, membandingkan rata-rata. Catatan: ini pengantar **beban kerja simulasi** dalam HPC, bukan benchmark superkomputer maupun implementasi paralel sejati.

**03. GIS sampah.** Pertanyaan: titik mana ditangani terlebih dahulu? Proses: data titik koordinat ilustratif → hitung jarak ke titik pusat → beri skor berbobot dari volume dan laporan → visualisasikan. Skor adalah keputusan desain latihan, bukan rekomendasi kebijakan nyata.

**04. Klasifikasi kelulusan.** Pertanyaan: dapatkah riwayat belajar digunakan untuk memprediksi kelas kelulusan? Proses: data sintetis → split stratified train/test → standardisasi → regresi logistik → classification report. Jangan gunakan hasil untuk menilai siswa nyata.

**05. Dashboard.** Pertanyaan: bagaimana petugas dapat melihat tren peminjaman dengan antarmuka sederhana? Prinsip: visibilitas filter, pesan umpan balik, label jelas, tabel detail jika dibutuhkan, dan ringkasan metrik.

**06. Perubahan vegetasi.** Pertanyaan: dapatkah perubahan indeks vegetasi digunakan sebagai penanda awal? Proses: band merah dan NIR sintetis sebelum-sesudah → NDVI → selisih NDVI → threshold → peta. Ini **bukan** klasifikasi penyebab deforestasi berbasis CNN. Untuk kasus penelitian nyata perlu Sentinel-1/Sentinel-2, label referensi, dan verifikasi lapangan sebagaimana dijelaskan pemateri.

## Cara upload ke GitHub

1. Buat repository baru, misalnya `praktisi-lecture-studi-kasus-versi-2`.
2. Unggah **isi folder proyek** (termasuk folder `cases` dan `outputs`) melalui **Add file → Upload files**.
3. Tekan **Commit changes** lalu salin link repositori.
4. Alternatif terminal (setelah membuat repositori kosong di GitHub):

```bash
git init
git add .
git commit -m "Add six practitioner lecture case studies"
git branch -M main
git remote add origin https://github.com/USERNAME/NAMA-REPOSITORY.git
git push -u origin main
```

Ganti `USERNAME/NAMA-REPOSITORY` dengan milik sendiri. Jangan mengunggah informasi pribadi, token, atau kunci akses.

**Catatan akademik:** Sebelum dikumpulkan, pelajari dan sesuaikan pembahasan, serta sebutkan bahwa data dalam proyek merupakan simulasi.
