import sys
# max_size = sys.maxsize
# min_size = -sys.maxsize - 1

class Solution:
    def __init__(self) -> None:
        pass

    def maxSubArray(self, nums: list[int]) -> int:
        cur_sum = 0
        max_sum = -sys.maxsize - 1   # a number smaller than all others
        n = len(nums)
        for i in range(n):
            cur_sum = cur_sum + nums[i]
            if max_sum < cur_sum:
                max_sum = cur_sum
            if cur_sum < 0:
                cur_sum = 0
        return max_sum

def main():
    list1 = [-2,1,-3,4,-1,2,1,-5,4]
    obj1 = Solution()
    result = obj1.maxSubArray(list1)
    print(result)

if __name__ == "__main__":
    main()
