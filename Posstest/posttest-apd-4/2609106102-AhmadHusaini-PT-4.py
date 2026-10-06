username_benar = "husain"
pin_benar = "102"
percobaan = 3

while percobaan > 0:
    print("=== LOGIN ===")
    username = input("Username: ")
    pin = input("Password: ")

    if username == username_benar and pin == pin_benar:
        print("Login Berhasil")
        break
    else:   
        percobaan -= 1
        print("Login Gagal. Sisa percobaan:", percobaan)

if percobaan == 0:
    print("Login gagal!")
    exit()

uang = int(input("Masukkan uang saku: "))
total = 0

while True:
    print("\n=== MENU ===")
    print("[1] Catat Pengeluaran")
    print("[2] Cek Sisa Uang")
    print("[3] Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        pengeluaran = int(input("Masukkan pengeluaran: "))

        if pengeluaran <= uang:
            uang = uang - pengeluaran
            total = total + pengeluaran
            print("Sisa uang: Rp", uang)
        else:
            print("Uang tidak cukup!")

    elif pilihan == "2":
        print("Sisa uang: Rp", uang)
        print("Total pengeluaran: Rp", total)

    elif pilihan == "3":
        print("Terima kasih boskuh")
        break

    else:
        print("Menu tidak tersedia")