kode_baju = input("Masukan kode Baju [5P/AD] : ")
ukuran = input ("masukan ukuran baju [S/M] : ")

if kode_baju == "sp" or kode_baju == "sp" :
    merk = "SuperDry"
    if ukuran == "S" or ukuran =="s":
        harga = 45000
    elif ukuran == "M" or ukuran =="m":
        harga = 50000
    else:
        harga = 0
elif kode_baju == "AD" or kode_baju =="ad":
    merk = "Adidas"
    if ukuran =="s" or ukuran == "S":
        harga = 650000
    elif  ukuran == "M" or  ukuran == "m":
        harga = 700000
    else:
        harga = 0

else: 
    merek = "Anda salah input kode merek"
    harga = 0
print("-----------------------")
print("Merek Baju : " +str(merek))
print("harga baju : Rp.",harga)

