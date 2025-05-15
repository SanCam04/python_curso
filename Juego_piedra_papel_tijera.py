x = input("Escribe tu eleccion entre " \
"piedra, papel o tijera ")
y = input("Escribe tu eleccion entre " \
"piedra, papel o tijera ")

if x == "piedra" and y == "tijera":
    print("piedra le gana a tijera")
    print("Gana x")
elif x == "papel" and y == "piedra":
    print("Papel le gana a piedra")
    print("Gana x")
elif x == "tijera" and y == "papel":
    print("tijera le gana a papel")
    print("Gana x")
else:
    print("Gana y")