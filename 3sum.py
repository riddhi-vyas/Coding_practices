# 15. 3Sum: Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#Notice that the solution set must not contain duplicate triplets.

# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

# Example 2:
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.

# Example 3:
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.


class Solution:
    def three_sum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        answer = []

        # Approach: I will make i steady and other pointers (j, k) will be moving (two pointer approach)       
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]: # to skip duplicates of i
                continue
            j = i+1
            k = n-1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    answer.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                    while j < k and nums[j] == nums[j-1]: # to skip duplicates of j
                        j += 1
                    
                    while j < k and nums[k] == nums[k+1]: # to skip duplicates of k
                        k -= 1
        return answer

def main():
    obj1 = Solution()
    list1 = [-1,0,1,2,-1,-4]
    list2 = [0,1,1]
    list3 = [0,0,0]
    result = obj1.three_sum(list1)
    print(f"three sum result = {result}")

if __name__ == "__main__":
    main()
                    
