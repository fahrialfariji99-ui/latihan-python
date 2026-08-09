import datetime
import os

# ======================================
# Data Awal
# ======================================

kamar = {
    "A": {"nama": "Standard Room", "harga": 300000},
    "B": {"nama": "Deluxe Room", "harga": 500000},
    "C": {"nama": "Suite Room", "harga": 800000}
}

riwayat_file = "transaksi.txt"

# ======================================
# Fungsi Login
# ======================================
akun = {
    "admin": "12345",
    "resepsionis": "hotel2025",
    "user": "user123"
}

# Fungsi login
def login():
    print("===================================")
    print("         SISTEM LOGIN HOTEL        ")
    print("===================================")

    for percobaan in range(3):  # Maksimal 3 kali percobaan
        username = input("Masukkan Username : ")
        password = input("Masukkan Password : ")

        # Cek apakah username dan password sesuai
        if username in akun and akun[username] == password:
            print(f"\n✅ Login berhasil! Selamat datang, {username}.\n")
            return username  # Kembalikan nama pengguna
        else:
            sisa = 2 - percobaan
            print(f"❌ Username atau password salah! Sisa percobaan: {sisa}\n")

    print("🚫 Terlalu banyak percobaan. Akses ditolak.")
    return None

# ======================================
# Fungsi Menampilkan Daftar Kamar
# ======================================
def tampilkan_daftar_kamar():
    print("===============================================")
    print("               DAFTAR KAMAR HOTEL              ")
    print("===============================================")
    print("Kode   Jenis Kamar           Harga per Malam")
    print("-----------------------------------------------")
    for kode, info in kamar.items():
        print(f" {kode}     {info['nama']:<20} Rp. {info['harga']:,}")
    print("-----------------------------------------------")

# ======================================
# Fungsi Pemesanan Kamar
# ======================================
def pemesanan():
    tampilkan_daftar_kamar()
    nama = input("\nMasukkan nama tamu: ")
    kode = input("Masukkan kode kamar (A/B/C): ").upper()

    if kode not in kamar:
        print("❌ Kode kamar tidak valid!")
        return

    lama = int(input("Masukkan lama menginap (hari): "))

    harga = kamar[kode]["harga"]
    subtotal = harga * lama
    pajak = subtotal * 0.1  # 10% pajak
    diskon = 0

    # Diskon jika menginap lebih dari 5 malam
    if lama > 5:
        diskon = subtotal * 0.1  # 10% diskon
  
    total = subtotal + pajak - diskon
    tanggal = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")

    print("\n========== STRUK PEMBAYARAN ==========")
    print(f"Tanggal         : {tanggal}")
    print(f"Nama Tamu       : {nama}")
    print(f"Jenis Kamar     : {kamar[kode]['nama']}")
    print(f"Harga per Malam : Rp {harga:,}")
    print(f"Lama Menginap   : {lama} malam")
    print(f"Subtotal        : Rp {subtotal:,}")
    print(f"Pajak (10%)     : Rp {pajak:,}")
    print(f"Diskon          : Rp {diskon:,}")
    print("--------------------------------------")
    print(f"Total Bayar     : Rp {total:,}")
    print("======================================")
    print("Terima kasih telah menginap di Hotel Makmur!\n")

    # Simpan transaksi ke file
    with open(riwayat_file, "a") as f:
        f.write(f"{tanggal} | {nama} | {kamar[kode]['nama']} | {lama} malam | Rp {total:,}\n")

# ======================================
# Fungsi Menampilkan Riwayat Transaksi
# ======================================
def lihat_riwayat():
    print("\n========== RIWAYAT TRANSAKSI ==========")
    if not os.path.exists(riwayat_file):
        print("Belum ada transaksi yang tersimpan.")
        return
    with open(riwayat_file, "r") as f:
        data = f.read()
        if data.strip() == "":
            print("Belum ada transaksi.")
        else:
            print(data)
    print("========================================\n")

# ======================================
# Program Utama
# ======================================
def main():
    if not login():
        return

    while True:
        print("===== MENU UTAMA HOTEL MAKMUR =====")
        print("1. Lihat Daftar Kamar")
        print("2. Pesan Kamar")
        print("3. Lihat Riwayat Transaksi")
        print("4. Keluar")
        pilihan = input("Pilih menu (1-4): ")

        if pilihan == "1":
            tampilkan_daftar_kamar()
        elif pilihan == "2":
            pemesanan()
        elif pilihan == "3":
            lihat_riwayat()
        elif pilihan == "4":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("❌ Pilihan tidak valid. Coba lagi.\n")

# Jalankan program
if __name__ == "__main__":
    main()
