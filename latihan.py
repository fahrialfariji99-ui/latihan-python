print("*****************")
print("TOKO MAINAN ANAK")
print("*****************")

nama_pembeli = input("nama pembeli : ")
kode_mainan = input("kode mainan : ")
harga = int(input("harga : "))
jumlah_beli = int(input("jumlah beli : "))

sub_total =harga * jumlah_beli
diskon = sub_total * 0.10
ppn = sub_total * 0.10
total = sub_total - diskon +ppn


print("\nstruk pembelian")
print("nama_pembeli : " + nama_pembeli)
print("kode mainan : " + str(kode_mainan))
print("harga : " + str (harga ))
print("jumlah_beli : "+ str (jumlah_beli))
print("sub_total : " + str (sub_total))
print("ppn : " + str(ppn))
print("total_bayar : " + str (total ))
