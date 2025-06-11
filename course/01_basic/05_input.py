
print("Holaa como te llamas")
nombre = input()

print(f"hola {nombre}, como estas?")
age= input("cuantos anos tienes?")
age = int(age)
print(f"tienes {age} anos")

print("obtener multiples valores a la vez")
country, city =input("en que pais y ciudad vives?").split()
print(f"vives en {country},{city}")