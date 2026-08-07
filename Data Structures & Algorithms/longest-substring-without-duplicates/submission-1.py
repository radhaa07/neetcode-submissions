class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        w=""
        m=0
        for i in s:
            if i in w:
                w=w[w.index(i)+1:]
            w+=i
            m=max(len(w),m)
        return m
        
        