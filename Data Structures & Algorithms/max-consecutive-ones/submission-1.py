class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr = 0
        max_one = 0
        for i in nums:
            if i ==1:
                curr+=1
                max_one = max(curr, max_one)
            else:
                curr=0
        return max_one