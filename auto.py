#ez gyartya le magat a classt - md1 2.feladat
class Auto:
    #minden fuggvenybe be kell irni a self-et
    #minden ertek ele be kell irni a self-et


    #ez ruhazza fel a targyat tulajdonsagokkal - md1 
    def __init__(self, marka_, tipus_, gyartasi_ev_, fogyasztas_ = 7.5, uzemanyag_ = 50):
        self.marka = marka_
        self.tipus = tipus_
        self.gyartasi_ev = gyartasi_ev_
        #az olyan erteket, aminek meg van adva aaz erteke, utoljara jonnek es nem kerulnek bele a fuggveny ()-be - md2 1.feladat
        self.sebesseg = 0
        #md4 1.feladat
        self.fogyasztas = fogyasztas_
        self.uzemanyag = uzemanyag_


    #ez iratja ki a targy tulajdonsagait, ha kiprinteled - md1 5.feladat és md2 5.feladat
    def __str__(self):
        return f"{self.marka} {self.tipus} ({self.gyartasi_ev}), sebesség {self.sebesseg} km/h, uzemanyag: {self.uzemanyag}" #md4 4.feladat (hozzaadtuk az uzemanyagot)
    
    #md2 2.feladat
    def gyorsit(self, ertek):
        self.sebesseg += ertek
        #megadjuk, hogy maximum mennyivel mehet az auto
        if self.sebesseg > 200:
            self.sebesseg = 200

    #md2 3.feladat
    def fekez(self, ertek):
        self.sebesseg -= ertek
        #megadjuk, hogy az auto nem mehet 0-nal kevesebbel
        if self.sebesseg < 0:
            self.sebesseg = 0

    #md4 2.feladat
    def tankol(self, mennyiseg):
        self.uzemanyag += mennyiseg
        if self.uzemanyag > 50:
            self.uzemanyag = 50

    #md4 3.feladat
    def utazik(self, tavolsag):
        fogyasztott_uzemanyag = (tavolsag / 100) * self.fogyasztas
        if fogyasztott_uzemanyag > self.uzemanyag:
            print("tankoklni kell")
        else:
            print(f"fogyasztott uzemeanyag: {fogyasztott_uzemanyag}")
            self.uzemanyag -= fogyasztott_uzemanyag