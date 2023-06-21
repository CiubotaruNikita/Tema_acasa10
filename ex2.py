numar_oaspeti = int(input("Câți oaspeți vor veni? "))
comenzi_oaspeti = {}

for _ in range(numar_oaspeti):
    nume_oaspete = input("Introduceți numele oaspetelui: ")
    felul_mancarii1 = input("Introduceți primul fel de mâncare: ")
    felul_mancarii2 = input("Introduceți al doilea fel de mâncare: ")
    comenzi_oaspeti[nume_oaspete] = (felul_mancarii1, felul_mancarii2)

print("Oaspeții vor fi:", list(comenzi_oaspeti.keys()))

numar_preparate = {}

for comenzi in comenzi_oaspeti.values():
    for preparat in comenzi:
        numar_preparate[preparat] = numar_preparate.get(preparat, 0) + 1


for oaspete, comenzi in comenzi_oaspeti.items():
    print(oaspete, "a comandat", comenzi[0], "și", comenzi[1])

print("Va trebui să pregătiți:")
for preparat, numar in numar_preparate.items():
    print(preparat, "x", numar)