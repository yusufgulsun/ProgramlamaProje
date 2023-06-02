class Insan: # insan sınıfı oluşturuldu
    def __init__(self, tc, ad, soyad, yas, cinsiyet, uyruk): # insan sınıfının özellikleri belirlendi
        self.__tc = tc # tc numarası özelliği
        self.__ad = ad # ad özelliği
        self.__soyad = soyad # soyad özelliği
        self.__yas = yas # yaş özelliği
        self.__cinsiyet = cinsiyet # cinsiyet özelliği
        self.__uyruk = uyruk # uyruk özelliği

    def tc_al(self): # tc numarası almak için
        return self.__tc

    def tc_yap(self, tc_no): # tc numarası değiştirmek için
        self.__tc = tc_no

    def ad_al(self): # ad almak için
        return self.__ad

    def ad_yap(self, ad): # ad değiştirmek için
        self.__ad = ad

    def soyad_al(self): # soyad almak için
        return self.__soyad

    def soyad_yap(self, soyad): # soyad değiştirmek için
        self.__soyad = soyad

    def yas_al(self): # yaş almak için
        return self.__yas

    def yas_yap(self, yas): # yaş değiştirmek için
        self.__yas = yas

    def cinsiyet_al(self): # cinsiyet almak için
        return self.__cinsiyet

    def cinsiyet_yap(self, cinsiyet): # cinsiyet değiştirmek için
        self.__cinsiyet = cinsiyet

    def uyruk_al(self): # uyruk almak için
        return self.__uyruk

    def uyruk_yap(self, uyruk): # uyruk değiştirmek için
        self.__uyruk = uyruk

    def __str__(self): # insan sınıfının özelliklerini yazdırmak için
        return f"tc: {self.__tc}\nad: {self.__ad}\nsoyad: {self.__soyad}\nyas: {self.__yas}\ncinsiyet: {self.__cinsiyet}\nuyruk: {self.__uyruk}"