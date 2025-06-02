class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        d = {}
        for i, c in enumerate(order):
            d[c] = i

        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]

            for j in range(len(w1)):
                if j ==len(w2): return False
            
                if w1[j] != w2[j]:
                    if d[w1[j]]>d[w2[j]]: 
                        return False
                    break
        return True



        # def cal_num(word, order, p):
        #     if len(word)==0: return p
        #     i = 0
            
        #     while i<len(word):
        #         char = word[0]
        #         p = order.index(char)
        #         word = word[1:]
        #         p = p*10 + cal_num(word, order, p)
        #     return p
        
        
        
        
        
        
        
        
        # indexed_list = list(zip(range(len(order)), list(order)))
        # l = []
        # for word in words:
        #     l.append(cal_num(word, order, p=0))
        # print(l)
        # if l==l.sort():
        #     return True
        # return False
        # return 0