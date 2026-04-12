class Solution:
    def isPalindrome(self, s: str) -> bool:

        # new_s = "".join(ch.lower() for ch in s if ch.isalnum())
        # if not new_s:
        #     return True
        n = len(s)
        left, right = 0, n-1
        while left <= right:
            while left < right and not s[left].isalnum():
                left += 1
            while right > left and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
            
        return True



        