class Solution:
    def __init__(self) -> None:
          pass
     
    def romanToInt(self, s: str) -> int:
        my_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000, 'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
        num = 0
        last = 0
        count = len(s)-1
        print(f"Initial count: {count}")
        for count in range(len(s)-1,-1,-1):
            val = ''
            print("New loop started.....")
            print(f"count: {count}")
            print(f"Current char: {s[count]}")

            if count < len(s)-1:
                if s[count] == 'I' and s[count+1] == 'V':
                    val = s[count] + s[count+1]
                    print(f"val = {val}")
                    print(f"my_dict[val]: {my_dict[val]}")
                    print(f"last: {last}")
                    num = num - last + my_dict[val] 
                    print(f"IV num: {num}")
                    count -= 1 

                elif s[count] == 'I' and s[count+1] == 'X':
                    val = s[count] + s[count+1]
                    num = num - last + my_dict[val] 
                    print(f"IX num: {num}")
                    count -= 1
    
                elif s[count] == 'X' and s[count+1] == 'L':
                    val = s[count] + s[count+1]
                    num = num - last + my_dict[val] 
                    print(f"XL num: {num}")
                    count -= 1 
                elif s[count] == 'X' and s[count+1] == 'C':
                    val = s[count] + s[count+1]
                    num = num - last + my_dict[val] 
                    print(f"XC num: {num}")
                    count -= 1
                
                elif s[count] == 'C' and s[count+1] == 'D':
                    val = s[count] + s[count+1]
                    num = num - last + my_dict[val] 
                    print(f"CD num: {num}")
                    count -= 1 
                elif s[count] == 'C' and s[count+1] == 'M':
                    val = s[count] + s[count+1]
                    num = num - last + my_dict[val] 
                    print(f"CM num: {num}")
                    count -= 1

            else:
                num += my_dict[s[count]]
                print(f"simple num: {num}")
                last = my_dict[s[count]]
                print(f"simple last: {last}")
                count -= 1

        return num
        
def main():
    obj1 = Solution()
    obj1.romanToInt("MCMXCIV")
    

if __name__ == "__main__":
    main()
