def fun_A(a, b):
    print("Start of fun A")
    print(a)
    print(b)
    print("End of fun A")


def fun_B(a, b, c, d, e, f):
    print("Start of fun B")
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)
    print("End of fun B")


print("\n---- A")
fun_A(42, 0.1)

print("\n---- B")
x = 32
y = 17
fun_A(x, y)

print("\n---- C")
fun_B(1, 2, 3, 4, 5, 6)
