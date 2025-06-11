add = lambda a, b: a + b
print(add(10, 4))

#Cuadradado de cada numero
numbers = range(11)
squared_numbers = list(map(lambda x : x ** 2, numbers))
print("Cuadrados:", squared_numbers)

#obtener numeros pares
 
even_numbers = list(filter(lambda x: x%2 == 0, numbers))
print("pares", even_numbers)