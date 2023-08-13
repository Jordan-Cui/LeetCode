class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        idx = 0
        while i < len(nums):
            if nums[idx] == 0:
                nums.pop(idx)
                nums.append(0)
            else:
                idx += 1
            i += 1
        return(nums)
