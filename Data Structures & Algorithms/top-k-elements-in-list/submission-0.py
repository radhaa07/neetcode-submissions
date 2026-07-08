class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums)+1)]
        hm={}
        for i in nums:
            hm[i] = hm.get(i,0)+1
        for value,count in hm.items():
            bucket[count].append(value)
        ans=[]
        for i in range(len(bucket)-1,0,-1):
            for num in bucket[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans


        