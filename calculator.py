
print("Simpel Lommeregner")
print("Vælg operation:")
print("1 = Plus")
print("2 = Minus")
print("3 = Gange")
print("4 = Divide")

valg = input("Indtast dit valg (1/2/3/4): ")

tal1 = float(input("Indtast første tal: "))
tal2 = float(input("Indtast andet tal: "))

if valg == "1":
    resultat = tal1 + tal2
    print("Resultat:", resultat)

elif valg == "2":
    resultat = tal1 - tal2
    print("Resultat:", resultat)

elif valg == "3":
    resultat = tal1 * tal2
    print("Resultat:", resultat)

elif valg == "4":
    if tal2 != 0:
        resultat = tal1 / tal2
        print("Resultat:", resultat)
    else:
        print("Man kan ikke dividere med 0!")

else:
    print("Ugyldigt valg")