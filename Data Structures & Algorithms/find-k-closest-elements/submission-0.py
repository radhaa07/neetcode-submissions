class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res=[]
        for i in range(len(arr)):
            if len(res) == k:
                if abs(x-arr[i]) < abs(x-arr[i-k]):
                    res.remove(arr[i-k])
                    res.append(arr[i])
            else:
                res.append(arr[i])
        return res