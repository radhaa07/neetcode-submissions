class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hm={}
        for i in nums:
            hm[i] = hm.get(i,0)+1
        for i in nums:
            if ((hm.get(i)) > (len(nums)/2)):
                return i 

        