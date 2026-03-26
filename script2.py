print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
opcao = int(input("Escolha uma das opções acima: "))


numero1 = float(input("Informe o primeiro número: "))
numero2 = float(input("Informe o segundo número: "))

if opcao == 1:
    print(f"O resultado da Soma é: {numero1 + numero2} ")
elif opcao == 2:
    print(f"O resultado da Subtração é: {numero1 - numero2} ")
elif opcao == 3:
    print(f"O resultado da Multiplicação é: {numero1 * numero2} ")
elif opcao == 4:
    if numero2 != 0:
        print(f"O resultado da Divisão é: {numero1 / numero2} ")
    else:
        print("Não é possível fazer uma divisão por 0.")
else:
    print("Digite uma opção válida.")
