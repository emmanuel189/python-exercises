def fibonacci(n):
    a, b = 1, 1
    list = list()
    for i in range(n):
        a, b = b, a + b
        list.append(a)
    print(list)
n = int(input("Introduce un numero: "))
fibonacci(n)
