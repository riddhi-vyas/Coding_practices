class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 0 : # Corner case 
            return ""

        def prefix_find(s1, s2):
            min_len = min(len(s1), len(s2))
            new_prefix = ""
            for iterate in range(min_len):
                if s1[iterate] == s2[iterate]:
                    new_prefix += s1[iterate]
                else:
                    break

            return new_prefix

        prefix = strs[0]
        for item in strs[1:]:
            prefix = prefix_find(prefix, item) 
        
        return prefix
