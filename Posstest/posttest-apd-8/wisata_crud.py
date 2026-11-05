from data import wisata, ambil_id_baru
from utils import hitung_rekursif
from validasi import validasi_data, validasi_id
from tampilan import tampilkan_wisata


def jumlah_wisata():
    return hitung_rekursif(list(wisata.keys()))


def input_data_wisata(prefix=""):
    nama_w = input(f"Nama {prefix}wisata: ".replace("  ", " "))
    tempat = input(f"Lokasi {prefix}: ".replace(" :", ":"))
    tiket = input(f"Harga {prefix}: ".replace(" :", ":"))
    harga = validasi_data(nama_w, tempat, tiket)
    return nama_w.strip(), tempat.strip(), harga


def lihat_wisata():
    if jumlah_wisata() == 0:
        print("Belum ada data wisata.")
    else:
        tampilkan_wisata()


def tambah_wisata():
    nama_w, tempat, harga = input_data_wisata()
    wisata[ambil_id_baru()] = {"nama": nama_w, "lokasi": tempat, "harga": harga}
    print("Data ditambahkan!")


def ubah_wisata():
    if jumlah_wisata() == 0:
        print("Belum ada data wisata.")
        return

    tampilkan_wisata()
    nomor = validasi_id(input("ID wisata: "))
    nama_w, tempat, harga = input_data_wisata("baru ")
    wisata[nomor] = {"nama": nama_w, "lokasi": tempat, "harga": harga}
    print("Data diubah!")


def hapus_wisata():
    if jumlah_wisata() == 0:
        print("Belum ada data wisata.")
        return

    tampilkan_wisata()
    nomor = validasi_id(input("ID wisata: "))
    del wisata[nomor]
    print("Data dihapus!")
