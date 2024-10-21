# 1.Two sum leetcode - https://leetcode.com/problems/two-sum/description/
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

class Solution:
    def two_sum(self, nums:list[int], target:int) -> list[int]:
        my_dictionary = {}
        for i in range(len(nums)):
            if target - nums[i] not in my_dictionary:
                my_dictionary[nums[i]] = i
            else:
                return (i, my_dictionary[target - nums[i]])
        return my_dictionary
    
def main():
    obj1 = Solution()
    array_1 = [2,7,11,15]
    target_1 = 9

    array_2 = [3,2,4]
    target_2 = 6

    result_1 = obj1.two_sum(array_1, target_1)
    print(f"indices for two elements from given array: {result_1}")

    result_2 = obj1.two_sum(array_2, target_2)
    print(f"indices for two elements from given array: {result_2}")

if __name__ == "__main__":
    main()