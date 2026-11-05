from data import wisata


def validasi_data(nama_w, tempat, tiket):
    if nama_w.strip() == "" or tempat.strip() == "":
        raise ValueError("Nama dan lokasi tidak boleh kosong!")
    if not tiket.isdigit():
        raise ValueError("Harga harus berupa angka!")
    return int(tiket)


def validasi_id(teks):
    if not teks.isdigit() or int(teks) not in wisata:
        raise ValueError("ID tidak valid!")
    return int(teks)
