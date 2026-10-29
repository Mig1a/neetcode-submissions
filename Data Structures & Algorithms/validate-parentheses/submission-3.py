class Solution:
    def isValid(self, s: str) -> bool:
        """
        input: str - parathesis
        output: boolean

        process each item in the input to check each opening has a closing in the input
        the open and close bracets have to be in oreder ()(())
        create a stack
        loop through the inputs
            - if the stack is empty and closing comes - False
            - if opening comes add it to the stack
            - if closing pop the last item from the stack and check its a right fit
        return true

        """
        stack = []
        for i in s:
            if i in '})]':
                if len(stack) == 0:
                    return False
                elif i == ')' and stack[-1] != "(":
                    return False
                elif i == '}' and stack[-1] != "{":
                    return False
                elif i == ']' and stack[-1] != "[":
                    return False
                else:
                    stack.pop()
            else:
                stack.append(i)
        return len(stack) == 0
            
        