import os
import subprocess

# Fungsi untuk mengecek versi Polkit
def check_polkit_version():
    try:
        # Menjalankan perintah untuk melihat versi polkit
        result = subprocess.run(['pkexec', '--version'], capture_output=True, text=True)
        if '0.105' in result.stdout:  # Versi yang diketahui rentan adalah 0.105
            print("Polkit rentan terdeteksi. Silakan perbarui Polkit segera.")
        else:
            print(f"Polkit aman. Versi saat ini: {result.stdout.strip()}")
    except Exception as e:
        print(f"Gagal memeriksa versi Polkit: {str(e)}")

# Fungsi untuk mengecek file mencurigakan di direktori /tmp
def check_suspicious_files():
    suspicious_files = ['/tmp/httpd', '/tmp/sh']  # File umum yang dipakai malware Perfctl
    for file in suspicious_files:
        if os.path.exists(file):
            print(f"File mencurigakan terdeteksi: {file}. Segera lakukan tindakan.")
        else:
            print(f"Tidak ada file mencurigakan: {file}")

# Fungsi untuk menonaktifkan Polkit jika tidak dibutuhkan
def disable_polkit():
    try:
        # Menonaktifkan layanan polkit
        subprocess.run(['systemctl', 'disable', 'polkit'], check=True)
        print("Polkit telah dinonaktifkan.")
    except Exception as e:
        print(f"Gagal menonaktifkan Polkit: {str(e)}")

if __name__ == "__main__":
    check_polkit_version()
    check_suspicious_files()

    # Jika ingin menonaktifkan Polkit
    response = input("Apakah Anda ingin menonaktifkan Polkit? (y/n): ")
    if response.lower() == 'y':
        disable_polkit()
