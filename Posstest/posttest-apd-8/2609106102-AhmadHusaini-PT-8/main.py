from tampilan import bersihkan_layar, tampilkan_menu, tampilkan_banner, animasi_loading
from auth import login, register
from menu import menu_wisata


def main():
    daftar = [("1", "Login"), ("2", "Register"), ("3", "Keluar")]

    while True:
        bersihkan_layar()
        tampilkan_banner("PARIWISATA")
        tampilkan_menu("MENU UTAMA", daftar)
        pilih = input("Pilih: ").strip()

        if pilih == "1":
            try:
                role = login()
            except ValueError as e:
                print(e)
                input("Enter untuk lanjut")
            else:
                print("Login berhasil!")
                animasi_loading("Memuat menu")
                menu_wisata(role)
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


if __name__ == "__main__":
    main()
