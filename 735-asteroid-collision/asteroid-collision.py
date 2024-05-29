class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []
        for astroid in asteroids:
            # if s==[]: 
            #     s.append(astroid)
            #     continue
            while s and astroid < 0 < s[-1]:
                if abs(s[-1]<abs(astroid)):
                    s.pop()
                    continue
                elif abs(s[-1]==abs(astroid)):
                    s.pop()
                break
                # else:
                #     s.pop()
                    # s.append(astroid)
                # print(s)
            else: s.append(astroid)
        return s