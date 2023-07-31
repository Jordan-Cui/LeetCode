class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        numsCopy = nums.copy()
        nums.sort()
        for i in range(len(nums)):
            numsCopy[i] = nums.index(numsCopy[i])
        return(numsCopy)
