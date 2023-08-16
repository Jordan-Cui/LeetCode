class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest = 0
        cumSum = 0
        for i in gain:
            cumSum += i
            if cumSum > highest:
                highest = cumSum
        return(highest)
