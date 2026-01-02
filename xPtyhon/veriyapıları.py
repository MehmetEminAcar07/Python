
#liste
"""
isimler = ["Mehmet", "Emin", "Acar", 65, 6, True]
print(isimler)
isimler[1] = "emin"
print(isimler)
"""


#demetler(tuple)
"""
isimler = ("Mehmet", "Emin", "Acar", 65, 6, True)
isimler2 = "Mehmet", "Emin", "Acar", 100, 7, False
print(isimler, isimler2)
"""

#sözlük(dictionary)
"""
sayilar = {10:"on", 20:"yirmi", 100:"yüz", 1000:"bin"}
print(sayilar)
"""

#kümeler(set)

asalSayilar = {2, 3, 5, 7, 11}
tekSayilar = {1, 3, 5, 7, 9}
tekSayilar.add(11)

kesisim = asalSayilar.intersection(tekSayilar)
print(kesisim)
asalSayilar & tekSayilar

birlesim = asalSayilar.union(tekSayilar)
print(birlesim)
asalSayilar | tekSayilar

fark = asalSayilar.difference(tekSayilar)
print(fark)
asalSayilar - tekSayilar
