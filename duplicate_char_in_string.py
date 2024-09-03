# Given a string S, the task is to print all the duplicate characters with their occurrences in the given string.

# Example:

# Input: S = “geeksforgeeks”
# Output:

# e, count = 4
# g, count = 2
# k, count = 2
# s, count = 2

# Explanation: e,g,k,and s are characters which are occured in string in more than one times.

class Solution:
    def __init__(self) -> None:
        pass

    def find_duplicate(self, data: str):
        if data == "":
            print(None)

        my_dict = {}
        for char in data:
            if char not in my_dict:
                my_dict[char] = 1
            else:
                my_dict[char] += 1
    
        for item in my_dict:
            if my_dict[item] > 1:
                print(f"{item}, count = {my_dict[item]}")
            

def main():
    obj1 = Solution()
    obj1.find_duplicate("helloworld")
    

if __name__ == "__main__":
    main()

