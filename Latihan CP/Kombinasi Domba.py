import math

mod = 1000000007
n = 100
r = 50

fact_n = 1
fact_r = 1

for i in range(n + 1):
    if(i != 0):
        fact_n = fact_n * (i % mod)
        fact_n = fact_n % mod
    
print(fact_n)

for i in range(r + 1):
    if(i != 0):
        fact_r = fact_r * (i % mod)
        fact_r = fact_r % mod

print(fact_r)

hasil = fact_n / ((fact_r * fact_r) % mod)

print(hasil)