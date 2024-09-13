#Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
#The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

class Solution:
    def product_except_self(self, nums: list[int]) -> list[int]:
        n = len(nums)
        if not n:
            return []
        left_array = [1]*n
        right_array = [1]*n

        # update left array
        for i in range(1, n):
            left_array[i] = left_array[i-1] * nums[i-1]
        #update right array
        for j in range(n-2, -1, -1):
            right_array[j] = right_array[j+1] * nums[j+1]

        answer = [1]*n
        for k in range(n):
            answer[k] = left_array[k] * right_array[k]
        
        return answer
    
def main():
    obj1 = Solution()
    list1 = [1,2,3,4]
    list2 = [-1,1,0,-3,3]
    result = obj1.product_except_self(list2)
    print(f"answer = {result}")

if __name__ == "__main__":
    main()