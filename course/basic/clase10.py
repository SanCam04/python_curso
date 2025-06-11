numbers = {1:"uno",2:"dos",3:"tres"}
print(numbers[2])
information = {"nombre":"Daniel",
               "apellido": "Camacho",
               "altura": "1.74",
               "edad":"20"}

print(information)
del information["edad"]
print(information)

claves = information.keys()
print(claves)
print(type(claves))
values = information.values()
print(values)

pairs = information.items()
print(pairs)

contacts = {   "Diego": {
               "apellido": "Florida",
               "altura": "1.80",
               "edad":"30"},
               "Daniel" : {
               "apellido": "Camacho",
               "altura": "1.74",
               "edad":"20"}
               }
print(contacts["Daniel"])



