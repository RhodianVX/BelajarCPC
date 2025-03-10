import math

bilangan = int(input())

faktorisasiPrima = []
i = 2
while (i <= bilangan):
    if (bilangan % i == 0):
        bilangan = bilangan / i
        faktorisasiPrima.append(i)
    else:
        i = i + 1

# proses membentuk string
from collections import Counter

def faktorisasi_to_string(faktor_array):
    # Hitung frekuensi setiap angka dalam array
    faktor_count = Counter(faktor_array)
    
    # Buat string untuk faktorisasi
    faktor_str = []
    for faktor, count in faktor_count.items():
        if count > 1:
            faktor_str.append(f"{faktor}^{count}")  # Format 3^2
        else:
            faktor_str.append(str(faktor))  # Format 7, 11, dll
    
    # Gabungkan faktor-faktor dengan 'x'
    return ' x '.join(faktor_str)

hasil_string = faktorisasi_to_string(faktorisasiPrima)
print(hasil_string)