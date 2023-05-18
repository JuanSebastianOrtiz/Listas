#desarrollado por :juan Sebastian Ortiz
#24/04/2023
#version 1.0
#programa que carga aleatoriamente 30 numeros en una lista los imprime remplaza valor ecrito por -1 y despues lo sca de la lista yt añade un 5 a la lista
import random
lista = []
longitud = 30
list1 = []
for i in range (longitud):
    lista.append(random.randint(0,30))
print(lista)     

num=int(input("Digite un numero de la lista"))
for i in range (longitud):
    if lista [i] == num:
        lista [i] = -1
print (lista)
print("Lista removiendo el -1")
lista.remove(-1)
print(lista)        

lista.append(5)
for k in range(29):
    for x in range(29):
        if lista[x]>lista[x+1]:
          aux=lista[x]
          lista[x]=lista[x+1]
          lista[x+1]=aux
print(lista)