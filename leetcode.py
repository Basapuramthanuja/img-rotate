class Solution:
    def longestPalindrome(self, s: str) -> str:
        p=''
        for i in range(len(s)):
            p1=self.getpalindrome(s,i,i)
            p2=self.getpalindrome(s,i,i+1)
            p=max([p,p1,p2],key=len)
        return p
    def getpalindrome(self,s:str,l:int,r:int) -> str:
        while l>=0 and r<len(s) and s[l]==s[r]:
            l-=1
            r+=1
        return s[l+1:r]