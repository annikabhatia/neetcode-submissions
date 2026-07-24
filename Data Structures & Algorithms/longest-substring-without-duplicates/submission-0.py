class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #create a hash map formatted like: [char: # of times that char appeared]
        #have a result string = 0, and once we reach a char that has been repeated it can reset to 0
        #have a for loop that runs till the end of the 's' string
        #return the len(res)

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
            

        

