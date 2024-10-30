class PersegiPanjang1:
    def __init__(self, lebar, panjang):
        self.panjang= panjang
        self.lebar=lebar

    def keliling(self):
        return 2 * (self.panjang + self.lebar)
    
    def luas(self):
        return self.panjang * self.lebar

    def __str__(self):
        return f"Persegi Panjang dengan panjang {self.panjang} cm dan lebar {self.lebar} cm"
    
pp = PersegiPanjang1(3, 2)
print(pp)               # Output: Persegi panjang, panjang 3 cm, dan lebar 2 cm
print(pp.keliling())    # Output: 10
print(pp.luas())  

#Fungsi ini __init__()dipanggil secara otomatis setiap kali kelas digunakan untuk membuat objek baru.