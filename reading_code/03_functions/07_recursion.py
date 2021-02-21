
def fun_A(a):
    print("In A with a = ", a)

    if a == 0:
        print("==== Level 0")
        print("==== Returning 1")
        return 1

    b = 2 * fun_A(a - 1)
    print("Returning ", b)
    return b


print("---- A")
fun_A(3)

print("---- B")
fun_A(10)
