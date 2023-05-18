 # ejemplos de ejercicicios ordenamiento de listas con ciclo for y .append
#programado por :juan sebastian ortiz
# version 1.0

sueldos=[]
for x in range(5):
  valor=int(input("ingrese sueldo: "))
  sueldos.append(valor)

print("Lista sin ordenar")
print(sueldos)
canInt=0
for k in range(4):
    for x in range(4):
        if sueldos[x]>sueldos[x+1]:
          aux=sueldos[x]
          sueldos[x]=sueldos[x+1]
          sueldos[x+1]=aux
          canInt=canInt+1
print("Lista ordenada")
print(sueldos)
print("Numero de intercambios: ", canInt)