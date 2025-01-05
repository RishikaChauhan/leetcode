class Solution:
    def evalRPN(self, p: List[str]) -> int:
        s = []
        for i in p:
            if i =="+":
                a = s.pop()
                b = s.pop()
                new = int(a) + int(b)
                s.append(new)
                # print(s, "here")
            elif i =="-":
                a = s.pop()
                b = s.pop()
                new = int(b) - int(a)
                s.append(new)
            elif i =="*":
                a = s.pop()
                b = s.pop()
                new = int(a) * int(b)
                s.append(new)
            elif i =="/":
                a = s.pop()
                b = s.pop()
                new = int(int(b) / int(a))
                s.append(new)
            else: s.append(int(i))
            # print(s)

        return s[0]