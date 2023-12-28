#Mehmet Seyfullah ÖZEN 20010011055

import math


def arttir(sayi):
    sayi = str(sayi)
    if "." not in sayi:
        sayi = int(sayi) + 1
    else:
        ayir = sayi.split('.')
        uzunluk = len(ayir[1])-1
        eklenecek = float("0."+(uzunluk*"0")+"1")
        sayi = round(float(sayi) + eklenecek, uzunluk + 1)
    return sayi


def azalt(sayi):
    sayi = str(sayi)
    if "." not in sayi:
        sayi = int(sayi) + 1
    else:
        ayir = sayi.split('.')
        uzunluk = len(ayir[1])-1
        eklenecek = float("0."+(uzunluk*"0")+"1")
        sayi = round(float(sayi) - eklenecek, uzunluk + 1)
    return sayi


sayilar = []
sinif_sayisi = 0
with open("in.txt", "r") as dosya:
    for satir in dosya.readlines():
        sayilar.append(float(satir[:-1]))
    sinif_sayisi = sayilar.pop(0)


sayilar.sort()  # sırala
n = len(sayilar)


R = sayilar[-1] - sayilar[0]
c = math.ceil(1.09/sinif_sayisi * 100.0) / 100.0
sinif_genisligi = float(azalt(c))


print("Alt		     Üst          Orta      Frekans     Göreli Frekans")
ilk = sayilar[0]
i = 0
with open("out.txt", "w") as dosya:
    dosya.write("Alt		     Üst          Orta      Frekans     Göreli Frekans\n")

    for _ in range(int(sinif_sayisi)):
        ilk += i
        i = c
        ust = ilk + sinif_genisligi
        orta = (ilk + ust) / 2
        freq = 0
        for sayi in sayilar:
            if round(ilk, 2) <= sayi <= round(ust, 2):
                freq += 1
        dosya.write("{:<12} {:<12} {:<12} {:<12} {:}\n".format(round(ilk, 2), round(ust, 2), round(orta, 2), freq,
                                                           round(freq / n, 2)))

        print("{:<12} {:<12} {:<12} {:<12} {:}".format(round(ilk, 2), round(ust, 2), round(orta, 2), freq, round(freq/n, 2)))


print()
# ---------------------------------------------------------------------------------------------------------------------
print()


# Ortalama Hesaplama
toplam = 0
for i in sayilar:
    toplam += i

ortalama = toplam / n
print("ortalama: {:.5f}".format(ortalama))


with open("out.txt", "a") as dosya:
    dosya.write("\n\nortalama: {:.5f}\n".format(ortalama))


# Mod Hesaplama
largestCount = 0
modes = []
isEqual = True
first = sayilar.count(sayilar[0])
for i in sayilar:
    if first != sayilar.count(i):
        isEqual = False
if isEqual:
    modes.append("ModYok")

if len(modes) == 0:
    for x in sayilar:
        if x in modes:
            continue
        count = sayilar.count(x)
        if count > largestCount:
            del modes[:]
            modes.append(x)
            largestCount = count
        elif count == largestCount:
            modes.append(x)

print("Mod:", modes)

with open("out.txt", "a") as dosya:
    dosya.write("Mod: {}\n".format(str(modes)))


# Medyan Hesaplama
if n % 2 == 0:
    x1 = sayilar[(n // 2) - 1]
    x2 = sayilar[(n // 2)]
    median = (x1 + x2) / 2
else:
    median = sayilar[((n + 1) // 2) - 1]

print("medyan:", median)

with open("out.txt", "a") as dosya:
    dosya.write("medyan: {}\n".format(median))


# Varyans Hesaplama
toplam = 0
for i in sayilar :
    toplam += (i-ortalama)**2

varyans = toplam/(n-1)
print("varyans: {:.9f}".format(varyans))

with open("out.txt", "a") as dosya:
    dosya.write("varyans: {:.9f}\n".format(varyans))


# Standart Sapma Hesaplama
standartSapma = math.sqrt(varyans)
print("StandartSapma: {:.9f}".format(standartSapma))

with open("out.txt", "a") as dosya:
    dosya.write("StandartSapma: {:.9f}\n".format(standartSapma))
