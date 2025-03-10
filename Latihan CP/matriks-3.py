def tetris(matriks):
    # menghapus seluruh nilai 1 yang ada
    pointer = 0
    isStrait = True

    arrayTes = []
    for z in range(C):
        arrayTes.append(1)

    while(isStrait == True):
        # proses menghapus baris yang bernilai 1 semua
        isStrait = False
        for i in range(R):
            if(matriks[i] == arrayTes):
                for j in range(C):
                    matriks[i][j] = 0
                isStrait = True
                pointer = i

        # proses menukar nilai terbawah
        for i in range(C):
            # menukar nilai 1 dengan 0
            lokasi = pointer
            temp = []
            while(lokasi >= 0):
                if(matriks[lokasi][i] == 1):
                    temp.append(lokasi)
                lokasi = lokasi - 1
            counter = len(temp)
            for n in temp:
                matriks[n][i] = 0

            # menurunkan nilai 1
            j = 0
            while (j < R):
                if (matriks[j][i] == 1):
                    position = j
                    j = R
                elif(j == R - 1):
                    position = R
                
                j = j + 1

            upper = 1
            while (counter != 0):
                matriks[position - upper][i] = 1
                upper = upper + 1
                counter = counter - 1

    return matriks

    
R, C = map(int, input().split())
matriks = []

#  Memasukkan matriks
for _ in range(R):
    baris = []
    input_baris = input()  # Baca satu baris input tanpa spasi
    for karakter in input_baris:
        baris.append(int(karakter))  # Konversi karakter ke integer
    matriks.append(baris)

matriks = tetris(matriks)

print()

# Menampilkan matriks
for i in range(R):
    for j in range(C):
        print(matriks[i][j], end = '')
    print()