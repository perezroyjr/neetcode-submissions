class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        x = -1
        s = ''.join(char for char in s if char.isalnum()).lower()
        for char in range(len(s) // 2):
            if s[char] != s[x]:
                return False
            x += -1
        return True
