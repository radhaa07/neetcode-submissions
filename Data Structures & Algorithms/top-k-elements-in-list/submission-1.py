class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums)+1)]#bucket is created for applying bucket sort
        hm={}
        for i in nums:
            hm[i] = hm.get(i,0)+1 # this will create a hashmap containing the element in array and its count. eg. {1:1,2:2,3:3}
        for value,count in hm.items():
            bucket[count].append(value)#here comes the main part where the element is stored in buckets according to its occurence. For eg. if element 3 is occured 3 times then element 3 will be stored at index 3 of bucket list
        ans=[]
        for i in range(len(bucket)-1,0,-1):
            for num in bucket[i]:# we will traverse the values at each index of the bucket list
                ans.append(num)
                if len(ans) == k:
                    return ans


        