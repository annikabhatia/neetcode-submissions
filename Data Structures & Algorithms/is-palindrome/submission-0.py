class Solution:
    def isPalindrome(self, s: str) -> bool:
        #takes care of the: "case-insensitive and ignores all non-alphanumeric characters."
        cleaned_s = "".join(char.lower() for char in s if char.isalnum())

        reversed_string = reversed(cleaned_s)
        reversed_text = "".join(reversed_string)

        return reversed_text == cleaned_s