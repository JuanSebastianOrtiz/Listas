#desarrollado por :juan Sebastian Ortiz
#24/04/2023
#version 1.0
#programa que ingrese dato a dato elementos a la lista y los ordena
lista=[]
for x in range(5):
  valor=int(input("ingrese un numero: "))
  lista.append(valor)
for k in range(4):
    for x in range(4):
        if lista[x]>lista[x+1]:
          aux=lista[x]
          lista[x]=lista[x+1]
          lista[x+1]=aux
print(lista)