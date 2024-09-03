# Given a sorted array and k where you need to find pair of elements which produce sum = k
class Solution:
    def two_sum(self, list1, k):
        n = len(list1)
        if n == 0:
            return []
        start = 0
        end = n-1
        result = []
        while start < end:
            my_sum = list1[start] + list1[end]
            if my_sum == k:
                result.append(f"({list1[start]}, {list1[end]})")
                start += 1
                end -= 1
            elif my_sum > k:
                end -= 1
            elif my_sum < k:
                start += 1
        return result
        

def main():
    list1 = [1, 3, 5, 7, 10, 11, 13]
    k = 16
    obj1 = Solution()
    ans = obj1.two_sum(list1, k)
    print(ans)

if __name__ == "__main__":
    main()