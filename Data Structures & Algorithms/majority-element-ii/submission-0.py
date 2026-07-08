class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hm={}
        ans=[]
        n = len(nums)
        for i in nums:
            hm[i] = hm.get(i,0)+1
        for i in hm:
            if hm.get(i) > n/3:
                ans.append(i)
        return ans


        