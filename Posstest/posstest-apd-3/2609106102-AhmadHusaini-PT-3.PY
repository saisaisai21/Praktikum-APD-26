nama_benar = "husain"
nim_benar = "102"

nama = input("Nama panggilan: ")
nim = input("3 digit terakhir NIM: ")

if nama == nama_benar and nim == nim_benar:
    print("Login berhasil")
    
    print("1. PS4 - 10000")
    print("2. PS4 Pro - 15000")
    print("3. PS5 - 20000")
    pilih = int(input("Pilih konsol: "))

    if pilih == 1:
        konsol = "PS4"
        harga = 10000
    elif pilih == 2:
        konsol = "PS4 Pro"
        harga = 15000
    elif pilih == 3:
        konsol = "PS5"
        harga = 20000
    else:
        print("Pilihan tidak tersedia")
        exit()

    jam = int(input("Jumlah jam sewa: "))
    total = harga * jam

    if jam >= 5:
        diskon = total * 0.08
    elif jam >= 3:
        diskon = total * 0.05
    else:
        diskon = 0

    print("1. Weekday")
    print("2. Weekend")
    waktu = int(input("Pilih waktu: "))

    if waktu == 2:
        weekend = total * 0.10
        waktu = "Weekend"
    elif waktu == 1:
        weekend = 0
        waktu = "Weekday"
    else:
        print("Pilihan tidak tersedia")
        exit()

    bayar = total - diskon + weekend

    print("===== STRUK =====")
    print("Nama          :", nama)
    print("NIM           :", nim)
    print("Konsol        :", konsol)
    print("Jumlah jam    :", jam)
    print("Total harga   : Rp", int(total))
    print("Diskon        : Rp", int(diskon))
    print("Waktu         :", waktu)
    print("Biaya weekend : Rp", int(weekend))
    print("Total bayar   : Rp", int(bayar))

else:
    print("Login gagal")
