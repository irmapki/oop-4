class Kendaraan:
    merk = ""
    tipe = ""

    def deskripsi(self):
        print("Ini adalah sebuah kendaraan.")

class Mobil(Kendaraan):
    def deskripsi(self):  # Override method
        print("Ini adalah sebuah mobil.")

    def display(self):
        print("Merek mobil ini adalah:", self.merk)

    def jenis(self):
        print("Tipe mobil ini adalah:", self.tipe)

    def fitur(self, *fitur_tambahan):  # Overloaded method
        fitur_utama = "Mobil ini memiliki AC, audio system, dan sensor parkir."
        if fitur_tambahan:
            fitur_utama += " Fitur tambahan: " + ", ".join(fitur_tambahan) + "."
        print(fitur_utama)

class Motor(Kendaraan):
    def deskripsi(self):  # Override method
        print("Ini adalah sebuah motor.")

    def display(self):
        print("Merek motor ini adalah:", self.merk)

    def jenis(self):
        print("Tipe motor ini adalah:", self.tipe)

    def fitur(self, *fitur_tambahan):  # Overloaded method
        fitur_utama = "Motor ini memiliki mesin injeksi dan rem cakram."
        if fitur_tambahan:
            fitur_utama += " Fitur tambahan: " + ", ".join(fitur_tambahan) + "."
        print(fitur_utama)

# Membuat objek dari subclass Mobil
mobil_toyota = Mobil()
mobil_toyota.merk = "Toyota"
mobil_toyota.tipe = "SUV"
mobil_toyota.deskripsi()
mobil_toyota.display()
mobil_toyota.jenis()
mobil_toyota.fitur("Sunroof", "Kamera belakang")  # Memanggil fitur dengan tambahan argumen

# Membuat objek dari subclass Motor
motor_honda = Motor()
motor_honda.merk = "Honda"
motor_honda.tipe = "Sport"
motor_honda.deskripsi()
motor_honda.display()
motor_honda.jenis()
motor_honda.fitur("ABS", "Pengisi daya USB")  # Memanggil fitur dengan tambahan argumen
