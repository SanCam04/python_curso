a = [1,2,3,4,5,6]
b = a
print(a)
print(b)
del a [0]
print(a)
print(id(b))
c = a[:]
print(id(c))
a.append(6)
print((a))
print((b))
print((c))