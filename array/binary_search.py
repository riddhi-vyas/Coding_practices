class Solution:
    def binary_search(self, my_array, my_key):
        my_array.sort()
        print(my_array)
        n = len(my_array)
        start = 0
        end = n-1
        mid = (start+end)//2

        while start <= end:
            if my_array[mid] == my_key:
                return mid
            elif my_array[mid] < my_key:
                start = mid + 1
            elif my_array[mid] > my_key:
                end = mid-1
        return -1
      
def main():
    list1 = [10, 20, 15, 12, 8]
    key = 12
    obj1 = Solution()
    ans = obj1.binary_search(list1, key)
    print(f"key {key} has found at position: {ans}")
    
if __name__ == "__main__":
    main()
        