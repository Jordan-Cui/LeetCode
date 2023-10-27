class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        #find distance between zeros, store in arr
        #create sliding window that sums distances, max distance + distance to next zero - 1 should be ans
        zeroDistance = []
        pos = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                zeroDistance.append(i - pos)
                pos = i
        zeroDistance.append(len(nums) - pos)
        if len(zeroDistance) <= k:
            return len(nums)
        maxDistance = 0
        for i in range(k + 1):
            maxDistance += zeroDistance[i]
        maxDistance -= 1
        distance = maxDistance
        for i in range(0, len(zeroDistance) - k - 1):
            distance -= zeroDistance[i]
            distance += zeroDistance[i + k + 1]
            if distance > maxDistance:
                maxDistance = distance
        return maxDistance
