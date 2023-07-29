class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxWealth = 0
        for i in range(len(accounts)):
            sum = 0
            for j in accounts[i]:
                sum += j
            if sum > maxWealth:
                maxWealth = sum
        return(maxWealth)
