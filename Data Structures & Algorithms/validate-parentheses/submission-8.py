class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mp={
            ")":"(",
            "}":"{",
            "]":"["
        }

        for i in range(len(s)):
            if s[i] in mp:
                if stack and stack[-1] == mp[s[i]]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
            
        if len(stack)>0:
            return False
        return True
                
    
