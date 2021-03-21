nums = []
quantity_pairs = int (input())
        
for i in range(quantity_pairs):
    num = list(map(int, input().split()))
    nums.append(num)


for i in range(quantity_pairs-1):
    for j in range(quantity_pairs-i-1):
        key=nums[j]
        next_key = nums[j+1]

        if (key[1] > next_key[1]) or (key[1] == next_key[1] and key[0] <= next_key[0]):
            nums[j], nums[j+1] = next_key, key

print(' ')
for now in nums[::-1]:
    print(*now)