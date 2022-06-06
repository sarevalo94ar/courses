def find_max(nums):
    max_num = float("-inf")  # smaller than all other numbers
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num


numsp = [4, 78, 9, 84]
print(find_max(numsp))
