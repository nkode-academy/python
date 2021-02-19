def fun_A(arg_a):
    print("In fun A")
    print(arg_a)


def fun_B(arg_a):
    print("In fun B")
    print(arg_a)


print("\n---- A")
fun_A(42)

print("\n---- B")
fun_A(50)

print("\n---- C")
fun_A("hello")

print("\n---- D")
fun_B(33)
fun_A(-32)

print("\n---- E")
fun_B(33)
fun_A(-32)
