class Solution:
    def isPalindrome(self, s: str) -> bool:

        final_str = "".join(char.lower() for char in s if char.isalnum())
        l = 0
        r = len(final_str)-1
        while l <= r:
            if final_str[l] != final_str[r]:
                return False
            l += 1
            r -= 1


        return True


        