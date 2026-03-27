numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

if numero2 < numero1 > numero3:
    print(f"O número maior é {numero1}")
elif numero1 == numero2 or numero1 == numero3:
    print("Números iguais.")
else:
    if numero1 < numero2 > numero3:
        print(f"O número maior é {numero2}")
    elif numero2 == numero1 or numero2 == numero3:
        print("Números iguais.")
    else:
        if numero2 < numero3 > numero1:
            print(f"O número maior é {numero3}")
        elif numero3 == numero2 or numero3 == numero1:
            print("Números iguais.")