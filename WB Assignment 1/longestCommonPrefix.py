class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        
        if (strs == [] or "" in strs): return prefix
        
        for char in strs[0]:
            temp = prefix + char
            for string in strs[1:]:
                if (string.startswith(temp)): continue
                else: return prefix
            prefix = temp
            
        return prefix