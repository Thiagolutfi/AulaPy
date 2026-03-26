nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
faltas = int(input("Quantiade de faltas: "))
media = (nota1 + nota2) / 2

if media >= 6 and faltas <= 20:
    print(f"Aprovado com média de: {media:.1f}\nFaltas: {faltas}")
else:
    if  4 < media < 6 and faltas <= 20:
        print(f"Em recuperação com média de {media:.1f}\nFaltas: {faltas}")
    else:
        if media < 4 and faltas > 20:
            print(f"Reprovado com média de {media:.1f} e repovado por falta.\nFaltas: {faltas}")
        elif faltas > 20:
            print(f"Reprovado pode exesso de faltas.\nFaltas: {faltas}")
        elif media < 4:
            print(f"Reprovado com média de {media:.1f}.\nFaltas: {faltas}")

