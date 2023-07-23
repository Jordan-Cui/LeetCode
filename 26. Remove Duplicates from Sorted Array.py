#in-place solution
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        check = nums[0]
        i = 1
        while i < len(nums):
            if check != nums[i]:
                k += 1
                check = nums[i]
                i += 1
            else:
                nums.pop(i)
        return(k)
#out of place solution
#class Solution:
#    def removeDuplicates(self, nums: List[int]) -> int:
#        k = 1
#        check = nums[0]
#        newNums = [check]
#        for i in nums:
#            if check != i:
#                k += 1
#                check = i
#                newNums.append(check)
#        nums.clear()
#        nums += newNums
#        return(k)
