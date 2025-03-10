def runtuh(papan):
    R = len(papan)
    C = len(papan[0])

    while True:
        baris_penuh = []
        for i in range(R):
            if all(papan[i][j] == '1' for j in range(C)):
                baris_penuh.append(i)

        if not baris_penuh:
            break

        papan_baru = [['0' for _ in range(C)] for _ in range(R)]

        for i in range(R - 1, -1, -1):
            if i not in baris_penuh:
                for j in range(C):
                    for k in range(R - 1, -1, -1):
                        if papan_baru[k][j] == '0':
                            papan_baru[k][j] = papan[i][j]
                            break

        papan = papan_baru

    return papan

R, C = map(int, input().split())
papan = [list(input()) for _ in range(R)]

papan_akhir = runtuh(papan)

for baris in papan_akhir:
    print(''.join(baris))