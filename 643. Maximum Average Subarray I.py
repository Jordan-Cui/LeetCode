class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        numsum = 0
        for i in range(k):
            numsum += nums[i]
        maxAvg = numsum
        for i in range(k, len(nums)):
            numsum = numsum - nums[i - k] + nums[i]
            if maxAvg < numsum:
                maxAvg = numsum
        return(maxAvg / k)
        
