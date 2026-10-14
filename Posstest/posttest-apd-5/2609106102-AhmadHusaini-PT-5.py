import os

akun = ["admin"]
password = ["102"]
role = ["admin"]

wisata = ["Pantai Melawai", "Kebun Raya"]
lokasi = ["Balikpapan", "Balikpapan"]
harga = [10000, 15000]

while True:
    os.system("cls" if os.name == "nt" else "clear")
    print("=== PARIWISATA ===")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    pilih = input("Pilih: ")

    if pilih == "2":
        nama = input("Username: ")

        if nama in akun:
            print("Username sudah digunakan!")
        else:
            akun.append(nama)
            password.append(input("Password: "))
            role.append("pengguna")
            print("Register berhasil!")

        input("Enter untuk lanjut")

    elif pilih == "1":
        nama = input("Username: ")
        sandi = input("Password: ")

        if nama in akun and password[akun.index(nama)] == sandi:
            i_akun = akun.index(nama)
            print("Login berhasil!")
            input("Enter untuk lanjut")

            while True:
                os.system("cls" if os.name == "nt" else "clear")
                print("=== MENU WISATA ===")
                print("1. Lihat wisata")
                print("2. Tambah wisata")
                print("3. Ubah wisata")
                print("4. Hapus wisata")
                print("5. Logout")
                menu = input("Pilih: ")

                if menu == "1":
                    for i, nama_w in enumerate(wisata):
                        print(i + 1, nama_w, lokasi[i], harga[i])

                elif menu == "2":
                    if role[i_akun] == "admin":
                        nama_w = input("Nama wisata: ")
                        tempat = input("Lokasi: ")
                        tiket = int(input("Harga: "))

                        wisata.append(nama_w)
                        lokasi.append(tempat)
                        harga.append(tiket)
                        print("Data ditambahkan!")
                    else:
                        print("Khusus admin!")

                elif menu == "3":
                    if role[i_akun] == "admin":
                        nomor = int(input("Nomor wisata: ")) - 1

                        if nomor in range(len(wisata)):
                            wisata[nomor] = input("Nama baru: ")
                            lokasi[nomor] = input("Lokasi baru: ")
                            harga[nomor] = int(input("Harga baru: "))
                            print("Data diubah!")
                        else:
                            print("Nomor tidak valid!")
                    else:
                        print("Khusus admin!")

                elif menu == "4":
                    if role[i_akun] == "admin":
                        nomor = int(input("Nomor wisata: ")) - 1

                        if nomor in range(len(wisata)):
                            wisata.pop(nomor)
                            lokasi.pop(nomor)
                            harga.pop(nomor)
                            print("Data dihapus!")
                        else:
                            print("Nomor tidak valid!")
                    else:
                        print("Khusus admin!")

                elif menu == "5":
                    break

                else:
                    print("Pilihan tidak valid!")

                input("Enter untuk lanjut")

        else:
            print("Login gagal!")
            input("Enter untuk lanjut")

    elif pilih == "3":
        break

    else:
        print("Pilihan tidak valid!")
        input("Enter untuk lanjut")