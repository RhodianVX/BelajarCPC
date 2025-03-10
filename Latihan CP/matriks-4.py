# fungsi membentuk matriks N x N terkecil untuk menampung string
def ordo_matriks():
    i = 1
    while i <= 16:
        if(len(teks) <= i * i):
            N = i
            i = 17
            return N
        else:
            i = i + 1

# input teks string
teks = str(input())

# mencari N terkecil untuk membangun matriks
N = ordo_matriks()

# mencari banyak titik yang akan ditambahkan kedalam teks
for i in range((N * N) - len(teks)):
    teks = teks + "."

# mengkonversikan teks menjadi matriks
matriks = []

pointer = 0
for i in range(N):
    temp = []
    for k in range(N):
        temp.append(str("*"))
    if(i % 2 == 0):
        for z in range(N):
            temp[z] = str(teks[pointer])
            pointer += 1
    else:
        for z in range(N):
            temp[(N - 1) - z] = str(teks[pointer])
            pointer += 1
    matriks.append(temp)

# menampilkan matriks
for i in range(N):
    for j in range(N):
        print(matriks[i][j], end = "")
    print()