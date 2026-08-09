#identifikasi input
berat_telur = 5 #kilogram
harga_telur_per_kg = 26000 #rupiah
tarif_angkot_sekali_jalan = 3500 #rupiah
uang_ibu = 200000 #rupiah

#hitung total biaya telur
total_biaya_telur = berat_telur * harga_telur_per_kg

#hitung total biaya transportasi
total_biaya_transpotasi = 2* tarif_angkot_sekali_jalan

#hitung total pengeluaran 
total_pengeluaran = total_biaya_telur + total_biaya_transpotasi

#hitung sisa uang 
sisa_uang = uang_ibu - total_pengeluaran

#tampilkan hasil
print(f"Total biaya telur: Rp {total_biaya_telur}")
print(f"Total biaya transportasi: Rp{total_biaya_transpotasi}")
print(f"Total prngrluaran: Rp{total_pengeluaran}")
print(f"Sisa uang ibu: Rp{sisa_uang}")