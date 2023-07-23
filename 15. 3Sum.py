class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        output = []
        for i in range(n - 2):
            j = i + 1
            k = n - 1
            while(j < k):
                if(nums[i] + nums[j] + nums[k]) == 0:
                    temp = [nums[i], nums[j], nums[k]]
                    if temp not in output:
                        output.append(temp)
                    j += 1
                elif (nums[i] + nums[j] + nums[k]) > 0:
                    k -= 1
                else:
                    j += 1
        return(output)

