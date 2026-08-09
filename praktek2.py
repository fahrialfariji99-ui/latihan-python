# input
pembeli=input("Masukan nama pembeli :")
no_hp=input("input No, Hendphond : ")
jurusan=input("Inpur Juurusan [SBY/BL/LMP]")
#proses
if jurusan =="SBY":
    namajurusan="Surbaya"
    harga=30000

    
elif jurusan == "BL":
    namajurusan = "bali"
    harga = 50000
else:
    namajurusan="lampung"
    harga= 50000
    
#input jumlah beli
jumlah=int(input("masukan jumlah beli : "))
#proses potongan  
if jumlah>=3 :
    potongan=(jumlah*harga)* 0.1
else:
    potongan=0

total=(jumlah*harga )-potongan

#cetakhasil
print("---------------------------------")
print("       PENJUALAN TIKET BUS"     )
print("                XYZ")
print("nama pembeli :"+str(pembeli))
print("No. Hanphone :"+str(no_hp))
print("Kode jurusan yang di pilih : " +str(jurusan))
print("harga            :", +(harga))
print("jumlah beli      : ", (jumlah))
print("-----------------------------------")
print("potongan yang di dapat : ", +(potongan))
print("Total bayar   :",+ (total))
ubay=int (input("masukkan uang bayar :"))
uangkembali=ubay-total
print("uang kembali   : ", +uangkembali)