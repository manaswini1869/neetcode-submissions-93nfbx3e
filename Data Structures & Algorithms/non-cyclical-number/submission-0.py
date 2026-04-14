class Solution:
    def isHappy(self, n: int) -> bool:
        num = str(n)

        seen = set()

        while num:
            if int(num) == 1:
                return True
            if int(num) in seen:
                return False
            n = 0
            for i in num:
                n += int(i)*int(i)
            seen.add(n)
            num = str(n)