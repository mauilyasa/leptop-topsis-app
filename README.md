# Sistem Rekomendasi Laptop with TOPSIS

Ini adalah aplikasi web sederhana yang dibangun dengan Flask yang merekomendasikan laptop berdasarkan kriteria yang ditentukan pengguna menggunakan metode TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution).

## Fitur

- Pengguna dapat menambahkan laptop baru ke dalam database dengan spesifikasinya.
- Pengguna dapat memasukkan preferensi mereka untuk harga, performa, dan masa pakai baterai untuk mendapatkan rekomendasi.
- Rekomendasi ditampilkan berdasarkan metode TOPSIS, dengan mempertimbangkan kriteria input pengguna.

## Teknologi yang Digunakan

- Python
- Flask
- SQLAlchemy
- HTML/CSS (Bootstrap)

## Persiapan

1. **Klon repositori:**

    ```bash
    git clone https://github.com/usernameanda/sistem-rekomendasi-laptop.git
    ```

2. **Pasang dependensi:**

    ```bash
    cd leptop-topsis-app
    pip install -r requirements.txt
    ```

3. **Mempopulasikan data:**

    Anda perlu mempopulasikan basis data dengan laptop-laptop sampel sebelum menjalankan aplikasi. Jalankan perintah berikut:

    ```bash
    python populate_data.py
    ```

4. **Jalankan aplikasi Flask:**

    ```bash
    python app.py
    ```

5. **Buka browser web Anda dan buka [http://{your-ip}:5000] atau [http://localhost:5000](http://localhost:5000) untuk mengakses aplikasi.**

## Preview

![image](https://github.com/mauilyasa/leptop-topsis-app/assets/133037454/1b81c0cf-9e1c-4e11-9c35-1819df897925)



