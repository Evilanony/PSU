broj = input("unesite broj od 0.0 do 1.0\n")

try:
    broj = float(broj)
    if broj < 1.0 and broj > 0.0:
        if broj < 0.6:
            print("F")
        elif broj >= 0.6 and broj < 0.7:
            print("D")
        elif broj >= 0.7 and broj < 0.8:
            print("C")
        elif broj >= 0.8 and broj < 0.9:
            print("B")
        elif broj >= 0.9:
            print("A")
    else:
        print("broj nije u intervalu")
except:
    if broj != float:
        print("broj nije float")
