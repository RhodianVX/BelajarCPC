def find_numbers_recursive(random, numberArray, index=0, result=""):
    # Hentikan rekursi jika semua karakter sudah berubah menjadi 'x'
    if all(c == 'x' for c in random):
        return result.strip()  # Hapus spasi berlebih di akhir
    
    # Hentikan jika indeks sudah melewati batas array numberArray
    if index >= len(numberArray):
        return result.strip()
    
    temp_random = list(random)  # Ubah string menjadi list untuk memodifikasi karakter
    word = numberArray[index]  # Ambil kata dari numberArray
    temp_count = temp_random[:]  # Salinan untuk pengecekan
    
    # Periksa apakah semua karakter dalam kata tersedia dalam random
    for char in word:
        if char in temp_count:
            temp_count[temp_count.index(char)] = 'x'  # Gantikan karakter pertama yang cocok dengan 'x'
        else:
            # Jika karakter tidak ditemukan, lanjutkan ke indeks berikutnya
            return find_numbers_recursive(random, numberArray, index + 1, result)
    
    # Jika kata ditemukan, ubah karakter dalam random menjadi 'x' dan ulangi dari index 0
    random = "".join(temp_count)
    result += word + " "  # Tambahkan angka ke hasil
    
    return find_numbers_recursive(random, numberArray, 0, result)  # Restart dari index 0

# Contoh eksekusi
random = "ewtooetzrowonk"
numberArray = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

output = find_numbers_recursive(random, numberArray)
print(output)