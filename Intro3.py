#while
#while <condicion_verdadera):
#   cuerpo del ciclo
#condiciones son: expresiones booleanas (or, and) y operaciones de comparación


#ciclos controlados por un contador

i=0
while i<10:
    print("ciclo") 
    #Importante modificar el valor del contador
    i=i+1
    

#Ciclos controlados por el valor de una variables

import random
a=0

while a != 5:
    a=random.randint(1,10)
    print(a)
    
print("Se acabo")

#ciclos controlados por un evento

a=0
while 1==1:
    
    a=int(input("Ingrese un número"))
    
    if a==10:
        break
    
    
    
#for: se utiliza para recorrer un ''iterable''
#lista, tupla, diccionario...

#lista: conjunto de variables organizadas en
#espacios consecutivos de memoria. A las que
#se les asigna un unico nombre. Se diferencian
#por la posición que ocupan respecto al primer
#elemento de la lista

miLista = [1, True, "Textos", 3.89] #se puede crear listas vacias
miLista2 = [] #vacia

# En Python todos son objetos.
print(miLista)
miLista.appends(45) #Se agrega al final

miLista.insert(0,"Hola") #se agrega antes del elemento cero el hola

miLista.pop() #elimina el 
miLista.pop(2) #elimina el elemento dos de la lista

miLista=[3,4,5,6,71,0,1]
miLista.sort() #ordena en forma ascendente en lista de menor a mayor

#funcion len
print(len(miLista)) #imprime cantidad de elementos en mi lista

#tupla: lista no modificable

miTupla=(2,45,6,8,9,10)


# FOR: ciclo para recorrer iterables. El cuerpo 
# se repite tantas veces como elementos tenga el
# iterable. En cada ciclo se guarda el valor del indice
# correspondiente en una variable definida.

miLista=[5,45,89,6,7]


#Estructura del for en Python:
#for <variable_donde_guardo_el_elemento in iterable.

for x in miLista:
    print(x)
    break #sólo imprimiria 5

for x in miLista:
    print(x)
    #imprime todos
    
for x in miLista:
    if x>50:
        print("Grande") #imprime sólo una vez porque sólo hay un numero mayor a 50.

#si solo utilizo el iterable para definir la cantidad de repeticiones entonces no es
#necesesaria la variable.

for _ in miLista:
    print("Ciclo")
    
    
#si no tengo lista puedo usar la función range para generar una secuencia de números

for x in range(10):
    print(x)
    
    
for x in range(-10, 10):
    print(x) #de -10 a 9
    
    
#PROMPT =pregunta-instrucción que se ingrsa a LLM, se caracteriza por expresar claramente lo que se necesita.
#refinar iterativamente 

#funcion recursiva es una funcion que se llaman asi misma
#sentencia de control de excepciones, try y except
#20, 50 10%
#40, 50, 0 15%