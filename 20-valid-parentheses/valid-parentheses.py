class Solution:
    def isValid(self, s: str) -> bool:
        while ('{}' in s) or ('[]' in s) or ('()' in s):
            s = s.replace("{}", "").replace("[]","").replace("()","")
        return s==""


        stack = []
        for i in s:
            p = stack[-1]
            if i == '}' and p == '{':
                stack.pop()
            if i == ')' and p == '(':
                stack.pop()
            if i == ']' and p == '[':
                stack.pop()
            else:
                stack.append(i)
        return stack==[]