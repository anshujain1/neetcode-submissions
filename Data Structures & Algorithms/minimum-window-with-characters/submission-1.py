class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)< len(t):
            return ""
        need = {}
        left = 0
        right = 0
        for c in t:
            need[c] = need.get(c,0) + 1
        
        window = {}
        required = len(need)
        have = 0
        result = ""
        result_len = float("inf")
        
        for right in range(len(s)):
            c = s[right]

            if c in need:
                window[c] = window.get(c,0)+1

                if window[c] == need[c]:
                    have += 1
            
            while have == required:
                window_len = right - left+1 

                if window_len < result_len:
                    result = s[left:right + 1]
                    result_len = window_len
                
                left_char = s[left]

                if left_char in need:
                    window[left_char] -= 1

                    if window[left_char] < need[left_char]:
                        have -= 1
                    
                left +=1

            
        return result

            
