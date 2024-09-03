class Solution:
    def selection_sort(self, my_array):
        n = len(my_array)
        
        for i in range(n):
            min_point = i
            for j in range(i+1,n):
                # if you want to sort in descending, change below condition to >
                if my_array[j] < my_array[min_point]:
                    min_point = j
            my_array[i], my_array[min_point] = my_array[min_point], my_array[i]
        return my_array

        
      
def main():
    list1 = [10, 20, 15, 12, 8]
    obj1 = Solution()
    ans = obj1.selection_sort(list1)
    print(ans)
   
    
if __name__ == "__main__":
    main()
        