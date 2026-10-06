# # # # # # # batas = 5
# # # # # # # for angka in range(batas):
# # # # # # #     print("Perulangan ke-", angka)

# # # # # # for sapa in range(5):
# # # # # #     print("halo, selamat siang")

# # # # # praktikum =  ["apd", "oRSIKOM", "jarkom", 78, 90, 88]
# # # # # for i in praktikum:
# # # # #     # print(i)
# # # # #     print(i, end=" ")

# # # # for i in range(1, 10, 2):
# # # #     print("angka ke-i adalah", i)

# # # for i in range(1, 3):# Mengontrol baris dalam tabel perkalian
# # #     for j in range(1, 4):# Mengontrol kolom dalam tabel perkalian
# # #         print(f'{i} x {j} = {i * j}')
# # #     print('')

# # # jawab = "ya"
# # # hitung = 0

# # # while(jawab == "ya"):
# # #     hitung += 1
# # #     jawab = input("Ulang lagi tidak? ")

# # # print(f"Total Perulangan : {hitung}")

# # # username = "husain"
# # # batas = 0
# # # while batas > 3:
# # #     login = input("masukkan username")
# # #     if login != username:
# # #         batas += 1
# # #     else:
# # #         batas = 3

# # # for i in range(10):
# # #     if i == 5:
# # #         break
# # # print(i) 

# # for i in range(10):
# #     if i % 2 == 0:
# #         continue
# #     print(i)

# tinggi = int(input("masukan tinggi yang dimau: "))
# for i in range(1, tinggi + 1):
#     print("*" *i)

tinggi = int(input("masukan tinggi yang dimau: "))
for i in range(1, tinggi + 1):
    spasi = " " * (tinggi - 1)
    tanda - "*" * i
    