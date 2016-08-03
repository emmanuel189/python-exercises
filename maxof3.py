a = int(input(“Introduce a number: ”))
b = int(input(“Introduce a nubmer: ”))
c = int(input(“Introduce a number: ”))
if a > b:
    if a > c:
        print(“Maximum is ”, a)
    else:
        print(“Maximum is ”, c)
elif b > c:
    print(“Maximum is ”, b)
else:
    print(“Maximum is ”, c)
