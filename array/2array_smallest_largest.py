import sys

class Solution:
    def array_min_max(self, my_array):
        n = len(my_array)
        largest = -sys.maxsize-1
        smallest = sys.maxsize

        for i in range(n):
            if my_array[i] < smallest:
                smallest = my_array[i]
            if my_array[i] > largest:
                largest = my_array[i]
        
        print(f"Smallest: {smallest}")
        print(f"Largest: {largest}")

def main():
    list1 = [10, 20, 15, 12, 8]
    obj1 = Solution()
    obj1.array_min_max(list1)

if __name__ == "__main__":
    main()
        