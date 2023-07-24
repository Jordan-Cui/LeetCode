class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        check = nums[0]
        i = 1
        dupe = False
        while i < len(nums):
            if check == nums[i]:
                if dupe == True:
                    nums.pop(i)
                else:
                    dupe = True
                    k += 1
                    i += 1
            else:
                dupe = False
                k += 1
                check = nums[i]
                i += 1
        return(k)
