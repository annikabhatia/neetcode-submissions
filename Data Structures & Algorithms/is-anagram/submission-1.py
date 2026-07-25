class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seenT = dict()
        seenS = dict()

        if len(s) != len(t):
            return False
        
        for index,val in enumerate(s):
            seenS[val] = seenS.get(val, 0) + 1
        
        for index,val in enumerate(t):
            seenT[val] = seenT.get(val, 0) + 1
        
        return seenT == seenS