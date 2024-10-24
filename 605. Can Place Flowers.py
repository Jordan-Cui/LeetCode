class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        prev = 0
        flowerbed.append(0)
        count = 0
        for i in range(len(flowerbed) - 1):
            if flowerbed[i] == 0 and prev == 0 and flowerbed[i + 1] == 0:
                count += 1
                prev = 1
            else:
                prev = flowerbed[i]
        return(count >= n)

#Alternate Solution using slicing:
#class Solution:
#    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
#        count = 1
#        i = 0
#        while i < len(flowerbed):
#            if flowerbed[i] != 1 and flowerbed[i-1:i] != [1] and flowerbed[i+1:i+2] != [1]:
#                count += 1
#                i += 2
#            else:
#                i += 1
#        return count > n
