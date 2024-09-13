# Leetcode 49. Group Anagrams - https://leetcode.com/problems/group-anagrams/description/

class solution():
    def group_anagram(self, strs: list[str]) -> list[list[str]]:
        my_dict = {}
        for i in strs:
            f = str(sorted(i)) # sort characters from ith ("eat" -> 'a', 'e', 't')
            if f not in my_dict:
                my_dict[f] = []
            my_dict[f].append(i)
        return list(my_dict.values())
    
def main():
    obj1 = solution()
    list1 = ["eat","tea","tan","ate","nat","bat"]
    list2 = [""]
    list3 = ["a"]
    result = obj1.group_anagram(list3)
    print(result)

if __name__ == "__main__":
    main()

# Time comp = O(n * m * log(m)), where n is the number of strings in the input list and m is the average length of each string. 
# This is because for each string, we are sorting it (which takes O(m * log(m)) time) and then checking if the sorted string is already in the dictionary (which takes O(1) time on average). 

# Space comp = O(n * m), as we are storing each string in the dictionary along with its sorted version.
