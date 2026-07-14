def linha():
    print("=" * 40)

def titulo():
    linha()
    print("CALCULADORA COM FUNÇÕES")
    linha()

def menu():
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: Divisão por zero!"
    return a / b

titulo()
menu()
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

opcao = int(input("Escolha uma opção (1-4): "))

if opcao == 1:
    resultado = somar(n1, n2)
elif opcao == 2:
    resultado = subtrair(n1, n2)
elif opcao == 3:
    resultado = multiplicar(n1, n2)
elif opcao == 4:
    resultado = dividir(n1, n2)
else:
    resultado = "Opção inválida!"

print(f"Resultado: {resultado}")