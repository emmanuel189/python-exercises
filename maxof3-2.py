# Maximum of three numbers
list = list()
for i in range(3):
    list.append(int(input("Introduce a number: ")))
list.sort()
print("Maximum is: ", list[len(list) - 1])
