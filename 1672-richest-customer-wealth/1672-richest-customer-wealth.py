class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        if not len(accounts):
            return 0
        wealthiest = 0
        for i in range(len(accounts)):
            customerMoney = 0
            for j in range(len(accounts[0])):
                customerMoney += accounts[i][j]
            wealthiest = max(wealthiest, customerMoney)
        return wealthiest