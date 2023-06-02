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
    def __str__(self): # insan sınıfının özelliklerini yazdırmak için
        return f"tc: {self.tc_al()}\nad: {self.ad_al()}\nsoyad: {self.soyad_al()}\nstatusu: {self.statu_bul()}"