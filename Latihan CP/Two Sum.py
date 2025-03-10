nums = [2,4,11,3]
target = 6

ketemu = False
hasil = 0

# solusi 1
# pointer = 0
# x = pointer + 1

# while (ketemu != True):
#     if(pointer < len(nums) - 1):
#         if(nums[pointer] + nums[x] == target):
#             ketemu = True
#             hasil = [pointer, x]
#         elif(x < len(nums) - 1):
#             x = x + 1
#         else:
#             pointer = pointer + 1
#             x = pointer + 1
# print(hasil)

dict = {}

for i in range(len(nums)):
    if(target - nums[i] not in dict.keys()):
        dict.update({target - nums[i] : i})
        print(dict)
    if (nums[i] in dict):
        hasil = [dict[nums[i]], i]

print(hasil)