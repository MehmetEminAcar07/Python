"""class bitki:
    tur = "cicekli"
    def __init__(self,bitkiAd):
        self.bitkiAd = bitkiAd
        
    def bitkiAdi(self):
        print("Bitki Türü = ", self.tur, " , Adı= ",self.bitkiAd)
        
pp_bonsai = bitki("Bonsai")
pp_bonsai.bitkiAd
pp_bonsai.tur
pp_bonsai.bitkiAdi()"""

class hayvanPasaportu(object):
    def __init__(self, ad, tur, irk, cinsiyet, dogumTarihi, renk):
        self.ad = ad
        self.tur = tur
        self.irk = irk
        self.cinsiyet = cinsiyet
        self.dogumTarihi = dogumTarihi
        self.renk = renk
        
    def kisaBilgi(self):
        print("Hayvan Türü = ", self.tur, ", Adı =",self.ad)
        
    def detayBilgi(self):
        print("DETAYLAR: ")
        print(self.ad)
        print(self.tur)
        print(self.irk)
        print(self.cinsiyet)
        print(self.dogumTarihi)
        print(self.renk)
        
        
#child class
class evcilHayvanPasaportu(hayvanPasaportu):
    def __init__(self, ad, tur, irk, cinisyet, dogumTarihi, renk, cipNo, sahipAd, sahipSoyad):
        self.cipNo = cipNo
        self.sahipAd = sahipAd
        self.sahipSoyad = sahipSoyad
        
        hayvanPasaportu.__init__(self, ad, tur, irk, cinisyet, dogumTarihi, renk)
        
    def kisaBilgi(self):
        print("Çip no = ", self.cipNo, "Hayvan Türü = ", self.tur, " , Adı = ", self.ad)
        
    def sahip(self):
        print("SAHİBİ = ", self.sahipAd, self.sahipSoyad)
        
        
bistan_pp = evcilHayvanPasaportu("Bistan", "Kedi", "Tekir", "Dişi", "12.01.1992", "Boz", "65", "Mehmet emin", "Acar")
bistan_pp.kisaBilgi()
bistan_pp.detayBilgi()
bistan_pp.sahip()