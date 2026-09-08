class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        a = len(s1)
        b = len(s2)
        if a>b:
            return False
        w = s2[:a]
        hm={}
        hm2={}
        for i in s1:
            hm[i] = hm.get(i,0)+1
        for i in w:
            hm2[i] = hm2.get(i,0)+1
        if hm == hm2:
            return True
        for i in range(a,b):
            old = s2[i-a]
            hm2[old] -=1
            if hm2[old] == 0:
                del hm2[old]
            hm2[s2[i]] = hm2.get(s2[i],0)+1
            if hm==hm2:
                return True
        return False

        
        
        
        