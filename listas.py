#Listas son estructuras de datos que permiten alamacenar muchos valores como una sola variable

pesos=[1.1,2.2,3.4,1.2,1.6]

#Se puede acceder a esta lista de multiples formas
contador=1
for elementos in pesos:
    print('Peso {}: {} cm'.format(contador,elementos))
    contador+=1

#La listas pueden contener muchos tipos de datos incluso listas

pesos=[['Carlos',65,70,68],['Leslye',50,48,49], ["Robin",80,75,70]]
print(pesos[0])

#Obtener o llamaer elementos de una lista

nombres=['Carlos','Robin','Israel','Leslye','Jonathan','Andres']

print(nombres[1],nombres[-2], nombres[0:4],nombres[:4],nombres[1:]) #Diferentes forma de llamar elementos de una lista, simple, negativa y agrupada

#Lista de areas y valores
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Mostrar el segundo elemento
print(areas[1])

# Mostrar el ultimo elemento de la lista
print(areas[-1])

# Mostrar el area de la living room
print(areas[5])

