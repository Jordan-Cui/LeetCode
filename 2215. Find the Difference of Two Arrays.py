class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        dict1 = {}
        dict2 = {}
        ans = [[], []]
        for i in nums1:
            if not i in dict1:
                dict1[i] = 0
        for i in nums2:
            if not i in dict2:
                dict2[i] = 0
                if not i in dict1:
                    ans[1].append(i)
        for i in dict1:
            if not i in dict2:
                ans[0].append(i)
        return(ans)
