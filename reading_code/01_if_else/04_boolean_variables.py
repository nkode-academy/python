x = 0.3

a1 = True
a2 = x >= 0.3
a3 = a1 and a2
a4 = a2 or a3 or True
a5 = not a4
a6 = a1 and a2 or a3 and a4

if a1:
    print("A1")

if a2:
    print("A2")

if a3:
    print("A3")

if a4:
    print("A4")

if a5:
    print("A5")

if a6:
    print("A6")
