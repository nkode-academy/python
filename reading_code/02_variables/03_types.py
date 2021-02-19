print("----- A")

x = 12
y = 13

print(type(x))
print(x)
print(type(y))
print(y)


print("----- B")

x = 12
y = 13.0

print(type(x))
print(x)
print(type(y))
print(y)


print("----- C")

x = "12"
y = "13.0"

print(type(x))
print(x)
print(type(y))
print(y)


print("----- D")

x = 12
y = 13.0
z = str(x)

print(type(x))
print(x)
print(type(y))
print(y)
print(type(z))
print(z)


print("----- E")

x = 12
y = 13.0
a1 = x + y
a2 = str(x) + str(y)
a3 = y + x
a4 = str(y) + str(x)

print(type(a1))
print(a1)
print(type(a2))
print(a2)
print(type(a3))
print(a3)
print(type(a4))
print(a4)
