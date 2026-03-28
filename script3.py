'''Faça um algoritmo que solicita ao usuário as notas de três provas. Calcule a média
aritmètica e informe se o aluno foi Aprovado ou Reprovado (o aluno é considerado aprovado
 com média igual ou superior a 6'''

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 6:
    print("Aprovado!")
else:
    print("Reprovado.")


'''Faça um algorítmo que solicita ao usuário um valor inteiro e exibe uma mensagem informando
se o número é par ou ímpar.'''

numero = int(input("Digite um número: "))

resto = numero % 2

if resto == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é impar.")


'''Faça um algorítmo que solicita ao usuário um número inteiro e exiba este número inteiro 
na tela. Se o número for negativo , antes de ser exibido, ele deve ser transformado no equivalente positivo.'''

numero = int(input("Digite um número: "))


if numero > 0:
    print(numero)
else:
    numero = numero * -1
    print(numero)

'''Faça um algoritmo que solicita ao usuário uma letra e exiba uma 
 mensagem informando se é uma vogal ou uma consoante.'''

letra = input("Digite uma letra: ").lower()

if letra == "a" or letra == "e" or letra == "i" or letra == "o"or letra == "u" :
    print(f"A letra {letra} é uma vogal")
else:
    print(f"A letra {letra} é uma consoante.")

'''Faça um algoritmo que solicia um número inteiro e exibe uma mensagem indicando se 
ele é positivo, negativo ou zero.'''

numero = int(input("Digite um número inteiro: "))
if numero > 0:
    print(f"O número {numero} é positivo.")
else:
    if numero == 0:
        print("O número é 0.")
    else:
        print(f"O número {numero} é negativo.")

'''Faça um algoritmo que solicita ao usuário dois número inteiros. O primeiro é valor 
das horas e o segundo dos minutos. Verifique as a hora é válida e exiba uma mensagem 
correspondente (São válidas as horas entre 00:00 e 23:59).'''

hora = int(input("Digite as horas: "))
minuto = int(input("Digite os minutos: "))

if 0 <=hora <= 23 and  0 <= minuto <= 59:
    print("São válidas as horas entre 00:00 e 23:59")
else:
    print(f"Hora Válida.")


'''Faça um algoritmo que solicira ao usuário três números e exibe na tela apenas o maior 
deles. Caso eles sejam iguais exiba a mensagem "Números iguais.'''

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

'''Faça um algoritmo que solicita ao usuário três números e exibe na tela apenas o menor 
deles, ou uma mensagem informando que os números são iguais. '''

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

if numero2 > numero1 < numero3:
    print(f"O menor número é {numero1}")
elif numero1 == numero2 or numero1 == numero3:
    print("Números iguais.")
else:
    if numero1 > numero2 < numero3:
        print(f"O menor número é {numero2}")
    elif numero2 == numero1 or numero2 == numero3:
        print("Números iguais.")
    else:
        if numero2 > numero3 < numero1:
            print(f"O menor número é {numero3}")
        elif numero3 == numero2 or numero3 == numero1:
            print("Números iguais.")

'''Faça um algoritmo que solicita ao usuário três valores correspondentes ao lados de um triângulo .
Informe se o triângulo é equilátero, isóceles ou escaleno.'''

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
valor3 = float(input("Digite o terceiro valor: "))

if valor1 == valor2 == valor3:
    print("O triângulo é equilátero")
else :
    if valor1 == valor2 or valor1 == valor3 or valor2 == valor3:
        print("O triânguo é isóceles")
    else:
        print("O triângulo é escaleno.")


'''Faça um algoritmo que solicite o salário fixo e o valor das vendas efetuadas pelo vendedor de uma 
empresa. Sabendo-se que ele recebe uma comissão de 3% sobre o total de vendas até R$1500 mais
5% sobre o que ultrapassar este valor, calcular e escrever o seu salário total.'''

salario_fixo = float(input("Digite o salário: "))
valor_vendas = float(input("Digite o valor das vendas: "))

if valor_vendas <= 1500:
    comissao = valor_vendas * (3/100)
elif valor_vendas > 1500:
    comissao = 1500 * (3/100) + (valor_vendas - 1500) * (5/100)

salario_total = salario_fixo + comissao

print(f"O salário total é {salario_total}")