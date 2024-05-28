class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        po = 0
        s = []
        for i in range(len(pushed)):
            s.append(pushed[i])
            while s and popped[po] == s[-1]:
                s.pop()
                po+=1
            
            
        # if po == len(popped)-1: return True
        return s==[]