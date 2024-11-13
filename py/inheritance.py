#inheritance

class Kendaraan:
    # atribut dan metode kelas induk
    merek = ""

    def nyalakan_mesin(self):
        print("Mesin menyala")

# pewarisan dari kelas Kendaraan
class Mobil(Kendaraan):
    #metode baru dalam kelas turunan
    def tampilkan_info(self):
        # akses atribut merek dari kelas induk menggunakan self
        print("Mobil ini adalah", self.merek)

# buat objek dari kelas turunan
mobil_saya = Mobil()

# akses atribut dan metode dari kelas induk
mobil_saya.merek = "Toyota"
mobil_saya.nyalakan_mesin()

# panggil metode kelas turunan
mobil_saya.tampilkan_info()
