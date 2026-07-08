class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = (s.lower())
        s = "".join(s.split())
        news=""
        for i in s:
            if(i in "abcdefghijklmnopqrstuvwxyz" or i in "1234567890"):
                news+=i
        n = news[::-1]
        if news == n:
            return True
        else:
            return False