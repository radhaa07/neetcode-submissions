class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m=0
        l=[]
        for i in nums:
            if(i==1):
                l.append(i)
            else:
                l=[]
            m = max(m,len(l))
        return m