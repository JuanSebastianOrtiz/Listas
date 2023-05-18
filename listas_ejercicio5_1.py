#27/04/2023
# desarrolado por Juan sebastian Ortiz 
#version 1.0 
#genera una lista y de esa lista genera otras  dos listas una ordenada y la otra contando cuantas veces se repite el numero en la lista 
import random

lista = []

for i in range(10):  
    lista.append(random.randint(1, 5))

print("Lista :", lista)

ocurrencias = {}

for numero in lista:
    if numero in ocurrencias:
        ocurrencias[numero] += 1
    else:
        ocurrencias[numero] = 1

frecuencias = []

for numero, frecuencia in ocurrencias.items():
    frecuencias.append((numero,"se repite ", frecuencia, "veces"))

print("Frecuencias:", frecuencias)