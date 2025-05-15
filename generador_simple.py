"""def my_generator():
    yield 1
    yield 2
    yield 3 

for value in my_generator():
    print(value)

def fibonachi(limit):
    a, b = 0, 1

    while a <limit:
        yield a
        a, b = b, a + b

for num in fibonachi(10):
    print(num)
"""
#generador de numeros pares
def pares(limit):
    a = 0
    b = 2

    while a < limit:
        yield a
        a = a + b

for num in pares(10):
    print(num)

def impares(limit):
    a = 1
    b = 2

    while a < limit:
        yield a
        a = a + b
for num in impares(10):
    print (num) 
        
