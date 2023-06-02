import insan as ins # insan.py dosyasını import ediyoruz. 
import issiz as iss # issiz.py dosyasını import ediyoruz. 
import calisan as cal   # calisan.py dosyasını import ediyoruz.
import maviyaka as mavi # maviyaka.py dosyasını import ediyoruz.
import beyazyaka as beyaz # beyazyaka.py dosyasını import ediyoruz.
import pandas as pd # pandas kütüphanesini import ediyoruz.

def main():
    try:
        # İnsan sınıfından 2 tane nesne oluşturuyoruz.
        insan1 = ins.Insan("12345678910", "Ali", "Veli", 20, "Erkek", "Türk")
        insan2 = ins.Insan("12345678911", "Ayşe", "Fatma", 21, "Kadın", "Türk")
        # Nesnelerin bilgilerini ekrana yazdırıyoruz.
        print(insan1)
        print(insan2)

        # İşsiz sınıfından 3 tane nesne oluşturuyoruz.
        issiz1 = iss.Issiz("12345678912", "Ahmet", "Mehmet", 22, "Erkek", "Türk", 5, 10, 4)
        issiz2 = iss.Issiz("12345678913", "Ayşe", "Fatma", 23, "Kadın", "Türk", 6, 2, 5)
        issiz3 = iss.Issiz("12345678914", "Ali", "Veli", 24, "Erkek", "Türk", 11, 4, 3)
        # Nesnelerin bilgilerini ekrana yazdırıyoruz.
        print(issiz1)
        print(issiz2)
        print(issiz3)

        # Çalışan sınıfından 3 tane nesne oluşturuyoruz.
        calisan1 = cal.Calisan("12345678915", "Ahmet", "Mehmet", 25, "Erkek", "Türk", "Teknoloji", 10, 10000)
        calisan2 = cal.Calisan("12345678916", "Ayşe", "Fatma", 26, "Kadın", "Türk", "Muhasebe", 11, 11000)
        calisan3 = cal.Calisan("12345678917", "Ali", "Veli", 27, "Erkek", "Türk", "İnşaat", 12, 21000)
        # Nesnelerin bilgilerini ekrana yazdırıyoruz.
        print(calisan1)
        print(calisan2)
        print(calisan3)

        # MaviYaka sınıfından 3 tane nesne oluşturuyoruz.
        maviyaka1 = mavi.MaviYaka("12345678918", "Ahmet", "Mehmet", 28, "Erkek", "Türk", "Teknoloji", 13, 10000, 0.1)
        maviyaka2 = mavi.MaviYaka("12345678919", "Ayşe", "Fatma", 29, "Kadın", "Türk", "Muhasebe", 24, 21000, 0.25)
        maviyaka3 = mavi.MaviYaka("12345678920", "Ali", "Veli", 30, "Erkek", "Türk", "İnşaat", 35, 31000, 0.45)
        # Nesnelerin bilgilerini ekrana yazdırıyoruz.
        print(maviyaka1)
        print(maviyaka2)
        print(maviyaka3)

        # BeyazYaka sınıfından 3 tane nesne oluşturuyoruz.
        beyazyaka1 = beyaz.BeyazYaka("12345678921", "Ahmet", "Mehmet", 31, "Erkek", "Türk", "Teknoloji", 14, 10000, 250)
        beyazyaka2 = beyaz.BeyazYaka("12345678922", "Ayşe", "Fatma", 32, "Kadın", "Türk", "Muhasebe", 37, 21000, 1500)
        beyazyaka3 = beyaz.BeyazYaka("12345678923", "Ali", "Veli", 35, "Erkek", "Türk", "İnşaat", 39, 31000, 3000)
        # Nesnelerin bilgilerini ekrana yazdırıyoruz.
        print(beyazyaka1)
        print(beyazyaka2)
        print(beyazyaka3)
    except Exception as e:
        print("Hata: ", e)

if __name__ == "__main__":
    main()
input()