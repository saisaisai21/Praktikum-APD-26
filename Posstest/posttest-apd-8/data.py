akun = {
    "admin": {"password": "102", "role": "admin"}
}

wisata = {
    1: {"nama": "Pantai Melawai", "lokasi": "Balikpapan", "harga": 10000},
    2: {"nama": "Kebun Raya", "lokasi": "Balikpapan", "harga": 15000},
}

_counter = {"id_berikutnya": 3}


def ambil_id_baru():
    id_baru = _counter["id_berikutnya"]
    _counter["id_berikutnya"] += 1
    return id_baru
