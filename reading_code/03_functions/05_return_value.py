def fun_A(x, y):
    print("In fun A")
    return x * y


print("---- A")
x = fun_A(3, 8)
print(x)

print("---- B")
print(fun_A(2, 8))

print("---- C")
a = 10
b = -3
c = fun_A(a, b)
print(c)
