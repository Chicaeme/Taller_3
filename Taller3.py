#Cree un programa en consola que pida un numero al usuario y
#1. Imprima los números impares entre -número y número
#2. Imprima los números primos entre 0 y número*100
#El programa debe garantizar que el usuario ingrese un numero positivo mayor a 0

def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def imprimir_impares(numero):
    print("Números impares entre -{} y {}:".format(numero, numero))
    for i in range(-numero, numero + 1):
        if i % 2 != 0:
            print(i, end=" ")

def imprimir_primos(numero):
    limite_superior = numero * 100
    print("\nNúmeros primos entre 0 y {}:".format(limite_superior))
    for i in range(limite_superior + 1):
        if es_primo(i):
            print(i, end=" ")

def main():
    while True:
        try:
            numero = int(input("Ingrese un número positivo mayor a 0: "))
            if numero <= 0:
                print("Error: Debe ingresar un número positivo mayor a 0.")
            else:
                imprimir_impares(numero)
                imprimir_primos(numero)
                break
        except ValueError:
            print("Error: Ingrese un número válido.")

if __name__ == "__main__":
    main()
