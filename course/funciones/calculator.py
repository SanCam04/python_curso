def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def calculator():

    while True:
        print("Buenas compa",
            "Ingresando a la calculadora")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicacion")
        print("4. Division")
        print("5. Salir")

        option = str(input("Seleccione un valor de 1 a 5: "))
        
        if option == "5":
            print("Saliendo de la Calculadora ")
            break
        if option in ["1","2","3","4"]:

            a = float(input("Ingrese el primer valor: "))
            b = float(input("Ingrese un segundo valor: "))
            
            if option == "1":
                print("La suma de los valores " \
                "ingresadon son: ",add(a, b))
            elif option == "2":
                print("La resta de los valores " \
                "ingresadon son: ",substract(a, b))
            elif option == "3":
                print("La multiplicacion de los valores " \
                "ingresadon son: ",multiply(a, b))
            elif option == "4":   
                print("La division de los valores " \
                "ingresados son: ",divide(a, b))    
        else:
            print("Valor ingresado incorrectamente")
calculator()
