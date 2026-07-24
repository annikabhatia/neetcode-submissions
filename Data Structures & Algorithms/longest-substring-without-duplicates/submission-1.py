class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #create a hash set so that as we iterate through the string, we can compare back to the hash set and see if there is a duplicate
        #left pointer so we can shrink the window if we find a duplicate
        #right pointer keeps moving forward
        #have a for loop that runs till the end of the 's' string
        #have a count variable that calculates the longest substring with no repeating chars

        chars = set() #char: count
        left = 0
        result = 0
        
        for right in range(len(s)): #right is continously moving forward, so we just iterate it through for loop
            while s[right] in chars: #this is when we reach a duplicate
                chars.remove(s[left])
                left+=1
            chars.add(s[right])
            result = max(result, right - left + 1) #number of chars that return largets non-dupe string
        return result
            

        

