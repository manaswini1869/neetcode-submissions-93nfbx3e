class Solution:
    def isPalindrome(self, s: str) -> bool:

        new_s = "".join(ch.lower() for ch in s if ch.isalpha())

        n = len(new_s)
        print(new_s)
        left, right = 0, n-1
        while left <= right:
            if new_s[left] != new_s[right]:
                return False
            left += 1
            right -= 1
        return True



        