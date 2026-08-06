class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for i in operations:
            if(i == 'C'):
                stack.pop()
            elif(i == '+'):
                x = stack[-1] + stack[-2]
                stack.append(x)
            elif(i == 'D'):
                stack.append(stack[-1] * 2)
            else:
                stack.append(int(i))

        score = 0
        for i in stack:
            score += i

        return score
