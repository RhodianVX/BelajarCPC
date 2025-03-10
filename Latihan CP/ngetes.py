array = []
tes = 4

matriks = [[1,2,3,4], [2,3,4,5], [3,4,5,6]]

for i in range(tes):
    array.append(0)
print(array)
# ubah
for i in range (3):
    matriks[i] = array
 
matriks[1][2] = 1

for i in range(3):
    for j in range(4):
        print(matriks[i][j], end=" ")
    print()

print(array)