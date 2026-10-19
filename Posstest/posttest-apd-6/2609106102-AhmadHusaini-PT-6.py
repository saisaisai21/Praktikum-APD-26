import os

akun = {
    "admin": {"password": "102", "role": "admin"}
}

wisata = {
    1: {"nama": "Pantai Melawai", "lokasi": "Balikpapan", "harga": 10000},
    2: {"nama": "Kebun Raya", "lokasi": "Balikpapan", "harga": 15000},
}
id_berikutnya = 3


def tampilkan_wisata():
    print(f"{'ID':<4}{'Nama':<20}{'Lokasi':<15}{'Harga':>10}")
    print("-" * 49)
    for id_w, data in wisata.items():
        print(f"{id_w:<4}{data['nama']:<20}{data['lokasi']:<15}{data['harga']:>10}")


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
            akun[nama] = {"password": sandi, "role": "pengguna"}
            print("Register berhasil!")

        input("Enter untuk lanjut")

    elif pilih == "1":
        nama = input("Username: ")
        sandi = input("Password: ")

        if nama in akun and akun[nama]["password"] == sandi:
            role_saat_ini = akun[nama]["role"]
            print("Login berhasil!")
            input("Enter untuk lanjut")

            while True:
                os.system("cls" if os.name == "nt" else "clear")
                print("=== MENU WISATA ===")
                print("1. Lihat wisata")
                if role_saat_ini == "admin":
                    print("2. Tambah wisata")
                    print("3. Ubah wisata")
                    print("4. Hapus wisata")
                    print("5. Logout")
                else:
                    print("2. Logout")
                menu = input("Pilih: ")

                if role_saat_ini != "admin":
                    if menu == "2":
                        menu = "5"
                    elif menu != "1":
                        menu = ""

                if menu == "5":
                    break

                elif menu == "1":
                    if len(wisata) == 0:
                        print("Belum ada data wisata.")
                    else:
                        tampilkan_wisata()

                elif menu == "2":
                    if role_saat_ini == "admin":
                        nama_w = input("Nama wisata: ")
                        tempat = input("Lokasi: ")
                        tiket = input("Harga: ")

                        if nama_w == "" or tempat == "":
                            print("Nama dan lokasi tidak boleh kosong!")
                        elif not tiket.isdigit():
                            print("Harga harus berupa angka!")
                        else:
                            wisata[id_berikutnya] = {
                                "nama": nama_w,
                                "lokasi": tempat,
                                "harga": int(tiket),
                            }
                            id_berikutnya += 1
                            print("Data ditambahkan!")
                    else:
                        print("Khusus admin!")

                elif menu == "3":
                    if role_saat_ini == "admin":
                        if len(wisata) == 0:
                            print("Belum ada data wisata.")
                        else:
                            tampilkan_wisata()
                            nomor = input("ID wisata: ")

                            if nomor.isdigit() and int(nomor) in wisata:
                                nomor = int(nomor)
                                nama_baru = input("Nama baru: ")
                                lokasi_baru = input("Lokasi baru: ")
                                harga_baru = input("Harga baru: ")

                                if nama_baru == "" or lokasi_baru == "":
                                    print("Nama dan lokasi tidak boleh kosong!")
                                elif not harga_baru.isdigit():
                                    print("Harga harus berupa angka!")
                                else:
                                    wisata[nomor] = {
                                        "nama": nama_baru,
                                        "lokasi": lokasi_baru,
                                        "harga": int(harga_baru),
                                    }
                                    print("Data diubah!")
                            else:
                                print("ID tidak valid!")
                    else:
                        print("Khusus admin!")

                elif menu == "4":
                    if role_saat_ini == "admin":
                        if len(wisata) == 0:
                            print("Belum ada data wisata.")
                        else:
                            tampilkan_wisata()
                            nomor = input("ID wisata: ")

                            if nomor.isdigit() and int(nomor) in wisata:
                                del wisata[int(nomor)]
                                print("Data dihapus!")
                            else:
                                print("ID tidak valid!")
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
        input("Enter untuk lanjuut")