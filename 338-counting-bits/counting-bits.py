class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            bn = bin(i)[2:]
            # print(bn.
            res.append(bn.count("1"))
            # print(bn, type(bin(n)))
        return res