# Given an array of N integers where each value represents the number of chocolates in a packet. Each packet can have a variable number of chocolates. 
# There are m students, the task is to distribute chocolate packets such that: 
# Each student gets one packet.
# The difference between the number of chocolates in the packet with maximum chocolates and the packet with minimum chocolates given to the students is minimum.

from bubble_sort import Sorting


class Solution:
    def __init__(self) -> None:
        pass

    def Chocolate_dist(self, nums: list[int], m: int) -> int:
        sort_obj1 = Sorting()
        sorted_nums = sort_obj1.bubble_sort_method(nums)
        n = len(nums)
        min_diff = nums[n-1] - nums[0]
        for i in range(n-m+1):
            if nums[i+m-1] - nums[i] < min_diff:
                min_diff = nums[i+m-1] - nums[i]
        return min_diff          

def main():
    list1 = [7, 3, 2, 4, 9, 12, 56]
    m = 3
    obj1 = Solution()
    result = obj1.Chocolate_dist(list1, m)
    print(f"min difference: {result}")

if __name__ == "__main__":
    main()
