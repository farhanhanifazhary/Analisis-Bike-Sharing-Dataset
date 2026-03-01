# Bike Sharing Data Analysis

## Latar Belakang

Sistem bike sharing memungkinkan pengguna menyewa sepeda secara otomatis dalam waktu singkat.  
Analisis ini bertujuan untuk memahami:

1. Faktor apa yang paling mempengaruhi jumlah peminjaman sepeda, dan kapan permintaan tertinggi terjadi?
2. Bagaimana perbedaan perilaku antara pengguna casual dan registered?

Dataset yang digunakan adalah `day.csv`.

---

# Gambaran Umum Sistem

- Total observasi: 731 hari
- Rata-rata rental per hari: ± 4.504 sepeda
- Total casual user: 620.017
- Total registered user: 2.672.662
- Registered ≈ 4.3 kali lebih banyak dibanding casual (~81% dari total penggunaan)

### Insight Awal
Sistem bike sharing lebih banyak digunakan sebagai **transportasi rutin** dibanding sekadar rekreasi.

---

# 1. Faktor yang Mempengaruhi Jumlah Peminjaman Sepeda

## Pengaruh Temperatur

- Korelasi temperatur terhadap rental ≈ 0.63
- Hubungan positif yang cukup kuat

**Interpretasi:**  
Semakin hangat suhu, semakin tinggi jumlah peminjaman sepeda. Temperatur merupakan faktor lingkungan paling berpengaruh dalam dataset ini.

---

## Pengaruh Cuaca

Rata-rata rental berdasarkan kondisi cuaca:

- Cuaca cerah → tertinggi
- Cuaca mendung ringan → menurun
- Cuaca buruk → turun drastis

Namun:
- Cuaca buruk hanya terjadi pada sebagian kecil observasi.

**Insight:**  
Cuaca ekstrem memang menurunkan demand secara signifikan, tetapi frekuensinya rendah sehingga kontribusi totalnya kecil terhadap sistem secara keseluruhan.

---

## Pengaruh Musim

- Musim hangat menunjukkan rata-rata rental tertinggi.
- Musim tersebut juga memiliki variasi (CV) lebih rendah → lebih stabil.

**Insight:**  
Musim hangat tidak hanya meningkatkan demand, tetapi juga membuat pola penggunaan lebih konsisten.

---

## Hari Kerja vs Non-Hari Kerja

- Mean rental hari kerja sedikit lebih tinggi.
- Hari kerja menyumbang lebih dari dua kali total rental dibanding non-hari kerja.
- Variasi demand lebih stabil pada hari kerja.

**Insight:**  
Hari kerja merupakan tulang punggung sistem bike sharing dan mencerminkan pola commuting yang konsisten.

---

# Kapan Permintaan Tertinggi Terjadi?

permintaan tertinggi secara harian terjadi pada:
- Cuaca baik
- Temperatur hangat

---

# 2. Perbedaan Perilaku Casual vs Registered

## istribusi Pengguna

- Registered mendominasi sistem (~81%)
- Casual jauh lebih sedikit (~19%)

**Interpretasi:**  
Sistem lebih berfungsi sebagai sarana transportasi rutin daripada sekadar aktivitas rekreasi.

---

# Kesimpulan Utama

1. Temperatur dan musim hangat merupakan faktor lingkungan paling berpengaruh terhadap peningkatan rental.
2. Permintaan tertinggi terjadi pada cuaca baik dan temperature hangat
3. Hari kerja menyumbang sebagian besar total penggunaan sistem.
4. Registered user mendominasi penggunaan sistem.

---

# Implikasi Bisnis

- Sistem bike sharing berperan sebagai solusi mobilitas perkotaan.
- Forecasting demand dapat difokuskan pada faktor waktu dan temperatur.
- Strategi pertumbuhan dapat difokuskan pada konversi pengguna casual di periode aktivitas tinggi.

# 3. Menjalankan Dashboard

Ikuti langkah berikut untuk menjalankan dashboard Bike Sharing menggunakan Streamlit.

---

## 1. Install Dependencies

Karena seluruh library sudah tercantum di `requirements.txt`, jalankan:

```bash
pip install -r requirements.txt
```

Pastikan proses instalasi selesai tanpa error.

---

## 2. Pastikan Struktur Folder Benar

Struktur folder minimal:

```
submission/
│
├── dashboard/
|   ├── dashboard.py
├── data/
|   ├── day.csv
├── notebook.ipynb
├── README.md
├── requirements.txt
└── url.txt
```

---

## 3. Jalankan Streamlit

Di terminal, jalankan:

```bash
streamlit run app.py
```

---

## 4. Akses Dashboard

Setelah dijalankan, Streamlit akan menampilkan URL seperti:

```
Local URL: http://localhost:8501
```

Buka URL tersebut di browser untuk melihat dashboard.

---

## 5. Menghentikan Dashboard

Tekan:

```
CTRL + C
```

di terminal untuk menghentikan aplikasi.

---