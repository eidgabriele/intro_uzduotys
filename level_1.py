
eiluciu_skaicius = 0
eiluciu_ilgiai = []
didziuju_kiekiai = []
with open('level_1.txt', 'r') as failas:
    tekstas = failas.readlines()
    for eilute in tekstas:
        didziosios = 0
        eiluciu_skaicius += 1 
        for raide in eilute:
            if raide.isupper():
                didziosios += 1
        ilgis = len(eilute.split())
        eiluciu_ilgiai.append(ilgis)
        didziuju_kiekiai.append(didziosios)
        print(f"Eilute {eiluciu_skaicius}: {ilgis} zodziu, {didziosios} didziuju raidziu")

ilgiausia = eiluciu_ilgiai.index(max(eiluciu_ilgiai))
daugiausia = didziuju_kiekiai.index(max(didziuju_kiekiai))


print(f"Tekste rastos {eiluciu_skaicius} eilutes")
print(f"ilgiausia eilute yra {ilgiausia+1}-a: {tekstas[ilgiausia]}")
print(f"daugiausiai didziuju raidziu {daugiausia+1}-oje eiluteje: {tekstas[daugiausia]}")

vientisas_tekstas = "".join(tekstas)
sakiniu_kiekis= vientisas_tekstas.count('.')+vientisas_tekstas.count('?')+vientisas_tekstas.count('!')

print(f"Tekste sakiniu yra {sakiniu_kiekis}")