class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zeroPos = [-1]
        for i in range(len(nums)):
            if nums[i] == 0:
                zeroPos.append(i)
        zeroPos.append(len(nums))
        if len(zeroPos) == 2:
            return len(nums) - 1
        maxLength = 0
        length = 0
        for i in range(1, len(zeroPos) - 1):
            length = zeroPos[i+1] - zeroPos[i-1] - 2
            if length > maxLength:
                maxLength = length
        return maxLength
