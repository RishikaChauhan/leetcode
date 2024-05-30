class FreqStack:

    def __init__(self):
        self.stack =defaultdict(list)
        self.freq = defaultdict(int)
        self.maxfreq = 0

    def push(self, val: int) -> None:
        self.freq[val] +=1  
        self.maxfreq = max(self.maxfreq, self.freq[val])
        self.stack[self.freq[val]].append(val)

    def pop(self) -> int:
        val = self.stack[self.maxfreq].pop()
        self.freq[val]-=1
        if not self.stack[self.maxfreq]:
            self.maxfreq -=1

        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()