# =============================================
# PROGRAM HITUNG GAJI KARYAWAN PT. DINGIN DAMAI
# =============================================

print("PROGRAM HITUNG GAJI KARYAWAN")
print("=" * 40)

# ===== LAYAR MASUKKAN =====
nama = input("Nama Karyawan       : ")
golongan = int(input("Golongan Jabatan (1/2/3): "))
pendidikan = input("Pendidikan (SMA/D1/D3/S1): ").upper()
jam_kerja = int(input("Jumlah jam kerja    : "))

# ===== PERHITUNGAN =====
gaji_pokok = 3000000  # Gaji pokok Rp 3.000.000

# --- Tunjangan Jabatan ---
if golongan == 1:
    tunj_jabatan = 0.05 * gaji_pokok
elif golongan == 2:
    tunj_jabatan = 0.10 * gaji_pokok
elif golongan == 3:
    tunj_jabatan = 0.15 * gaji_pokok
else:
    tunj_jabatan = 0

# --- Tunjangan Pendidikan ---
if pendidikan == "SMA":
    tunj_pendidikan = 0.025 * gaji_pokok
elif pendidikan == "D1":
    tunj_pendidikan = 0.05 * gaji_pokok
elif pendidikan == "D3":
    tunj_pendidikan = 0.20 * gaji_pokok
elif pendidikan == "S1":
    tunj_pendidikan = 0.30 * gaji_pokok
else:
    tunj_pendidikan = 0

# --- Honor Lembur ---
if jam_kerja > 8:
    lembur = (jam_kerja - 8) * 70000 *20    # diganti 70.000 per jam
else:
    lembur = 0

# --- Total Gaji ---
total_gaji = gaji_pokok + tunj_jabatan + tunj_pendidikan + lembur

# ===== LAYAR KELUARAN =====
print("\nKaryawan yang bernama :", nama)
print("Honor yang diterima :")
print(f"  Tunjangan Jabatan     : Rp {tunj_jabatan:,.0f}")
print(f"  Tunjangan Pendidikan  : Rp {tunj_pendidikan:,.0f}")
print(f"  Honor Lembur          : Rp {lembur:,.0f}")
print("-" * 40)
print(f"Total Gaji              : Rp {total_gaji:,.0f}")