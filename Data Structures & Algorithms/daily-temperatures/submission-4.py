class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = [0]*(len(temperatures))
        stack = []

        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                i, t = stack.pop()
                result[i] = idx - i
            stack.append([idx, temp])

        


        return result

        # result = []

        # n = len(temperatures)

        # for i in range(n):
        #     curr = 0
        #     for j in range(i+1, n):
        #         curr += 1
        #         if temperatures[j] > temperatures[i]:
        #             break
        #     else:
        #         curr = 0
        #     result.append(curr)
        
        # return result

        


        