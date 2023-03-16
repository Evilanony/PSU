lista = []
uvjet = True
counter = 0
while uvjet:
    broj = input("Unesite broj ili Done\n")
    if broj.isdigit():
        broj = int(broj)
        lista.append(broj)
        counter += 1
    elif broj == "Done":
        uvjet = False
    else:
        continue
vrijednost = 0
min = lista[0]
max = lista[0]
for i in range(0, counter):
    vrijednost += lista[i]
    if min > lista[i]:
        min = lista[i]
    if max < lista[i]:
        max = lista[i]

srednja_vrijednost = vrijednost/counter
print("srednja vrijednost je: ", srednja_vrijednost, "\n",
      "minimalna vrijednost je: ", min, "\n", "maximlna vrijednost je: ", max, "\n")


lista.sort()
print(lista)
