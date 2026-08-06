class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups={}
        

        for word in strs:
            key = [0]*26
            for ch in word:
                val = ord(ch) - ord("a")
                key[val] += 1

            if tuple(key) in groups:
                groups[tuple(key)].append(word)
            else:
                groups[tuple(key)] = [word]

            
        return list(groups.values())





        