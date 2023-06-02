import calisan as cal

class BeyazYaka(cal.Calisan): # calisan sınıfından miras alındı
    def __init__(self, tc, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, tesvik_primi): # calisan sınıfının özellikleri belirlendi
        super().__init__(tc, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas) # calisan sınıfının özellikleri alındı
        self.__tesvik_primi = tesvik_primi # teşvik primi özelliği

    def tesvik_primi_al(self): # teşvik primi almak için
        return self.__tesvik_primi
    
    def tesvik_primi_yap(self, tesvik_primi): # teşvik primi değiştirmek için
        self.__tesvik_primi = tesvik_primi

    def zam_hakki(self): # zam hakkı hesaplamak için
        if self.tecrube_al() < 24: # tecrübe 24'ten küçükse
            return self.__tesvik_primi # teşvik primini döndür
        elif self.tecrube_al() >= 24 and self.tecrube_al() <= 48 and self.maas_al() < 15000: # tecrübe 24 ile 48 arasındaysa ve maaş 15000'den küçükse
            return (self.maas_al()%self.tecrube_al())*5 + self.__tesvik_primi # maaşın tecrübe ile çarpımını döndür
        elif self.tecrube_al() > 48 and self.maas_al() < 25000:
            return (self.maas_al()%self.tecrube_al())*4 + self.__tesvik_primi
        else:
            return 0
        
    def __str__(self): # yazdırmak için
        return f"ad: {self.ad_al()}\nsoyad: {self.soyad_al()}\ntecrübe: {self.tecrube_al()}\nyeni maaş: {self.zam_hakki() + self.maas_al()}"