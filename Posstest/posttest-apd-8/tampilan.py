import os
import time

import pyfiglet
from prettytable import PrettyTable
from tqdm import tqdm

from data import wisata


def bersihkan_layar():
    os.system("cls" if os.name == "nt" else "clear")


def tampilkan_banner(teks):
    print(pyfiglet.figlet_format(teks, font="standard"))


def animasi_loading(pesan, durasi=0.8):
    langkah = 20
    for _ in tqdm(range(langkah), desc=pesan, bar_format="{desc} |{bar}| {percentage:3.0f}%"):
        time.sleep(durasi / langkah)


def tampilkan_menu(judul, daftar_menu):
    tabel = PrettyTable()
    tabel.title = judul
    tabel.field_names = ["No", "Menu"]
    tabel.align["Menu"] = "l"
    for no, nama in daftar_menu:
        tabel.add_row([no, nama])
    print(tabel)


def tampilkan_wisata():
    tabel = PrettyTable()
    tabel.title = "DAFTAR WISATA"
    tabel.field_names = ["ID", "Nama", "Lokasi", "Harga (Rp)"]
    tabel.align["Nama"] = "l"
    tabel.align["Lokasi"] = "l"
    tabel.align["Harga (Rp)"] = "r"
    for id_w, data in wisata.items():
        tabel.add_row([id_w, data["nama"], data["lokasi"], f"{data['harga']:,}".replace(",", ".")])
    print(tabel)
