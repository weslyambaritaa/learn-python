from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

# 📂 Path file Excel (ganti dengan path yang benar)
file_path = r"D:\Download\nomor.xlsx"

# 🔧 Konfigurasi WebDriver (Pastikan ChromeDriver sesuai dengan versi Chrome Anda)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # Biarkan browser tetap terbuka

driver = webdriver.Chrome(options=options)
driver.get("https://web.whatsapp.com")

input("📱 Silakan scan QR code lalu tekan ENTER untuk melanjutkan...")

try:
    df = pd.read_excel(file_path, header=None)

    for index, row in df.iterrows():
        nomor = f"{str(row[0])}"  # Nomor tanpa tanda +
        nama = f"{str(row[1])}"  # Nama pengguna
        pesan = f"Halo {nama}!, ini pesan otomatis dari sistem kami. Semoga harimu menyenangkan!   *Wesly Ambarita"
        url = f"https://web.whatsapp.com/send?phone={nomor}&text={pesan}"
        driver.get(url)

        time.sleep(10)  # Tunggu hingga WhatsApp memuat

        try:
            send_button = driver.find_element(By.XPATH, "//span[@data-icon='send']")
            send_button.click()
            print(f"✅ Pesan terkirim ke {nomor}")
        except:
            print(f"❌ Gagal mengirim ke {nomor}")

        time.sleep(1)  # Tunggu sebelum mengirim ke nomor berikutnya

    print("🎉 Semua pesan telah dikirim!")
except FileNotFoundError:
    print(f"❌ File {file_path} tidak ditemukan! Periksa kembali path-nya.")
except Exception as e:
    print(f"❌ Terjadi kesalahan: {e}")

# 🚪 Tutup browser setelah semua pesan terkirim
time.sleep(5)
driver.quit()
