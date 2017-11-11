#122


# Time:  O(n)
# Space: O(1)


# Say you have an array for which the ith element 
# is the price of a given stock on day i.
# Design an algorithm to find the maximum profit.
# You may complete as many transactions as you like
# (ie, buy one and sell one share of the stock multiple times).
# However, you may not engage in multiple transactions at the same time 
# (ie, you must sell the stock before you buy again).


class greedySol():
    def bestTimeBuySellStock(self,prices):
        max_profit=0
        for day in range(len(prices)-1):
            max_profit+=max(0,prices[day+1]-prices[day])
        return max_profit
