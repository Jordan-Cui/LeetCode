class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        largestArea = 0
        i = 0
        j = n - 1
        while(i < j):
            if height[i] > height[j]:
                area = height[j] * (j-i)
                j -= 1
            else:
                area = height[i] * (j-i)
                i += 1
            if area > largestArea:
                largestArea = area
        return(largestArea)

        
