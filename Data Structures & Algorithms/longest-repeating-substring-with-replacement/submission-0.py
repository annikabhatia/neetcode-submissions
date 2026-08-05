class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #if there is a way to keep a track of all of the letters present in the string, we should do that. we ideally will want to keep an eye out for the most frequent char.
        #window should be of size k, we continously compare and replace with other letter and count the number of letters in that string
        #when it exceeds the current max, set the new max = to that variable

        count = {}
        res = 0
        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
