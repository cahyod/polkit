# polkit
Pengecekan dan perbaikan sistem dari celah keamanan polkit
## Pendahuluan
Untuk mengecek dan mencegah eksploitasi CVE-2021-4043 dengan Python, kita bisa membuat skrip yang melakukan beberapa pemeriksaan sistematis dan langkah mitigasi. Berikut adalah contoh langkah dasar yang bisa dilakukan:
1. Mengecek Versi Polkit: Skrip ini akan memeriksa apakah Polkit sudah diperbarui atau masih rentan.
2. Memantau Keberadaan File dan Proses Mencurigakan: Kita bisa memeriksa direktori seperti /tmp untuk file mencurigakan yang sering digunakan oleh malware.
3. Mencegah Eksekusi Polkit Jika Tidak Dibutuhkan: Jika Polkit tidak digunakan di sistem, kita bisa menonaktifkannya.
## Penjelasan skrip
1. Cek Versi Polkit: Skrip ini memeriksa apakah versi Polkit yang diinstal adalah yang rentan (0.105). Jika ya, Anda harus segera memperbaruinya.
2. Cek File Mencurigakan: Malware Perfctl sering menggunakan direktori /tmp untuk menjalankan proses berbahaya. Skrip ini memeriksa apakah ada file mencurigakan yang mungkin merupakan indikasi infeksi.
3. Menonaktifkan Polkit: Jika Polkit tidak diperlukan, Anda dapat memilih untuk menonaktifkannya.
## Catatan Penting: Setelah menjalankan skrip ini, pastikan sistem Anda diperbarui dan lakukan pemeriksaan berkala pada integritas file dan proses yang berjalan.
