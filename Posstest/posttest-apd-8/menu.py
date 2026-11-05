from tampilan import bersihkan_layar, tampilkan_menu
from wisata_crud import lihat_wisata, tambah_wisata, ubah_wisata, hapus_wisata


def menu_wisata(role_saat_ini):
    if role_saat_ini == "admin":
        daftar = [("1", "Lihat wisata"), ("2", "Tambah wisata"),
                  ("3", "Ubah wisata"), ("4", "Hapus wisata"), ("5", "Logout")]
        aksi = {"1": lihat_wisata, "2": tambah_wisata,
                "3": ubah_wisata, "4": hapus_wisata}
        kode_logout = "5"
    else:
        daftar = [("1", "Lihat wisata"), ("2", "Logout")]
        aksi = {"1": lihat_wisata}
        kode_logout = "2"

    while True:
        bersihkan_layar()
        tampilkan_menu("MENU WISATA", daftar)
        pilihan = input("Pilih: ").strip()

        if pilihan == kode_logout:
            break

        try:
            if pilihan in aksi:
                aksi[pilihan]()
            else:
                print("Pilihan tidak valid!")
        except ValueError as e:
            print(e)
        finally:
            input("Enter untuk lanjut")
