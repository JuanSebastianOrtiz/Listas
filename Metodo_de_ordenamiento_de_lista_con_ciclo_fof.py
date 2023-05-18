 # ejemplos de ejercicicios ordenamiento de listas con cciclo for
#programado por :juan sebastian ortiz
# version 1.0

sueldos=[]
for x in range(5):
  valor=int(input("ingrese sueldo: "))
  sueldos.append(valor)

print("Lista sin ordenar")
print(sueldos)

for x in range(4):
    if sueldos[x]>sueldos[x+1]:
      aux=sueldos[x]
      sueldos[x]=sueldos[x+1]
      sueldos[x+1]=aux

print("Lista con el ultimo elemento ordenado ")
print(sueldos)