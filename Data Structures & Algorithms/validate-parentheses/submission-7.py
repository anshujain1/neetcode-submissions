class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        freq ={
            ")":"(",
            "]":'[',
            "}":"{"  
        }

        for i in range(len(s)):
            if s[i] in freq:
                if len(stack)!= 0 and stack[-1] == freq[s[i]]:
                    stack.pop(-1)
                else:
                    return False
            else:
                stack.append(s[i])
        
        if len(stack) == 0:
            return True
        return False
        
