import math

# tipo de operação
def add (x, y):
    return x + y

def subtract (x, y):
    return x - y

def multiply (x, y):
    return x * y

def divide (x, y):
    return x / y

def power (x, y):
    return x ** y

def sqrt (x):
    return math.sqrt(x)

def factorial(x):
    return math.factorial(int(x))

# dicionario de funções
operations = {
    '1': add,
    '2': subtract,
    '3': multiply,
    '4': divide,
    '5': power,
    '6': sqrt,
    '7': factorial
}

# programa princial loop
while True:
    
    try:
        print("Select operation:")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Porcentagem")
        print("6. Raiz Quadrada")
        print("7. Fatorial")
        choice = input("Enter choice (1/2/3/4/5/6/7): ")
        if choice in ['1', '2', '3', '4', '5']:
            num1 = float(input("Primeiro Número: "))
            num2 = float(input("Segundo Número: "))
            if choice == '4' and num2 == 0:
                print("Erro: Divisão do zero")
            else:
                result = operations[choice](num1, num2)
                print(num1, "/", num2, "=", result)
        elif choice == '6':
            num = float(input("Digite o número: "))
            if num < 0:
                print("Erro: Raiz quadrada por número 0")
            else:
                result = operations[choice](num)
                print("sqrt(", num, ") =", result)
        elif choice == '7':
            num = float(input("Digite o número: "))
            if num < 0:
                print("Erro: Fatorial por número negativo")
            else:
                result = operations[choice](num)
                print(num, "! =", result)
        else:
            print("Opção Inválida")
    except ValueError:
        print("Erro: Opção inválida")

    # perguntar ao usúario se quer fazer outro calculo
    choice = input("Gostaria de calcular novamente? (y/n)")
    if choice.lower() != 'y':
        break

print ("Espero ter ajudado, até mais.")
