class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        wealth = []
        for l in range(len(accounts)):
            wealth_of_each = sum(accounts[l])
            wealth.append(wealth_of_each)
        return max(wealth)
