#overriding

class Kendaraan:
    # atribut dan metode kelas induk
    merek = "test"

    def nyalakan_mesin(self):
        print("Mesin menyala")

# Pewarisan dari kelas Kendaraan
class Mobil(Kendaraan):
    # Override metode nyalakan_mesin
    def nyalakan_mesin(self):
        # super().nyalakan_mesin()  # Memanggil metode dari kelas induk
        print("Mesin mobil menyala dengan suara yang halus")

    # Metode untuk menampilkan merek
    # def tampilkan_info(self):
    #     print("Mobil ini adalah:", self.merek)

# Buat objek dari kelas Mobil
mobil_saya = Mobil()

# Akses atribut dari kelas induk
mobil_saya.merek = "Toyota"
mobil_saya.nyalakan_mesin()  # Panggil metode yang di-overide
# mobil_saya.tampilkan_info()  # Menampilkan informasi merek