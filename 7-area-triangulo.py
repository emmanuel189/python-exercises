import math
a = int(input("Introduce el valor de a: "))
b = int(input("Introduce el valor de b: "))
c = int(input("Introduce el valor de a: "))
p = (a + b + c) / 2 # Perimetro
area = math.sqrt(p * (p - a) * (p - b) * (p - c))
print("El area es: ", area)
