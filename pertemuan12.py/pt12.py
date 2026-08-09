while True:
    print("\n================= Milenial Cellular Shop =================")
    no_imei = input("No Imei                : ")

    print("\nJenis Handphone")
    print("1. Samsung")
    print("2. Oppo")
    print("3. Vivo")

    kode_hp = input("Pilih Kode Handphone [S/O/V] : ").upper()
    tipe_hp = input("Pilih Tipe Handphone [A/B/C] : ").upper()
    jumlah_beli = int(input("Jumlah Beli                   : "))

    # Menentukan Nama HP dan Harga
    harga_hp = 0
    bonus = "-"

    if kode_hp == "S":
        nama_hp = "Samsung"
        if tipe_hp == "A": harga_hp = 5000000
        elif tipe_hp == "B": harga_hp = 4000000
        elif tipe_hp == "C": harga_hp = 3000000
    elif kode_hp == "O":
        nama_hp = "Oppo"
        if tipe_hp == "A": harga_hp = 3500000
        elif tipe_hp == "B": harga_hp = 1900000
        elif tipe_hp == "C": harga_hp = 350000
    elif kode_hp == "V":
        nama_hp = "Vivo"
        if tipe_hp == "A": harga_hp = 4000000
        elif tipe_hp == "B": harga_hp = 2500000
        elif tipe_hp == "C": harga_hp = 1000000
    else:
        print("Kode HP tidak valid!")
        continue

    # Hitung Total Harga
    total_harga = harga_hp * jumlah_beli

    # Menentukan Potongan dan Bonus
    if total_harga > 10000000:
        potongan = total_harga * 0.10
        bonus = "Tas Ransel"
    elif total_harga > 5000000:
        potongan = total_harga * 0.05
        bonus = "Tshirt"
    else:
        potongan = 0
        bonus = "-"

    # Total Bayar
    total_bayar = total_harga - potongan

    print("\n================= Milenial Cellular Shop =================")
    print(f"No Imei            : {no_imei}")
    print(f"Nama Handphone     : {nama_hp}")
    print(f"Jenis Handphone    : {tipe_hp}")
    print(f"Harga Handphone    : Rp {harga_hp:,}")
    print(f"Jumlah Beli        : {jumlah_beli}")
    print("==========================================================")
    print(f"Total Harga        : Rp {total_harga:,}")
    print(f"Potongan           : Rp {int(potongan):,}")
    print(f"Bonus              : {bonus}")

    print(f"Total Bayar        : Rp {int(total_bayar):,}")
    uang_bayar = int(input("Uang Bayar         : Rp "))
    uang_kembali = uang_bayar - total_bayar
    print(f"Uang Kembali       : Rp {int(uang_kembali):,}")
    print("==========================================================")

    ulang = input("\nIngin Input Data Lagi? [Y/T] : ").upper()
    if ulang != "Y":
        break