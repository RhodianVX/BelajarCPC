import math

banyakLoop = int(input())
arrayCounter = []

for i in range(banyakLoop):
    bilangan = int(input())

    counter = 0
    for j in range(1, int(math.sqrt(bilangan) // 1) + 1):
        if(bilangan % j == 0):
            counter = counter + 1

    if(counter <= 2):
        arrayCounter.append("YA")
    else:
        arrayCounter.append("BUKAN")

print()
for i in range(len(arrayCounter)):
    print(arrayCounter[i])