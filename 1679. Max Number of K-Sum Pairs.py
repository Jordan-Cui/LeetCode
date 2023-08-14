class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # a = []
        # count = 0
        # for i in nums:
        #     temp = k - i
        #     try: 
        #         temp2 = a.index(i)
        #         count += 1
        #         a.pop(temp2)
        #     except:
        #         a.append(temp)
        # return(count)
        nums.sort()
        left = 0
        right = len(nums) - 1
        count = 0
        while left < right:
            temp = nums[left] + nums[right]
            if temp > k:
                right -= 1
            elif temp < k:
                left += 1
            else:
                count += 1
                left += 1
                right -= 1
        return(count)
