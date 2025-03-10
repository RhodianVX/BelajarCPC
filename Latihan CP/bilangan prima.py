angka = [i for i in range(2, 10000)]
bilangan_prima = []
# pointer = 0
# while(pointer <= len(angka)):
#     angka = [x for x in angka if x % angka[pointer] != 0 & x != angka[pointer]]
#     pointer = pointer + 1

# print(angka)

for i in range (len(angka)):
    if(i == 0):
        bilangan_prima.append(angka[i])
    else:
        prima = True
        for j in range(len(bilangan_prima)):
            if(angka[i] % bilangan_prima[j] == 0):
                prima = False
                break
        if(prima == True):
            bilangan_prima.append(angka[i])

T = int(input())
hasil = []

for i in range(T):
    K = int(input())
    for j in range(len(angka)):
        if(j == K - 1):
            hasil.append(angka[j])

for i in range(T):
    print(hasil[i])
