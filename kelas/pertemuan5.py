# # # formula1 = ["Suzuka", 10, True, 20.30, ["Lewis Hamilton", 2, 2.50]]
# # # print(formula1)

# # # formula1 = ["Suzuka", 10, True, 20.30, ["Lewis Hamilton", 2, 2.50]]
# # # print(formula1[3])
# # # # Output
# # # 20.30
# # # print(formula1[4][0])
# # # # Output
# # # "Lewis Hamilton"

# # sirkuit = ["Suzuka", "Monza", "Silverstone", "Marina Bay"]
# # print(sirkuit)
# # # Output
# # ['Suzuka', 'Monza', 'Silverstone', 'Marina Bay']
# # sirkuit.append("Spa-Francorchamps")
# # print(sirkuit)
# # # Output
# # ['Suzuka', 'Monza', 'Silverstone', 'Marina Bay', 'Spa-Francorchamps']

# lemari = ["celana panjang", "baju" , 69, 7.2, True]
# print("sebelum di extend")
# print("lemari")
# lemari.append(["ktp", "sepatu", "dompet"])
# print("sesudah di extend")

# lemari = ["baju", "celana", 69, 7.2, True, 70, 222, 240]

# jumlah = 0
# for item in lemari:
#     if type (item) == int:
#         jumlah += 1
# print (jumlah) 

# for index, item in enumerate(lemari):
#     print(f"indeks ke-{index + 1} : {item}")

# print("sebelum di ubah")
# print(lemari)
# lemari[0:2] = ["celana panjang", "jaket", "jas hujan"]

# del lemari[1]
# lemari.remove(69)
# sisa_lemari = lemari.pop(3)
# print(sisa_lemari)

# print("sesudah di ubah")
# print(lemari)

# 1. Operator penjumlahan
# Operator ini digunakan untuk menggabungkan dua buah list menjadi satu.

# team1 = ["Mercedes", "Ferrari", "MacLaren"]
# team2 = ["Red Bull", "Alpine", "Aston Martin"]
# gabung_team = team1 + team2
# print(gabung_team)

# 2. Operator pengulangan
# Operator ini digunakan untuk mengulang isi dari sebuah list sebanyak n kali.

# juara_WDC = ["MacLaren", "Red Bull"]
# juara = juara_WDC * 3
# print(juara)

# 8. Nested List
# Seperti yang telah disinggung sebelumnya, list dapat berisi berbagai tipe data,
# bahkan berisi list di dalam list (nested list), Konsep nested list sendiri mirip dengan
# matriks dalam matematika. Berikut adalah contoh nested list dua dimensi :
# line_up = [
# ["Ferrari", "Leclerc", 16],
# ["Mercedes", "Hamilton", 44],
# ["Red Bull", "Verstappen", 1],
# ["McLaren", "Norris", 4]
# ]
# print(line_up[2][1])

# line_up = [
# ["Ferrari", "Leclerc", 16],
# ["Mercedes", "Hamilton", 44],
# ["Red Bull", "Verstappen", 1],
# ["McLaren", "Norris", 4]
# ]
# for i in line_up:
#     for j in i:
#          print(j)

# TUPLE

chara = ("Yukari", 20, True, 150.4, ["Odette", 25], ("Yukino", 22))
# print(chara)
# print(chara[2])
# print(chara[-1])
# print(chara[4][0])
#  Menambah satu elemen dari belakang

# listchara = list(chara)
# listchara.append("Yui ")
# chara = tuple(listchara)
# print(chara)

# Menambah banyak elemen dari belakang

# listchara = list(chara)
# listchara.extend(["Kohaku", "Hikaru"])
# chara = tuple(listchara)
# print(chara)

# Menyisipkan elemen ke dalam tuple

# listchara = list(chara)
# listchara.insert(2, "Senku")
# chara = tuple(listchara)
# print(chara)

# Mengubah elemen pada tuple

# Mengubah elemen menggunakan indeks langsung

# listchara = list(chara)
# listchara[2] = False
# chara = tuple(listchara)
# print(chara)

# Mengubah elemen menggunakan metode slicing4

listchara = list(chara)
listchara[0:2] = ["Senku", 17]
chara = tuple(listchara)
print(chara)