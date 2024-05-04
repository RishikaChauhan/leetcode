class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        if flowerbed ==[0]: return True
        if len(flowerbed)>1 and [flowerbed [0],flowerbed[1]]==[0,0]:
            flowerbed[0]=1
            count+=1
        for i in range(1, len(flowerbed)-1):
            if [flowerbed[i-1], flowerbed[i], flowerbed[i+1]]==[0,0,0]:
                flowerbed[i]=1
                count+=1
        if len(flowerbed)>1 and [flowerbed [-2],flowerbed[-1]]==[0,0]:
            flowerbed[-1]=1
            count+=1
        
        return n<=count