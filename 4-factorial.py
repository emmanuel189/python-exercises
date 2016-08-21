factorial = 1
n = int(input("Introduce un numero: "))
for i in range(n):
    factorial *= n
    n = n - 1
print("El factorial es ", factorial)
