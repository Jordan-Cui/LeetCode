class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        count = 0
        target -= 1
        for i in hours:
            if i > target:
                count += 1
        return(count)
