class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        #have to check if the lengths are equal 
        if len(s) != len(t):
            return False

        countS = {}
        countT = {}

        for index in range(len(s)):
            #s[index] = char in s
            countS[s[index]] = countS.get(s[index], 0) + 1
            countT[t[index]] = countT.get(t[index], 0) + 1
        return countS == countT