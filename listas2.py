#Lista de areas y valores
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

#Extraccion de valores y uso

area_total_cocina_dormitorio=areas[3]+areas[7]

print(area_total_cocina_dormitorio) #Obtengo los valores que necesito y los sumo en una nueva variable

#Lista con listas de datos agrupados
areas = [["hallway", 11.25], ["kitchen", 18.0], ["living room", 20.0], ["bedroom", 10.75], ["bathroom", 9.50]]
print(type(areas[-1]))
#Llamado de listas dentro de listas
print(areas[-1][1]) #De la ultima lista llama el elemento 1