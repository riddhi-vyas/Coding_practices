nums = [3,2,6,1]
n = len(nums)
for i in range(n):
    min_point = i
    for j in range(i+1,n):
        if nums[j] < nums[min_point]:
           min_point = j
    nums[i], nums[min_point] = nums[min_point], nums[i]
print(nums)
    