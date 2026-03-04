
#ezzel importaljuk at a classt ebbe a fajlba. az auto az auto.py fajl neve az Auto meg a class neve
from auto import Auto
import random

#letrehozunk targyakat es megadjuk nekik az ertekeiket
auto1 = Auto("Toyota", "Corolla", 2015)
auto2 = Auto("Ford", "Focus", 2018)
auto3 = Auto("Audi", "E-Tron GT", 2021)
auto4 = Auto("Ford", "Mustang", 2020)


# print(auto1)
# print(auto2)

# auto1.gyorsit(150)
# print(auto1)

# auto1.fekez(100)
# print(auto1)

#letrehozunk egy listat amibe belerakjuk az osszes autot
autok = [auto1, auto2, auto3, auto4]
for auto in autok:
    print(auto)

#megadunk minden autonak egy random gyorsitasi erteket
print("\n Gyorsit\n")
for auto in autok:
    auto.gyorsit(random.randint(30, 150))
    print(auto)

#megadjuk az autok atlag eletszamat
autok_szama = len(autok)
ossz_eletkor = 0
for auto in autok:
    kor = 2026 - auto.gyartasi_ev
    ossz_eletkor += kor

atlag_eletkor = ossz_eletkor/autok_szama
print(f"az autok atlagaeletkora: {atlag_eletkor} év")