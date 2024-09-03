class Solution:
    def __init__(self):
        pass 

    def reverse_array(self, nums: list[int], k: int) -> None:
        begin = 0
        end = k-1
        while begin < end:
            nums[begin], nums[end] = nums[end], nums[begin]
            begin+=1
            end-=1


def main():
    array1 = [-1,-2,-3,-4,-5]
    k = len(array1)
    object1 = Solution()
    object1.reverse_array(array1, k)
    print(array1)
    
if __name__ == "__main__":
    main()


