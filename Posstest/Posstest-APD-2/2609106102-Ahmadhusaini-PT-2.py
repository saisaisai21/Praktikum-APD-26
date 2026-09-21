merchandise_1 = 45000
merchandise_2 = 50000
merchandise_3 = 60000
merchandise_4 = 75000
merchandise_5 = 90000
merchandise_6 = 120000

harga_marchandise = [merchandise_1, merchandise_2, merchandise_3, merchandise_4, merchandise_5, merchandise_6]

total_harga = (merchandise_1 + merchandise_2 + merchandise_3 + merchandise_4 + merchandise_5 + merchandise_6)
total_harga = total_harga + 7500

rata_rata = total_harga / len(harga_marchandise)

nim = 100

bolean = nim > rata_rata

kurs_USD = 17805
total_harga_USD = total_harga / kurs_USD

slice_negatif = harga_marchandise[-4:-1]

print ("merchandise_1 :", merchandise_1)
print ("merchandise_2 :", merchandise_2)
print ("merchandise_3 :", merchandise_3)
print ("merchandise_4 :", merchandise_4)
print ("merchandise_5 :", merchandise_5)
print ("merchandise_6 :", merchandise_6)
print ("list_harga_marchandise =", harga_marchandise)
print ("total_harga =", total_harga)
print ("rata_rata =", rata_rata)
print ("nim =", nim)
print ("bolean = ", bolean)
print ("kurs_USD =", kurs_USD)
print ("total_harga_USD =", total_harga_USD)
print ("slice_negatif =", slice_negatif)