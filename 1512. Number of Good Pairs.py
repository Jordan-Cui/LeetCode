class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        numPairs = {}
        goodPairs = 0
        for i in nums:
            if i in numPairs:
                numPairs[i] += 1
            else:
                numPairs[i] = 1
        for i in numPairs:
            n = numPairs[i] - 1
            goodPairs += int(n * (n + 1) / 2)
        return(goodPairs)
