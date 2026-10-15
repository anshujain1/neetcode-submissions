class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i=0
        prefix = strs[0]
        for i in range(len(strs)):
            j=0
            for j in range(min(len(strs[i]), len(prefix))):
                if prefix[j] != strs[i][j]:
                    break
                j+=1
            prefix = prefix[:j]
        return prefix 
        

            
        
        