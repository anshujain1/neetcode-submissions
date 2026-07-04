class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups={}
        
        for word in strs:
            count=[0]*26
            
            for ch in word:
                diff= ord(ch) - ord("a")
                count[diff] +=1
            if tuple(count) in groups.keys():
                groups[tuple(count)].append(word)
            else:
                value=[]
                value.append(word)
                groups[tuple(count)] = value
            
        return list(groups.values())