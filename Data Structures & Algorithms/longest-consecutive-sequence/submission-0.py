class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        

        for n in nums:
            #if this is NOT true (meaning n - 1 exists), then n is NOT the start of the sequence 
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                #updating longest throughout going through the whole nums
                longest = max(length, longest)
        return longest

        