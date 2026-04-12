class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        n = len(speed)

        pos_speed = [(position[i], speed[i]) for i in range(n)]

        pos_speed = sorted(pos_speed, reverse=True)

        stack = []
        
        for p, s in pos_speed:
            stack.append((target - p)/s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)





        