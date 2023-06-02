import insan as ins
class Calisan(ins.Insan): # insan sınıfından miras alındı
    def __init__(self, tc, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas): # insan sınıfının özellikleri belirlendi
        super().__init__(tc, ad, soyad, yas, cinsiyet, uyruk) # insan sınıfının özellikleri alındı
        self.__sektor = sektor # sektor özelliği
        self.__tecrube = tecrube # tecrübe özelliği
        self.__maas = maas # maaş özelliği

    def sektor_al(self): # sektor almak için
        return self.__sektor
    
    def sektor_yap(self, sektor): # sektor değiştirmek için
        self.__sektor = sektor

    def tecrube_al(self): # tecrübe almak için
        return self.__tecrube
    
    def tecrube_yap(self, tecrube): # tecrübe değiştirmek için
        self.__tecrube = tecrube

    def maas_al(self): # maaş almak için
        return self.__maas
    
    def maas_yap(self, maas): # maaş değiştirmek için
        self.__maas = maas

    def zam_hakki(self): # zam hakkı hesaplamak için
        if self.__tecrube < 24: # tecrübe 24'ten küçükse
            return 0 # 0 döndür
        elif self.__tecrube >= 24 and self.__tecrube <= 48 and self.__maas < 15000: # tecrübe 24 ile 48 arasındaysa ve maaş 15000'den küçükse
            return (self.__maas%self.__tecrube) / 100 # maaşın tecrübe ile çarpımını döndür
        elif self.__tecrube > 48 and self.__maas < 25000:
            return (self.__maas%self.__tecrube) / 200
        else:
            return 0
        
    def __str__(self): # string döndürmek için
        return f"ad: {self.ad_al()}\nsoyad: {self.soyad_al()}\ntecrübe: {self.__tecrube}\nyeni maaş: {self.__maas + self.zam_hakki() * self.__maas}"
        
