import insan as ins
class Issiz(ins.Insan): # insan sınıfından miras alındı 
    def __init__(self, tc, ad, soyad, yas, cinsiyet, uyruk, maviyaka, beyazyaka, yonetici): # insan sınıfının özellikleri belirlendi
        super().__init__(tc, ad, soyad, yas, cinsiyet, uyruk) # insan sınıfının özellikleri alındı
        self.__maviyaka = maviyaka # mavi yaka özelliği
        self.__beyazyaka = beyazyaka # beyaz yaka özelliği
        self.__yonetici = yonetici # yönetici özelliği

    def statu_al(self): # statü almak için
        return self.__statu

    def statu_yap(self, statu): # statü değiştirmek için
        self.__statu = statu

    def tecrube_al(self): # tecrübe almak için
        return self.__tecrube

    def tecrube_yap(self, tecrube): # tecrübe değiştirmek için
        self.__tecrube = tecrube

    def statu_bul(self): # statü bulmak için
        try:
            maviyaka_kat = self.__maviyaka * 20 / 100 # mavi yaka katkısı
            beyazyaka_kat = self.__beyazyaka * 35 / 100 # beyaz yaka katkısı
            yonetici_kat = self.__yonetici * 45 / 100 # yönetici katkısı
            liste_kat = [maviyaka_kat, beyazyaka_kat, yonetici_kat] # katkıları listeye ekle
            max_kat = max(liste_kat) # en yüksek katkıyı bul
            if max_kat == yonetici_kat: # en yüksek katkı yönetici katkısı ise
                self.__statu = "Yönetici"
            elif max_kat == beyazyaka_kat: # en yüksek katkı beyaz yaka katkısı ise
                self.__statu = "Beyaz Yaka"
            elif max_kat == maviyaka_kat: # en yüksek katkı mavi yaka katkısı ise
                self.__statu = "Mavi Yaka"
            return self.__statu
        except:
            print("Bulunamadı.")

    def __str__(self): # insan sınıfının özelliklerini yazdırmak için
        return f"tc: {self.tc_al()}\nad: {self.ad_al()}\nsoyad: {self.soyad_al()}\nstatusu: {self.statu_bul()}"