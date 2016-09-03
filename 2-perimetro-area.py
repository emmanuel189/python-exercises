from math import pi
b = float(input("Introduce base: "))
h = float(input("Introduce altura: "))
r = float(input("Introduce radio: "))
areac = pi * (r ** 2)
arear = b * h
print("El area del circulo es: ", areac)
print("El area del rectangulo es: ", arear)
perimetroc = 2 * pi * r
perimetror = 2 * (b + h)
print("El perimetro del circulo es: ", perimetroc)
print("El perimetro del rectangulo es: ", perimetror)
