import os

akun = {
    "admin": {"password": "102", "role": "admin"}
}

wisata = {
    1: {"nama": "Pantai Melawai", "lokasi": "Balikpapan", "harga": 10000},
    2: {"nama": "Kebun Raya", "lokasi": "Balikpapan", "harga": 15000},
}
id_berikutnya = 3


def hitung_rekursif(daftar):
    if len(daftar) == 0:
        return 0
    return 1 + hitung_rekursif(daftar[1:])


def validasi_data(nama_w, tempat, tiket):
    if nama_w == "" or tempat == "":
        raise ValueError("Nama dan lokasi tidak boleh kosong!")
    if not tiket.isdigit():
        raise ValueError("Harga harus berupa angka!")
    return int(tiket)


def validasi_id(teks):
    if not teks.isdigit() or int(teks) not in wisata:
        raise ValueError("ID tidak valid!")
    return int(teks)


def jumlah_wisata():
    return hitung_rekursif(list(wisata.keys()))


def input_data_wisata():
    nama_w = input("Nama wisata: ")
    tempat = input("Lokasi: ")
    tiket = input("Harga: ")
    harga = validasi_data(nama_w, tempat, tiket)
    return nama_w, tempat, harga


def bersihkan_layar():
    os.system("cls" if os.name == "nt" else "clear")


def tampilkan_wisata():
    print(f"{'ID':<4}{'Nama':<20}{'Lokasi':<15}{'Harga':>10}")
    print("-" * 49)
    for id_w, data in wisata.items():
        print(f"{id_w:<4}{data['nama']:<20}{data['lokasi']:<15}{data['harga']:>10}")


def register():
    nama = input("Username: ")
    sandi = input("Password: ")

    if nama == "" or sandi == "":
        raise ValueError("Username dan password tidak boleh kosong!")
    if nama in akun:
        raise ValueError("Username sudah digunakan!")

    akun[nama] = {"password": sandi, "role": "pengguna"}
    print("Register berhasil!")


def tambah_wisata():
    global id_berikutnya
    nama_w, tempat, harga = input_data_wisata()
    wisata[id_berikutnya] = {
        "nama": nama_w,
        "lokasi": tempat,
        "harga": harga
    }
    id_berikutnya += 1
    print("Data ditambahkan!")


def ubah_wisata():
    if jumlah_wisata() == 0:
        print("Belum ada data wisata.")
        return

    tampilkan_wisata()
    nomor = validasi_id(input("ID wisata: "))

    nama_baru = input("Nama baru: ")
    lokasi_baru = input("Lokasi baru: ")
    harga_baru = input("Harga baru: ")
    harga = validasi_data(nama_baru, lokasi_baru, harga_baru)

    wisata[nomor] = {
        "nama": nama_baru,
        "lokasi": lokasi_baru,
        "harga": harga
    }
    print("Data diubah!")


def hapus_wisata():
    if jumlah_wisata() == 0:
        print("Belum ada data wisata.")
        return

    tampilkan_wisata()
    nomor = validasi_id(input("ID wisata: "))
    del wisata[nomor]
    print("Data dihapus!")


def menu_wisata(role_saat_ini):
    while True:
        bersihkan_layar()
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

        try:
            if menu == "1":
                if jumlah_wisata() == 0:
                    print("Belum ada data wisata.")
                else:
                    tampilkan_wisata()
            elif menu == "2":
                tambah_wisata()
            elif menu == "3":
                ubah_wisata()
            elif menu == "4":
                hapus_wisata()
            else:
                print("Pilihan tidak valid!")
        except ValueError as e:
            print(e)
        finally:
            input("Enter untuk lanjut")


def login():
    nama = input("Username: ")
    sandi = input("Password: ")

    try:
        if nama not in akun or akun[nama]["password"] != sandi:
            raise ValueError("Login gagal!")
    except ValueError as e:
        print(e)
        input("Enter untuk lanjut")
    else:
        role_saat_ini = akun[nama]["role"]
        print("Login berhasil!")
        input("Enter untuk lanjut")
        menu_wisata(role_saat_ini)


while True:
    bersihkan_layar()
    print("=== PARIWISATA ===")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    pilih = input("Pilih: ")

    if pilih == "1":
        login()
    elif pilih == "2":
        try:
            register()
        except ValueError as e:
            print(e)
        finally:
            input("Enter untuk lanjut")
    elif pilih == "3":
        break
    else:
        print("Pilihan tidak valid!")
        input("Enter untuk lanjut")