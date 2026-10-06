class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        combined_arr = []

        for pos, sp in zip(position, speed):

            combined_arr.append([pos, sp])

        combined_arr.sort(reverse=True)

        stack = []

        for p, s in combined_arr:
            stack.append(((target-p)/ s))
            if (len(stack) >= 2) and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)

        