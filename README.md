# Web-Rumpiii (mytodo)

Ringkasan singkat
-----------------
Ini adalah aplikasi Django sederhana untuk membuat posting, komentar, dan like. Aplikasi utama berada di `todos` dan menggunakan SQLite (`db.sqlite3`) sebagai database bawaan. Template HTML dan file statis ada di folder `templates` dan `static`.

Fitur
------
- Daftar postingan (urut dari terbaru)
- Detail postingan dengan komentar
- Membuat, mengedit, menghapus postingan (hanya oleh author)
- Like / Unlike postingan
- Registrasi dan login pengguna
- Dashboard admin untuk mengelola pengguna

Struktur proyek (penting)
-------------------------
- `manage.py` - entry point untuk menjalankan perintah Django
- `mytodo/` - konfigurasi Django (settings, urls, wsgi)
- `todos/` - aplikasi utama (models, views, forms, templates terkait)
- `templates/` - template HTML untuk tampilan
- `static/` - aset statis (CSS, JS, gambar)
- `db.sqlite3` - database SQLite (jika sudah dibuat)

Persyaratan
-----------
- Python 3.8+
- Django 4.x (direkomendasikan)

Jika ada file `requirements.txt`, gunakan itu untuk menginstal dependensi.

Menjalankan proyek (Windows PowerShell)
---------------------------------------
1. Buka PowerShell dan pindah ke folder proyek:

```powershell
Set-Location "C:\Users\Lenovo\OneDrive\Documents\Berkas_Adrian Syahputra\Project\mytodo"
```

2. (Direkomendasikan) Buat dan aktifkan virtual environment:

```powershell
python -m venv .venv
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process  # jika perlu
.\.venv\Scripts\Activate.ps1
```

3. Perbarui pip dan instal dependensi:

```powershell
pip install --upgrade pip
# Jika ada requirements.txt:
pip install -r .\requirements.txt
# Jika tidak ada, instal minimal Django:
pip install "django>=4.0"
```

4. Terapkan migrasi database:

```powershell
python manage.py migrate
```

5. (Opsional) Buat superuser untuk akses admin:

```powershell
python manage.py createsuperuser
```

6. Jalankan development server:

```powershell
python manage.py runserver
```

Kemudian buka browser ke `http://127.0.0.1:8000`.

Debug & troubleshooting singkat
-------------------------------
- Couldn't import Django: pastikan virtualenv aktif dan Django terinstal di environment.
- Permission saat Activate.ps1: jalankan `Set-ExecutionPolicy -Scope Process RemoteSigned` sebelum mengaktifkan.
- Port 8000 sibuk: jalankan `python manage.py runserver 8001` (ganti port).
- Jika ada error dependency: install paket yang tercantum pada pesan error, atau buat `requirements.txt`.

Catatan pengembang
------------------
- Autentikasi mendukung login dengan username atau email lewat `todos.authentication.EmailBackend`.
- Model penting: `Post`, `Comment`, `Like` di `todos/models.py`.

Kontribusi
----------
Silakan buat branch baru untuk fitur/perbaikan, dan kirim pull request. Sertakan deskripsi perubahan dan langkah reproduksi bila perlu.

Lisensi
-------
Tambahkan license file jika ingin membagikan proyek secara publik.
