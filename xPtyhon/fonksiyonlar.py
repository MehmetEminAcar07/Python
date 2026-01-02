"""def toplam_fark(sayi1, sayi2):
        toplam = sayi1+sayi2
        fark = sayi1-sayi2
        return(toplam, fark)
    
sonuc = toplam_fark(3, 5)
sonuc_toplam, sonuc_fark = toplam_fark(3, 5)"""

def ciftSayilariGetir(n):
    sayilar = []
    bas = 0
    while len(sayilar) < n:
        if bas % 2 == 0:
            sayilar.append(bas)
        bas += 1 
    return(sayilar)
    
ciftSayilariGetir(10)
