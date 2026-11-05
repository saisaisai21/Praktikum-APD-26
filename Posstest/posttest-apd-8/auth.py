import getpass

import pwinput
from data import akun


def input_password():
    try:
        return pwinput.pwinput("Password: ", mask="*")
    except Exception:
        return getpass.getpass("Password: ")


def register():
    nama = input("Username: ").strip()
    sandi = input_password()

    if nama == "" or sandi == "":
        raise ValueError("Username dan password tidak boleh kosong!")
    if nama in akun:
        raise ValueError("Username sudah digunakan!")

    akun[nama] = {"password": sandi, "role": "pengguna"}
    print("Register berhasil!")


def login():
    nama = input("Username: ").strip()
    sandi = input_password()

    if nama not in akun or akun[nama]["password"] != sandi:
        raise ValueError("Login gagal!")
    return akun[nama]["role"]
