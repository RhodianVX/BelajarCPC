angka = [i for i in range(2, 1000000)]
pointer = 0
bilangan_prima = [angka[pointer]]

while pointer <= len(angka):
    sementara = [i for i in range(2, 1000000) if i % bilangan_prima[pointer] == 0]
    angka = sorted(list(set(angka).difference(set(sementara))))
    bilangan_prima.append(angka[pointer])
    pointer = pointer + 1

print(bilangan_prima)