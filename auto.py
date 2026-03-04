#ez gyartya le magat a classt
class Auto:
    #minden fuggvenybe be kell irni a self-et
    #minden ertek ele be kell irni a self-et


    #ez ruhazza fel a targyat tulajdonsagokkal
    def __init__(self, marka_, tipus_, gyartasi_ev_):
        self.marka = marka_
        self.tipus = tipus_
        self.gyartasi_ev = gyartasi_ev_
        #az olyan erteket, aminek meg van adva aaz erteke, utoljara jonnek es nem kerulnek bele a fuggveny ()-be
        self.sebesseg = 0

    #ez iratja ki a targy tulajdonsagait, ha kiprinteled
    def __str__(self):
        return f"{self.marka} {self.tipus} ({self.gyartasi_ev}), sebesség {self.sebesseg} km/h"
    
    #ezzel oldjuk meg a 2. feladatot
    def gyorsit(self, ertek):
        self.sebesseg += ertek
        #megadjuk, hogy maximum mennyivel mehet az auto
        if self.sebesseg > 200:
            self.sebesseg = 200

    #ezzel oldjuk meg a 3. feladatot
    def fekez(self, ertek):
        self.sebesseg -= ertek
        #megadjuk, hogy az auto nem mehet 0-nal kevesebbel
        if self.sebesseg < 0:
            self.sebesseg = 0