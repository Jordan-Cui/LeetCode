class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        right = [1]
        for i in range(len(nums) - 1):
            left.append(left[i] * nums[i])
        for i in reversed(range(1, len(nums))):
            right.insert(0, right[0] * nums[i])
        for i in range(len(nums)):
            left[i] *= right[i]
        return(left)
