# ulang=2
# for i in range(ulang):
#  print ("data Ke- " + str(i+1))
#  nama=input("Masukkan Nim anda : ")
#  uts=int(input("Masukkan Nilai UTS anda :"))
#  uas=int(input("Masukkan Nilai UAS : "))
#  print("NIm anda adalah %s nilai UTS anda %i nilai UTS anda %i" % (nama,uts,uas))
#  print("-------------------------------------\n")




 
print("===============================================")
print("                GEROBAK FRIED CHICKEN          ")
print("===============================================")
print("Kode   Jenis Potong        Harga")
print("-----------------------------------------------")
print(" D      Dada               Rp. 15000")
print(" P      Paha               Rp. 10000")
print(" S      Sayap              Rp. 8000")
print("-----------------------------------------------")

# Daftar harga ayam
harga_ayam = {
    'D': 15000,
    'P': 10000,
    'S': 8000
}

# Layar Masukan
banyak_jenis = int(input("Banyak Jenis : "))

daftar_beli = []

for i in range(banyak_jenis):
    print(f"\nJenis ke-{i+1}")
    kode = input("Kode Potong [D/P/S] : ").upper()
    if kode not in harga_ayam:
        print("Kode salah! Gunakan D, P, atau S.")
        continue
    banyak = int(input("Banyak Potong : "))

    if kode == 'D':
        jenis = "Dada"
    elif kode == 'P':
        jenis = "Paha"
    else:
        jenis = "Sayap"

    harga = harga_ayam[kode]
    jumlah = harga * banyak
    daftar_beli.append((jenis, harga, banyak, jumlah))

# Hitung total
total = sum(item[3] for item in daftar_beli)
pajak = total * 0.10
total_bayar = total + pajak

# Layar Keluaran
print("\n===============================================")
print("                GEROBAK FRIED CHICKEN          ")
print("-----------------------------------------------")
print("No  Jenis Potong   Harga Satuan   Banyak   Jumlah")
print("-----------------------------------------------")

for i, item in enumerate(daftar_beli, start=1):
    print(f"{i:<3} {item[0]:<13} Rp{item[1]:<10} {item[2]:<7} Rp{item[3]}")

print("-----------------------------------------------")
print(f"Jumlah Bayar                        Rp {total}")
print(f"Pajak 10%                           Rp {int(pajak)}")
print(f"Total Bayar                         Rp {int(total_bayar)}")
print("===============================================")
print("Terima kasih telah membeli di Gerobak Fried Chicken!")