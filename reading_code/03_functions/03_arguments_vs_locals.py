x = 0.75
arg_a = 30


def fun_A(arg_a):
    print("In fun A")
    print(arg_a)
    print(x)


print("\n---- A")
print(arg_a)
fun_A(42)
print(arg_a)

print("\n---- B")
x = 30
fun_A(50)

print("\n---- C")
print(arg_a)
fun_A(42)
print(arg_a)
