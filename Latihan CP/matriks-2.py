def rotasi_90(matriks):
    sementara = []
    for i in range(sementara2):
        baris = []
        x = sementara1 - 1
        while x >= 0:
            baris.append(matriks[x][i])
            x = x - 1
        sementara.append(baris)
    matriks = sementara
    return matriks

def refleksi_horizontal(matriks):
    sementara = []
    for i in range(sementara1):
        index = sementara1 - 1 - i
        baris = []
        for j in range(sementara2):
            baris.append(matriks[index][j])
        sementara.append(baris)
    matriks = sementara
    return matriks

def refleksi_vertikal(matriks):
    sementara = []
    for i in range(sementara1):
        index = sementara2 - 1
        baris = []
        for j in range(sementara2):
            baris.append(matriks[i][index])
            index = index - 1
        sementara.append(baris)
    matriks = sementara
    return matriks

M, N, X = map(int, input().split())
matriks = []
sementara1 = M
sementara2 = N
counter = 0

#  Memasukkan matriks
for i in range(M):
    baris = list(map(int, input().split()))[:N]
    matriks.append(baris)

# memasukan kondisi
for i in range(X):
    rotasi = str(input())

    if(rotasi == "_"):
        matriks = refleksi_horizontal(matriks)
    
    elif(rotasi == "|"):
        matriks = refleksi_vertikal(matriks)

    elif(rotasi == "90"):
        matriks = rotasi_90(matriks)
        counter = counter + 1
        if(counter % 2 == 1):
            sementara1 = N
            sementara2 = M
        else:
            sementara1 = M
            sementara2 = N
    
    elif(rotasi == "180"):
        matriks = rotasi_90(matriks)
        counter = counter + 1
        if(counter % 2 == 1):
            sementara1 = N
            sementara2 = M
        else:
            sementara1 = M
            sementara2 = N

        matriks = rotasi_90(matriks)
        counter = counter + 1
        if(counter % 2 == 1):
            sementara1 = N
            sementara2 = M
        else:
            sementara1 = M
            sementara2 = N

    elif(rotasi == "270"):
        matriks = rotasi_90(matriks)
        counter = counter + 1
        if(counter % 2 == 1):
            sementara1 = N
            sementara2 = M
        else:
            sementara1 = M
            sementara2 = N

        matriks = rotasi_90(matriks)
        counter = counter + 1
        if(counter % 2 == 1):
            sementara1 = N
            sementara2 = M
        else:
            sementara1 = M
            sementara2 = N

        matriks = rotasi_90(matriks)
        counter = counter + 1
        if(counter % 2 == 1):
            sementara1 = N
            sementara2 = M
        else:
            sementara1 = M
            sementara2 = N

print()

# tampil hasil matriks
for i in range(sementara1):
    for j in range(sementara2):
        print(matriks[i][j], end = ' ')
    print()