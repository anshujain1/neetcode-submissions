class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = {}
        left = 0
        if len(s1) > len(s2):
            return False
        for i in s1:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        # hashmap is made upto here 
        # now first window 
        for i in range(0,len(s1)):
            if s2[i] in freq:
                freq[s2[i]] -= 1
            if all(values == 0 for values in freq.values()):
                return True
        
        for i in range( len(s1),len(s2)):
            if s2[i] in freq:
                freq[s2[i]] -= 1
            if s2[left] in freq:
                freq[s2[left]] += 1
            left += 1
            if all(values == 0 for values in freq.values()):
                return True
        
        return False
            


                
                    

