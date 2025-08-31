# Analisis Data: Bike Sharing Dataset

Proyek ini bertujuan untuk melakukan analisis data eksplorasi (EDA) pada dataset Bike Sharing untuk memahami pola penyewaan sepeda berdasarkan berbagai faktor seperti cuaca dan waktu.

## Latar Belakang

Layanan berbagi sepeda menjadi solusi populer untuk mobilitas perkotaan. Dengan menganalisis data historis penyewaan, kita dapat menemukan wawasan berharga yang dapat digunakan untuk mengoptimalkan operasional, seperti penempatan sepeda dan strategi pemasaran. Dataset ini berisi data penyewaan sepeda harian dan per jam dari tahun 2011 hingga 2012.

## Pertanyaan Bisnis

Analisis ini berfokus untuk menjawab pertanyaan-pertanyaan berikut:

1. Berapa jumlah penyewaan sepeda harian dan per jam berdasarkan cuaca?
2. Pada jam berapa sajakah puncak penyewaan sepeda terjadi?

## Struktur Proyek

```
.
├── data/
│   ├── day.csv
│   └── hour.csv
├── dashboard/
│   ├── dashboard.py
├── notebook.ipynb
└── README.md
```

- **`data/`**: Folder berisi dataset mentah.
- **`notebook.ipynb`**: Notebook Jupyter berisi proses analisis data eksplorasi (EDA) langkah demi langkah.
- **`dashboard.py`**: Skrip Python untuk membuat dasbor interaktif menggunakan Streamlit.
- **`README.md`**: Penjelasan mengenai proyek.

## Setup Lingkungan

Untuk menjalankan proyek ini, Anda disarankan menggunakan Conda untuk manajemen lingkungan.

1. Buat lingkungan Conda baru:
   ```bash
   conda create --name bike-sharing-analysis python=3.10
   ```
2. Aktifkan lingkungan:
   ```bash
   conda activate bike-sharing-analysis
   ```
3. Instal semua paket yang dibutuhkan:
   ```bash
   conda install pandas matplotlib seaborn streamlit babel
   ```

## Cara Menjalankan

### 1. Analisis Eksplorasi (Jupyter Notebook)

Buka dan jalankan file `notebook.ipynb` menggunakan Jupyter Notebook atau VS Code untuk melihat proses analisis data secara detail.

### 2. Dasbor Interaktif (Streamlit)

Untuk menjalankan dasbor, pastikan Anda berada di direktori utama proyek, lalu jalankan perintah berikut di terminal Anda:

```bash
streamlit run dashboard.py
```

Setelah itu, dasbor akan otomatis terbuka di browser Anda.

## Hasil Analisis

### Pola Penyewaan Berdasarkan Cuaca

- **Insight:** Jumlah penyewaan sepeda tertinggi terjadi pada saat cuaca cerah. Jumlahnya menurun secara signifikan seiring memburuknya kondisi cuaca, menunjukkan bahwa cuaca adalah salah satu faktor penentu dalam keputusan seseorang untuk menyewa sepeda.

### Puncak Jam Penyewaan

- **Insight:** Terdapat dua puncak penyewaan yang jelas pada hari kerja: **puncak pagi (08:00)** dan **puncak sore (17:00-18:00)**, yang sangat sesuai dengan pola berangkat dan pulang kerja.
