class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for string in strs:
            a=len(string)
            s+=str(a)+"#"+string
        
        return s

    def decode(self, s: str) -> List[str]:
        l=[]
        i=0
        while i<len(s):
            j= i 
            length=''
            while s[j] != "#":
                length +=s[j]
                j+=1
                
            j+=1
            l.append(s[j:j+int(length)]) 

            i= j+int(length)
        return l   
            

        
    