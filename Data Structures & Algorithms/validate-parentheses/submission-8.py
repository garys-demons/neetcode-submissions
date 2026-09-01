class Solution:
    def isValid(self, s: str) -> bool:
        b = {')':'(', ']':'[', '}':'{'}
        stack = []
        for i in s:
            if(stack != [] and i in b.keys()):
                if(stack[-1] != b[i]):
                    return False
                stack.pop()
            else:
                stack.append(i)

        return True if stack == [] else False