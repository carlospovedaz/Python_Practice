#Lista de valores
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
#Se puede acceder a los valores y modificarlos de forma sencilla
# Modificar el area del bathroom
areas[-1]=10.50

# Modificar el nombre de living room por chill zone

areas[4]='chill zone'

# Puedo agregar valores sumando listas

areas_1=areas+['poolhouse',24.5]

# En este caso se crearon dos nuevas listas agregando valores en cada una de ellas
areas_2=areas_1+['garage',15.45]


#Eliminar elementos de una lista

del(areas[-1]);del(areas[-1])  #Elimiando elementos de mi lista con la funcion del

print (areas)