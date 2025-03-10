# array = []

# def GrowUpNumber(x):
#     while (x > -1):
#         array.append(x)
#         x = x - 1
#     print(array)


# GrowUpNumber(5)

def high_and_low(numbers):
    # proses memecah string menjadi array
    array = numbers.split()
 
    # proses mengubah string menjadi int    
    for i in range(len(array)):
        array[i] = int(array[i])

    # proses mencari nilai terkecil dan terbesar
    smallest = array[0]
    highest = array[0]             
    for i in range(len(array)):
        if (smallest > array[i]):
            smallest = array[i]
        if (highest < array[i]):
            highest = array[i]
    
    # mengembalikan kembali menjadi string nilai terkecil dan terbesar
    numbers = ""
    numbers = numbers + str(highest) + " " + str(smallest)
    return numbers

numbers = "1 2 23 -4 5"
high_and_low(numbers)