''' question: You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0'''
class Solution(object):
    def maxProfit(self, prices):
        profit = 0
        for fix_num in range(-1,-len(prices),-1):
            min_num = min(prices[:fix_num])
            if profit < (prices[fix_num] - min_num):
                profit = prices[fix_num] - min_num
        return profit
array_object = Solution()
print(array_object.maxProfit([7,1,5,3,6,4])) 

