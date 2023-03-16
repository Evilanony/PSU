print("unesite radne sate")
radni_sati = float(input())
print("unesite satnicu")
satnica = float(input())


def total_euro(radni_sati, satnica):
    zarada = radni_sati*satnica
    print("zarada je ", zarada)


total_euro(radni_sati, satnica)
