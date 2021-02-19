def fun_A():
    print("In fun A")
    return 42


print("---- A")
fun_A()

print("---- B")
x = fun_A()
print(x)

print("---- B")
print(fun_A())
