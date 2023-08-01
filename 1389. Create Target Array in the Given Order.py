class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        numsCopy = []
        for i in range(len(nums)):
            numsCopy.insert(index[i], nums[i])
        return(numsCopy)
