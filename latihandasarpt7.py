print("=== PROGRAM SEWA MAKAM ===")

total_semua = 0
data_penyewa = []
ulang = "u"

while ulang.lower() == "u":
    print("\n--- Input Data Penyewa ---")
    nama = input("Nama penyewa: ")

    # Pilih tipe makam
    print("\nPilih tipe makam:")
    print("1. Reguler -> Rp5.000.000 / 5 tahun")
    print("2. VIP     -> Rp12.000.000 / 5 tahun")
    print("3. VVIP    -> Rp20.000.000 / 5 tahun")
    tipe = int(input("Masukkan pilihan (1-3): "))

    if tipe == 1:
        tipe_makam = "Reguler"
        harga_dasar = 5000000
    elif tipe == 2:
        tipe_makam = "VIP"
        harga_dasar = 12000000
    elif tipe == 3:
        tipe_makam = "VVIP"
        harga_dasar = 20000000
    else:
        print("Pilihan tidak valid!")
        continue

    # Lama sewa
    print("\nPilih lama sewa:")
    print("1. 5 tahun (harga tetap)")
    print("2. 10 tahun (+50%)")
    print("3. 15 tahun (+100%)")
    lama = int(input("Masukkan pilihan (1-3): "))

    if lama == 1:
        tahun = 5
        harga_sewa = harga_dasar
    elif lama == 2:
        tahun = 10
        harga_sewa = harga_dasar * 1.5
    elif lama == 3:
        tahun = 15
        harga_sewa = harga_dasar * 2
    else:
        print("Pilihan lama sewa tidak valid!")
        continue

    # Pilih perawatan
    print("\nApakah ingin layanan perawatan makam?")
    print("0. Tidak perlu perawatan")
    print("1. reguler  -> Rp500.000 / tahun")
    print("2. VIP    -> Rp1.000.000 / tahun")
    print("3. VVIP  -> Rp2.000.000 / tahun")
    pilih_rawat = int(input("Masukkan pilihan (0-3): "))

    if pilih_rawat == 0:
        jenis_rawat = "Tanpa perawatan"
        biaya_rawat_tahun = 0
    elif pilih_rawat == 1:
        jenis_rawat = "reguler"
        biaya_rawat_tahun = 500000
    elif pilih_rawat == 2:
        jenis_rawat = "VIP"
        biaya_rawat_tahun = 1000000
    elif pilih_rawat == 3:
        jenis_rawat = "VVIP"
        biaya_rawat_tahun = 2000000
    else:
        print("Pilihan tidak valid!")
        continue

    biaya_rawat = biaya_rawat_tahun * tahun
    total = harga_sewa + biaya_rawat
    total_semua += total

    # Simpan data
    data_penyewa.append([nama, tipe_makam, tahun, jenis_rawat, int(harga_sewa), int(biaya_rawat), int(total)])

    ulang = input("\nApakah ingin input penyewa berikutnya? (u/n): ")

# === LAPORAN ===
print("\n=== LAPORAN SEWA MAKAM ===")
print("-" * 100)
print(f"{'No':<3} {'Nama':<15} {'Tipe':<10} {'Lama':<8} {'Perawatan':<15} {'Sewa (Rp)':<15} {'Rawat (Rp)':<15} {'Total (Rp)':<15}")
print("-" * 100)

for i, d in enumerate(data_penyewa, 1):
    print(f"{i:<3} {d[0]:<15} {d[1]:<10} {d[2]:<8} {d[3]:<15} {d[4]:<15,} {d[5]:<15,} {d[6]:<15,}")

print("-" * 100)
print(f"{'TOTAL SEMUA PENYEWA':<83} Rp{int(total_semua):,}")
print("-" * 100)
print("Terima kasih telah menggunakan layanan sewa makam!")    