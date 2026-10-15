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
        sandi = input("Password: ")

        if nama == "" or sandi == "":
            print("Username dan password tidak boleh kosong!")
        elif nama in akun:
            print("Username sudah digunakan!")
        else:
            akun.append(nama)
            password.append(sandi)
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

                if menu == "5":
                    break

                elif menu == "1":
                    if len(wisata) == 0:
                        print("Belum ada data wisata.")
                    else:
                        print(f"{'No':<4}{'Nama':<20}{'Lokasi':<15}{'Harga':>10}")
                        print("-" * 49)
                        for i in range(len(wisata)):
                            print(f"{i + 1:<4}{wisata[i]:<20}{lokasi[i]:<15}{harga[i]:>10}")

                elif menu == "2":
                    if role[i_akun] == "admin":
                        nama_w = input("Nama wisata: ")
                        tempat = input("Lokasi: ")
                        tiket = input("Harga: ")

                        if nama_w == "" or tempat == "":
                            print("Nama dan lokasi tidak boleh kosong!")
                        elif not tiket.isdigit():
                            print("Harga harus berupa angka!")
                        else:
                            wisata.append(nama_w)
                            lokasi.append(tempat)
                            harga.append(int(tiket))
                            print("Data ditambahkan!")
                    else:
                        print("Khusus admin!")

                elif menu == "3":
                    if role[i_akun] == "admin":
                        for i in range(len(wisata)):
                            print(i + 1, wisata[i], lokasi[i], harga[i])

                        nomor = input("Nomor wisata: ")

                        if nomor.isdigit() and 1 <= int(nomor) <= len(wisata):
                            nomor = int(nomor) - 1
                            nama_baru = input("Nama baru: ")
                            lokasi_baru = input("Lokasi baru: ")
                            harga_baru = input("Harga baru: ")

                            if nama_baru == "" or lokasi_baru == "":
                                print("Nama dan lokasi tidak boleh kosong!")
                            elif not harga_baru.isdigit():
                                print("Harga harus berupa angka!")
                            else:
                                wisata[nomor] = nama_baru
                                lokasi[nomor] = lokasi_baru
                                harga[nomor] = int(harga_baru)
                                print("Data diubah!")
                        else:
                            print("Nomor tidak valid!")
                    else:
                        print("Khusus admin!")

                elif menu == "4":
                    if role[i_akun] == "admin":
                        for i in range(len(wisata)):
                            print(i + 1, wisata[i], lokasi[i], harga[i])

                        nomor = input("Nomor wisata: ")

                        if nomor.isdigit() and 1 <= int(nomor) <= len(wisata):
                            nomor = int(nomor) - 1
                            wisata.pop(nomor)
                            lokasi.pop(nomor)
                            harga.pop(nomor)
                            print("Data dihapus!")
                        else:
                            print("Nomor tidak valid!")
                    else:
                        print("Khusus admin!")

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