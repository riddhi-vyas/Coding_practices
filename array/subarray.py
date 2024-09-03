
# Print subarray from given array
class Solution:
    def find_subarray(self, list1):
        my_array = list1
        n = len(my_array)
        if n == 0:
            return []
        result = []
        for i in range(n):
            j = i
            for j in range(i, n):
                subarray = my_array[i:j+1]
                result.append(subarray)
        return result


def main():
    list1 = [1, 2, 3]
    obj1 = Solution()
    ans = obj1.find_subarray(list1)
    print(ans)

if __name__ == "__main__":
    main()