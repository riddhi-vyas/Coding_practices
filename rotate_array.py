# Leet code Problem: Rotate Array
# Given an integer array nums, rotate the array to the right by k steps, 
# where k is non-negative.

nums = [2,4,5,6,7]
k = 1

nums_dict = {}

for i in range(len(nums)):
    next_index = (i+k) % len(nums)
    nums_dict[nums[i]] = nums.index(nums[next_index])
print(nums_dict)
for key, value in nums_dict.items():
    nums[value] = key