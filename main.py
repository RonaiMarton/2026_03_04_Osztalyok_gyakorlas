
#ezzel importaljuk at a classt ebbe a fajlba. az auto az auto.py fajl neve az Auto meg a class neve
from auto import Auto
import random

#letrehozunk targyakat es megadjuk nekik az ertekeiket - md1 3.feladat
auto1 = Auto("Toyota", "Corolla", 2015)
auto2 = Auto("Ford", "Focus", 2018)
#letrehozunk meg 3 targyat - md3 1.feladat
auto3 = Auto("Audi", "E-Tron GT", 2021)
auto4 = Auto("Ford", "Mustang", 2020)
auto4 = Auto("Ford", "Mustang", 2002)


# print(auto1)
# print(auto2)

# auto1.gyorsit(150)
# print(auto1)

# auto1.fekez(100)
# print(auto1)

#letrehozunk egy listat amibe belerakjuk az osszes autot - md3 2.feladat
autok = [auto1, auto2, auto3, auto4]
for auto in autok:
    print(auto)

#megadunk minden autonak egy random gyorsitasi erteket - md3 3.feladat
print("\n Gyorsit\n")
for auto in autok:
    auto.gyorsit(random.randint(30, 150))
    print(auto)

#megadjuk az autok atlag eletkorat - md3 4.feladat
autok_szama = len(autok)
ossz_eletkor = 0
for auto in autok:
    kor = 2026 - auto.gyartasi_ev
    ossz_eletkor += kor

atlag_eletkor = ossz_eletkor/autok_szama
print(f"az autok atlagaeletkora: {atlag_eletkor} év")

#megadjuk a legidosebb auto adatait - md3 5.feladat A-verzio
legidosebb_auto = None
legidosebb_auto_kora = 0
for auto in autok:
    kor = 2026 - auto.gyartasi_ev
    if kor > legidosebb_auto_kora:
        legidosebb_auto_kora = kor
        legidosebb_auto = auto
print(f"a legidosebb auto kora:{legidosebb_auto_kora}, adatai: {legidosebb_auto}")

#md3 5.feladat B-verzio
autok_kora = []
for i in autok:
    autok_kora.append(2026- i.gyartasi_ev)

legidosebb_auto_indexe = autok_kora.index(max(autok_kora))
print(f"a legidosebb auto kora: {max(autok_kora)}, adatai: {autok[legidosebb_auto_indexe]}")

#md3 5.feladat C-verzio
gyartasi_evek = [auto.gyartasi_ev for auto in autok]
for auto in autok:
    if auto.gyartasi_ev == min(gyartasi_evek):
        print(f"a legidosebb auto adatai: {auto}___{2026 - auto.gyartasi_ev}")
        print(f"a legidosebb auto: {auto.marka} {auto.tipus}")