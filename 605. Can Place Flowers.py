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
