from auto import Auto
autok = []
with open('C:\Users\RonaiMarton\projektek\2026_03_04_Osztalyok_gyakorlas\__pycache__\auto.cpython-313.pyc', 'r', encoding='utf-8') as forrasfajl:
    next(forrasfajl)
    for sor in forrasfajl:
        adatok = sor.strip().split(',')
        if len(adatok) >= 4:
            marka, tipus, gyartasi_ev, fogyasztas = adatok
        auto = Auto(marka, tipus, int(gyartasi_ev), float(fogyasztas))
        autok.append(auto)

print(f'{autok=}')
    