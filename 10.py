num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
num3 = int(input("Digite um número: "))
num4 = int(input("Digite um número: "))
num5 = int(input("Digite um número: "))
num6 = int(input("Digite um número: "))
num7 = int(input("Digite um número: "))
num8 = int(input("Digite um número: "))
num9 = int(input("Digite um número: "))
num10 = int(input("Digite um número: "))

numeros = [num1, num2, num3, num4, num5, num6, num7, num8, num9, num10]

numeros_ord = sorted(numeros)

print(" em ordem crescente:")
for numero in numeros_ord:
    print(numero)