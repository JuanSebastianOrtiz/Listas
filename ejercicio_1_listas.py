#desarrollado por :juan Sebastian Ortiz
#24/04/2023
#version 1.0
#programa que carga aleatoriamente 30 numeros en una lista los imprime y el valor digito lo remplaza por un -1 
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

if num == -1:
    print [list1]