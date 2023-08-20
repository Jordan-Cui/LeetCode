class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost) + 1
        costToReach = [0] * n
        for i in range(2, n):
            costToReach[i] += min(costToReach[i - 2] + cost[i - 2], costToReach[i - 1] + cost[i - 1])
        return(costToReach[n - 1])
