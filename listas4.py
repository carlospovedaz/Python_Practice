# Las listas en python funcionan de forma particular
#Basicamente no son un valor que guarda un dato sino mas bien
#Una referencia de memoria hacia un conjunto de datos

x=[1,2,3,4]

y=x

y[0]=23

print(x,y)

#Se puede ver como al realizar una copia de la lista en otra variable y modificar un datos ambos sufren modificaciones
#Esto debido a que no creo una copia sino mas bien referencia la nueva lista a ese conjunto de datos existente
#Por lo tanto modifico ambos datos al realizar cambios
#en caso de que querer copiar una lista se utiliza la siguiente funcion
x=[1,2,3,4]
y=list(x)
y[0]=23


print(x,y) # Se nota el cambio con la utilizacion de dicho metodo