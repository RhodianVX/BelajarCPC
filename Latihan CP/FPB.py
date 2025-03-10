import math

pecahan1 = list(map(int, input().split()))[:2]
pecahan2 = list(map(int, input().split()))[:2]
hasil = []

fpb = math.gcd(pecahan1[1], pecahan2[1])

hasil.append(int((pecahan1[0] * pecahan2[1] + pecahan2[0] * pecahan1[1]) / fpb))
hasil.append(int((pecahan1[1] * pecahan2[1]) / fpb))

for i in range (len(hasil)):
    print(hasil[i], end=" ")