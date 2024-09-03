class Solution:
    def insertion_sort(self, my_array):
        n = len(my_array)
        for i in range(n):
            j = i
            while j>0 and my_array[j-1] > my_array[j]:
                my_array[j-1], my_array[j] = my_array[j], my_array[j-1]
                j -= 1
        return my_array


def main():
    list1 = [5, 3, 4, 3, 1, 2]
    obj1 = Solution()
    ans = obj1.insertion_sort(list1)
    print(ans)

if __name__ == "__main__":
    main()

# Time comp: O(n^2)
# Space comp: O(1)