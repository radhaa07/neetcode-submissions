class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        freq = {}
        max_f = 0
        ans = 0
        for i in range(len(s)):
            freq[s[i]] = freq.get(s[i],0)+1
            max_f = max(max_f,freq[s[i]])
            win_l = i-left+1
            replace = win_l - max_f 
            while replace > k:
                freq[s[left]]-=1
                left+=1
                win_l = i-left+1
                replace = win_l - max_f
            ans = max(ans, win_l)
        return ans


        