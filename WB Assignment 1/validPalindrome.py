class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for char in s:
            if char.isalnum():
                newStr += char.lower()
        revStr = newStr[::-1]
        return newStr == revStr