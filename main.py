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
        # Çalışanların bilgilerini bir sözlükte topluyoruz.
        bilgiler = {"nesne": ["calisan", "calisan", "calisan", "maviyaka", "maviyaka", "maviyaka", "beyazyaka", "beyazyaka", "beyazyaka"],
                    "tc_no": [calisan1.tc_al(), calisan2.tc_al(), calisan3.tc_al(), maviyaka1.tc_al(), maviyaka2.tc_al(), maviyaka3.tc_al(), beyazyaka1.tc_al(), beyazyaka2.tc_al(), beyazyaka3.tc_al()],
                    "ad": [calisan1.ad_al(), calisan2.ad_al(), calisan3.ad_al(), maviyaka1.ad_al(), maviyaka2.ad_al(), maviyaka3.ad_al(), beyazyaka1.ad_al(), beyazyaka2.ad_al(), beyazyaka3.ad_al()],
                    "soyad": [calisan1.soyad_al(), calisan2.soyad_al(), calisan3.soyad_al(), maviyaka1.soyad_al(), maviyaka2.soyad_al(), maviyaka3.soyad_al(), beyazyaka1.soyad_al(), beyazyaka2.soyad_al(), beyazyaka3.soyad_al()],
                    "yas": [calisan1.yas_al(), calisan2.yas_al(), calisan3.yas_al(), maviyaka1.yas_al(), maviyaka2.yas_al(), maviyaka3.yas_al(), beyazyaka1.yas_al(), beyazyaka2.yas_al(), beyazyaka3.yas_al()],
                    "cinsiyet": [calisan1.cinsiyet_al(), calisan2.cinsiyet_al(), calisan3.cinsiyet_al(), maviyaka1.cinsiyet_al(), maviyaka2.cinsiyet_al(), maviyaka3.cinsiyet_al(), beyazyaka1.cinsiyet_al(), beyazyaka2.cinsiyet_al(), beyazyaka3.cinsiyet_al()],
                    "uyruk": [calisan1.uyruk_al(), calisan2.uyruk_al(), calisan3.uyruk_al(), maviyaka1.uyruk_al(), maviyaka2.uyruk_al(), maviyaka3.uyruk_al(), beyazyaka1.uyruk_al(), beyazyaka2.uyruk_al(), beyazyaka3.uyruk_al()],
                    "sektor": [calisan1.sektor_al(), calisan2.sektor_al(), calisan3.sektor_al(), maviyaka1.sektor_al(), maviyaka2.sektor_al(), maviyaka3.sektor_al(), beyazyaka1.sektor_al(), beyazyaka2.sektor_al(), beyazyaka3.sektor_al()],
                    "tecrube": [calisan1.tecrube_al(), calisan2.tecrube_al(), calisan3.tecrube_al(), maviyaka1.tecrube_al(), maviyaka2.tecrube_al(), maviyaka3.tecrube_al(), beyazyaka1.tecrube_al(), beyazyaka2.tecrube_al(), beyazyaka3.tecrube_al()],
                    "maas": [calisan1.maas_al(), calisan2.maas_al(), calisan3.maas_al(), maviyaka1.maas_al(), maviyaka2.maas_al(), maviyaka3.maas_al(), beyazyaka1.maas_al(), beyazyaka2.maas_al(), beyazyaka3.maas_al()],
                    "yipranma_payi": [0, 0, 0, maviyaka1.yipranma_payi_al(), maviyaka2.yipranma_payi_al(), maviyaka3.yipranma_payi_al(), 0, 0, 0],
                    "tesvik_primi": [0, 0, 0, 0, 0, 0, beyazyaka1.tesvik_primi_al(), beyazyaka2.tesvik_primi_al(), beyazyaka3.tesvik_primi_al()],
                    "yeni_maas": [calisan1.maas_al() + calisan1.maas_al()*calisan1.zam_hakki(), calisan2.maas_al() + calisan2.maas_al()*calisan2.zam_hakki(), calisan3.maas_al() + calisan3.maas_al()*calisan3.zam_hakki(), maviyaka1.maas_al() + maviyaka1.maas_al()*maviyaka1.zam_hakki(), maviyaka2.maas_al() + maviyaka2.maas_al()*maviyaka2.zam_hakki(), maviyaka3.maas_al() + maviyaka3.maas_al()*maviyaka3.zam_hakki(), beyazyaka1.maas_al() + beyazyaka1.zam_hakki(), beyazyaka2.maas_al() + beyazyaka2.zam_hakki(), beyazyaka3.maas_al() + beyazyaka3.zam_hakki()]}
    except Exception as e:
        print("Hata: ", e)

if __name__ == "__main__":
    main()
input()