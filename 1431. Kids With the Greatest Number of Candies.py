class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        mostCandies = max(candies) - 1
        result = []
        for i in candies:
            if i + extraCandies > mostCandies:
                result.append(True)
            else:
                result.append(False)
        return(result)
