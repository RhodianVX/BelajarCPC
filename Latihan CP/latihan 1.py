def rotate_counter_clockwise():
    sementara = []
    for i in range(len(matriks)):
        temp = []
        for j in range (len(matriks[i])):
            temp.append(matriks[j][len(matriks) - 1 - i])
        sementara.append(temp)
    return sementara
            
def transpose():
    sementara = []
    for i in range(len(matriks)):
        temp = []
        for j in range (len(matriks[i])):
            temp.append(matriks[j][i])
        sementara.append(temp)
    return sementara

def mirror_x_axis():
    sementara = []
    for i in range(len(matriks)):
        temp = []
        for j in range (len(matriks[i])):
            temp.append(matriks[len(matriks) - 1 - i][j])
        sementara.append(temp)
    return sementara

def mirror_y_axis():
    sementara = []
    for i in range(len(matriks)):
        temp = []
        for j in range (len(matriks[i])):
            temp.append(matriks[i][len(matriks) - 1 - j])
        sementara.append(temp)
    return sementara

def tampil_matriks():
    for i in range(len(matriks)):
        for j in range (len(matriks[i])):
            print(matriks[i][j], end=" ")
        print()

matriks = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

print("Menu Pilihan")
print("1. putar 90 derajat")
print("2. transpose")
print("3. mirror sumbu x")
print("4. mirror sumbu y")
menu = int(input("Masukkan menu : "))

if(menu == 1):
    matriks = rotate_counter_clockwise()

elif(menu == 2):
    matriks = transpose()

elif(menu == 3):
    matriks = mirror_x_axis()

elif(menu == 4):
    matriks = mirror_y_axis()

tampil_matriks()