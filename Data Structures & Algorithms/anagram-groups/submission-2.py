class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups={}
        
        for word in strs:
            k = sorted(word)
            s = "".join(k)
            if s in groups.keys():
                groups[s].append(word)
            else:
                groups[s] = [word]
            
        return list(groups.values())