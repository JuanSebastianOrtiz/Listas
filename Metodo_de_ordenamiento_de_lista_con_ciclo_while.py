 # ejemplos de ejercicicios ordenamiento de listas con ciclo while el cual muestra el largo de la lista
#programado por :juan sebastian ortiz
# version 1.0

list=[]
valor=int(input("Ingresar valor (0 para finalizar)"))
while valor!=0:
  list.append(valor)
  valor=int(input("Ingresar valor (0 para finalizar)"))
print("tamaño de la lista")
print(len(list))