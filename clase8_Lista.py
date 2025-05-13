to_do = ["Dirigirnos al hotel",
         "Ir a almorzar",
         "Ir a un museo",
         "Volever al hotel"]

print(to_do)
numbers = [1,2,3,4, "cinco"]
print(type(numbers))
print(numbers)

mix = ["uno", 2, 3.14, True, [1,2,3]]

print(mix)
print(len(mix))
print("Primer elemento",mix[0])
print("Segundo elemento",mix[1])
print("Ultimo elemento",mix[-1])

String = "Hola Mundo"
print("Primer elemento",String[0])
print("Segundo elemento",String[1])
print("Ultimo elemento",String[-1])
print(mix[0:2])
print(mix[2:-2])

print(mix)
#anadir
mix.append(False)
print(mix)
#reemplazar por posicion
mix.insert(1,["a","b"])
print(mix)
#encontrar 
print(mix.index(["a","b"]))
#magnitudes mayor y menor
numbers = [1,2,100,200,300,440,100,222]
print(numbers)
print("mayor",max(numbers))
print("mayor",min(numbers))
#Eliminar posiciones
del numbers[-1]
print(numbers)
del numbers[:2]
print(numbers)