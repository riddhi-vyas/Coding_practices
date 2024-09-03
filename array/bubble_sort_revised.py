class Solution:
    def bubble_sort(self, my_array):
        n = len(my_array)
        if n == 0:
            return []
        
        # Push n-1 elements to the end: loop through n-1 elements
        for itr in range(n-1):
            # pairwise swap in unsorted array
            for i in range(n - 1 - itr):
                if my_array[i] > my_array[i+1]:
                    my_array[i], my_array[i+1] = my_array[i+1], my_array[i]
        
        return my_array


def main():
    list1 = [5, 4, 3, 2, 1]
    obj1 = Solution()
    ans = obj1.bubble_sort(list1)
    print(ans)

if __name__ == "__main__":
    main()

# Time comp: O(n^2)
# Space comp: O(1)