def hitung_rekursif(daftar):
    if len(daftar) == 0:
        return 0
    return 1 + hitung_rekursif(daftar[1:])
