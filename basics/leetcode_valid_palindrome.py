class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        cleaned_s = ''.join(c for c in s if c.isalnum())
        length = len(cleaned_s)
        first_half = cleaned_s[:length//2]
        second_half = cleaned_s[length//2:]
        second_half = second_half[::-1]
        if(first_half == second_half or first_half == second_half[:-1]):
            return True
        else:
            return False