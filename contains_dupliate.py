# Leetcode 217. Contains duplicate - https://leetcode.com/problems/contains-duplicate/description/

class Solution:
    def contains_duplicate(self, nums:list[int]) -> bool:
        my_dictionary = {}
        for i in range(len(nums)):
            if nums[i] not in my_dictionary:
                my_dictionary[nums[i]] = 1
            else:
                return True
        return False
    
def main():
    obj1 = Solution()
    array_1 = [1, 2, 3, 1]
    result_1 = obj1.contains_duplicate(array_1)
    if result_1 is True:
        print(f"Given array {array_1} contains duplicate")
    else:
        print(f"Given array {array_1} does not contain duplicate")

if __name__ == "__main__":
    main()