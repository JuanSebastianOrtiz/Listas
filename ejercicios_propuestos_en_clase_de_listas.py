 # ejercicio propuesto en clase de listas 
#programado por :juan sebastian ortiz
# version 1.0

# Capturar los elemnetod de la lista
cont=0
list=[]
for i in range (5):
  valor=int(input("ingrese un valor entero: "))
  list.append(valor)

mayor=list[0]
for x in range (1,5):
    if list [x]>mayor:
        mayor=list[x]

print("lista completa")
print(list)
print("Mayor de la lista")
print(mayor)

menor=mayor
for x in range (0,5):
    if list [x]<menor:
        menor=list[x]

print("Menor de la lista")
print (menor)
#Leer numeros por teclado y responder
#si esta o no esta
#cuantas veces se repite y en que poscisiones 

NumBus=int(input("ingrese el numero a buscar: "))

if list[x]== NumBus:
  print("EL numero que se repite es: ", NumBus)
  cont=cont+1
  print(cont)
else: 
  print("El numero no esta en la lista")