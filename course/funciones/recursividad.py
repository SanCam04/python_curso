def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

def fibonacci(n):
    if n == 0:
        return(0)
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(4))

def SumNatu(n):
    if n == 0:
        return 0
    else:
        return n + SumNatu(n-1)
print(SumNatu(6))

def NumPrim(n):
    if n % 2 == 0:
        return "Es par"
    else:
        return "No lo es"
print(NumPrim(4))