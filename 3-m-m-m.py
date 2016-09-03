lista = list()
suma = 0
for i in range(3):
    lista.append(int(input("Introduce un numero: ")))
lista.sort()
print("El minimo es: ", lista[0])
print("El maximo es: ", lista[len(lista)-1])
for i in range(len(lista)):
    suma += lista[i]
mediana = suma / len(lista)
print("La mediana es: ", mediana)
