# # Meminta input bilangan bulat dari pengguna
# N = int(input("Masukkan bilangan bulat (1-100): "))

# # Memastikan nilai N sesuai ketentuan
# if 1 <= N <= 100:
#     # Membuat pola segitiga siku-siku
#     for i in range(1, N + 1):
#         print('$' * i)
# else:
#     print("Input harus antara 1 sampai 100!")


# N = int(input("Masukkan bilangan bulat (1-100): "))
# kar = input("Masukkan karakter: ")

N = int(input("Masukkan bilangan bulat (1-100): "))
kar = input("Masukkan karakter: ")

# Validasi input
if 1 <= N <= 100 and len(kar) == 1:
    # Loop untuk membuat segitiga sama kaki
    for i in range(1, N + 1):
        spasi = ' ' * (N - i)      # spasi di sisi kiri
        pola = kar * (2 * i - 1)   # jumlah karakter per baris
        print(spasi + pola)
else:
    print("Input tidak valid! N harus 1-100 dan karakter hanya 1 simbol/huruf.")