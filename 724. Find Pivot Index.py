class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalSum = sum(nums)
        cumSum = 0
        for i in range(len(nums)):
            if cumSum == totalSum - cumSum - nums[i]:
                return(i)
            cumSum += nums[i]
        return(-1)
