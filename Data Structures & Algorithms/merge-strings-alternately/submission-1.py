class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a=min(len(word1),len(word2))
        x=0
        i=0
        ans=""
        while x<a:
            ans+=word1[x]
            ans+=word2[x]
            x+=1
        if len(word1)>len(word2):
            ans+=word1[len(word2):]
        elif len(word2)>len(word1):
            ans+=word2[len(word1):]
        return ans
            




        