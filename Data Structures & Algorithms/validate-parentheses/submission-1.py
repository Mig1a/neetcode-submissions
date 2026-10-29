class Solution:
    def isValid(self, s: str) -> bool:
        cont = {')':'(','}':'{',']':'['}
        stack = []
        for i in s:
            if i in ')}]' and stack and stack[-1] == cont[i]:
                stack.pop()
            elif i in '({[':
                stack.append(i)
            else:
                return False
        return len(stack) == 0

        