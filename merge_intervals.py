# Leetcode 56 Merge intervals - https://leetcode.com/problems/merge-intervals/description/
# Hint Note: answer[-1] refers to the last row
# answer[-1][1] refers to the second element of the last row i.e, if row is [1,2] -> refer 2 

class Solution():
    def merge_intervals(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        n = len(intervals)
        answer = []
        for i in range(n):
            # if current interval does not lie in the previous interval
            if not answer or intervals[i][0] > answer[-1][1]:
                answer.append(intervals[i])
            else: # it current interval lies in the previous interval
                answer[-1][1] = max(answer[-1][1], intervals[i][1])
        return answer
    
def main():
    obj1 = Solution()
    list1 = [[1,3],[2,6],[8,10],[15,18]]
    list2 = [[1,4],[4,5]]
    result = obj1.merge_intervals(list2)
    print(f"Merged interval = {result}")

if __name__ == "__main__":
    main()