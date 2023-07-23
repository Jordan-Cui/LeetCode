class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        numsChange = []
        for i in range(0, len(nums)):
            numsChange.append(nums[nums[i]])
        return(numsChange)
