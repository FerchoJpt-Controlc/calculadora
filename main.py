def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b



def menu():
    print("CALCULADORA")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicar")
    print("4. Dividir")

    opcion = input("Elige una opción: ")

    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    match opcion:
        case "1":
            print("Resultado de la suma:", sumar(num1, num2))
        case "2":
            print("Resultado de la resta:", restar(num1, num2))
        case "2":
            print("Resultado de la multiplicacion:", multiplicar(num1, num2))
        case "3":
            print("Resultado de la divicion:", dividir(num1, num2))
        case _:
            print("Opción no válida")



menu()
