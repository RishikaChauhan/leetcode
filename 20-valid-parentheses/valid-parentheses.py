class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in "([{":
                stack.append(char)
            else:
                if not stack:
                    return False
                top = stack[-1]
                if char == ')' and top == '(':
                    stack.pop()
                elif char == '}' and top == '{':
                    stack.pop()
                elif char == ']' and top == '[':
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
