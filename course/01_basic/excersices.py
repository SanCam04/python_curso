###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

from os import system
if system("clear") != 0: system("cls")

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

### Completa aquí

name, city =input("Cual es tu nombre y donde vives ").split()
print(f"Tu numbre es {name}, \n Vives en {city}")

print("--------------")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None
print(type(a)), print(type(b)), print(type(c)),print(type(d)),print(type(e))

### Completa aquí

print("--------------")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

### Completa aquí
cadena1 = "12345"
cadena1 =(int(cadena1))
print(type(cadena1))
cadena1 =(float(cadena1))
print(type(cadena1))


numero = 3.5
numero = int(numero)
print(numero)
print(int(numero))
#trunca el número: 3.99 se convierte en 3, porque corta todo lo que está después del punto.
numero = 3.99
print(round(numero))  # Esto sí imprime 4



print("--------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"
name, age, hight = input("Could you give me your name, age and hight please?? \n").split()
print(f"Your name sr is {name}, your age is {age} and finally your hight is {hight}")
### Completa aquí

print("--------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")
PI = 3.1416
print(round(PI))
print(round(PI)//2)