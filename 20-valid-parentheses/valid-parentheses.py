class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i=='(': stack.append('(')
            if i=='{': stack.append('{')
            if i=='[': stack.append('[')
            if i==')':
                if len(stack)>0 and stack[-1]=='(': stack.pop()
                else:return False
            if i=='}':
                if len(stack)>0 and  stack[-1]=='{': stack.pop()
                else:return False
            if i==']':
                if len(stack)>0 and stack[-1]=='[': stack.pop()
                else:return False
            # print(stack)
        return len(stack)==0
