#Cree un programa en consola que pida un numero al usuario y
#1. Imprima los números impares entre -número y número
#2. Imprima los números primos entre 0 y número*100
#El programa debe garantizar que el usuario ingrese un numero positivo mayor a 0

def imprimir_impares(limite):
    for i in range(1, limite + 1, 2):
        print(i)

if __name__ == "__main__":
    limite = int(input("Ingrese el límite superior: "))
    print("Los números impares hasta", limite, "son:")
    imprimir_impares(limite)
    

def es_primo(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def imprimir_primos(limite):
    for i in range(2, limite + 1):
        if es_primo(i):
            print(i)

if __name__ == "__main__":
    limite = int(input("Ingrese el límite superior: "))
    print("Los números primos hasta", limite, "son:")
    imprimir_primos(limite)