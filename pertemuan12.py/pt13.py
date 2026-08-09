def jadwal_harian(daftar_tugas):
    #urutkan tugas berdasarkan durasi (paling singkat dahulu)
    # ini adalah strategi greedy: "Biar Cepet selesai Banyak"
    tugas_urut = sorted(daftar_tugas,key=lambda x: x ['durasi'])

    waktu_sekarang = 0
    urutan_selesai = []


    print("--- Rencana Kerja Greedy Hari Ini ---")
    for tugas in tugas_urut:
        waktu_sekarang+=tugas['durasi']
        urutan_selesai.append(tugas['nama'])
        print(f"Menyelesaikan: {tugas['nama']} (Butuh {tugas['durasi']} menit )")

    return urutan_selesai,waktu_sekarang


# Daftar tugas acak 
tugas_saya = [
    {"nama":"balas email","durasi":10},
    {"nama":"cuci mobil","durasi":60},
    {"nama":"beli token listrik","durasi":5},
    {"nama":"masakan makan siang","durasi":30}
]

hasil, total_waktu = jadwal_harian(tugas_saya)

print("\n--- KESIMPULAN ---")
print(f"urutan kerja: {"->".join(hasil)}")
print (f"Total waktu produktif: {total_waktu} menit")