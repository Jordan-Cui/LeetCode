class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        one = nums[0]
        two = nums[1]
        three = nums[len(nums) - 1]
        for i in range(1, len(nums)):
            if one < two and two < three:
                return True
            if one == two:
                if i == len(nums) - 1:
                    return False
                two = nums[i + 1]
            if one > nums[i]:
                one = nums[i]
                three = nums[len(nums) - 1]
            elif one != nums[i] and two > nums[i]:
                two = nums[i]
                three = nums[len(nums) - 1]
            elif two != nums[i] and nums[i] > three:
                three = nums[i]
        return False
