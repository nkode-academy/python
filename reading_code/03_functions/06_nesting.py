
def fun_A(a):
    print("In A")
    fun_B(a)
    print("End of A")


def fun_B(b):
    print("In B")
    if b == 0:
        fun_C()
    else:
        fun_D()
    print("End of B")


def fun_C():
    print("In C")
    print("End of C")


def fun_D():
    print("In D")
    fun_B(0)
    print("End of D")


fun_A(10)
