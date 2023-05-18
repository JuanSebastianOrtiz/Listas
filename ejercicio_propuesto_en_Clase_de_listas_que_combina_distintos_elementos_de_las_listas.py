
# ejercicio de listas propuesto como taller en clase con distintos ciclos y estructuras
#programador :Juan sebastian ortiz ibarra 
#vérsion 1.0 

#capturar los elementos de la lista
list=[]
listPosRep=[]
listNORep=[]
valor=int(input("Ingresar valor (0 para finalizar)"))
while valor!=0:
  list.append(valor)
  valor=int(input("Ingresar valor (0 para finalizar)"))
print("tamaño de la lista")
print(list)


print("Pedir un dato y buscarlo")
NumBus=int(input("ingrese el numero a buscar: "))


poslis=0
canEleRep=0
while poslis< int(len(list)):
  if list[poslis]==NumBus:
      canEleRep=canEleRep+1  
      print("Lo encontró en la posición", poslis)
      listPosRep.append(poslis) 
  else:
      listNORep.append(poslis) 
      print("Posiciones vacias",posl )
  poslis=poslis+1

print("El numero se repite ", canEleRep, "veces")
print("Lista de repeticion",listPosRep)