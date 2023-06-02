import calisan as cal

class MaviYaka(cal.Calisan): # calisan sınıfından miras alındı
    def __init__(self, tc, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, yipranma_payi): # calisan sınıfının özellikleri belirlendi
        super().__init__(tc, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas) # calisan sınıfının özellikleri alındı
        self.__yipranma_payi = yipranma_payi # yıpranma payı özelliği
        
    def yipranma_payi_al(self): # yıpranma payı almak için
        return self.__yipranma_payi
    
    def yipranma_payi_yap(self, yipranma_payi): # yıpranma payı değiştirmek için
        self.__yipranma_payi = yipranma_payi
        
    def zam_hakki(self): # zam hakkı hesaplamak için
        if self.tecrube_al() < 24: # tecrübe 24'ten küçükse
            return self.__yipranma_payi * 10 # yıpranma payının 10 katını döndür
        elif self.tecrube_al() >= 24 and self.tecrube_al() <= 48 and self.maas_al() < 15000: # tecrübe 24 ile 48 arasındaysa ve maaş 15000'den küçükse
            return ((self.maas_al()%self.tecrube_al())/2 + self.__yipranma_payi * 10)/100 # maaşın tecrübe ile çarpımını döndür
        elif self.tecrube_al() > 48 and self.maas_al() < 25000:
            return ((self.maas_al()%self.tecrube_al())/3 + self.__yipranma_payi * 10)/100
        else:
            return 0
        
    def __str__(self): # string döndürmek için
        return f"ad: {self.ad_al()}\nsoyad: {self.soyad_al()}\ntecribe: {self.tecrube_al()}\nyeni maas: {self.maas_al() + self.maas_al() * self.zam_hakki()}"