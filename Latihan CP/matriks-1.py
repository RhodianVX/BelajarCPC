M, N = map(int, input().split())
matriks = []

#  Memasukkan matriks
for i in range(M):
    baris = list(map(int, input().split()))[:N]
    matriks.append(baris)

print()
# Menampilkan reverse matriks

for i in range(N):
    x = M - 1
    while x >= 0:
        print(matriks[x][i], end = ' ')
        x = x - 1
    print()