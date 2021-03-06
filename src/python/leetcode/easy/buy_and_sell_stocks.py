# Generated By lexicon-dsa CLI tool.
# Author: Saptak Sengupta(deeps.sengupta@gmail.com)
# Github: https://github.com/saptaksengupta/


class Solution:

    # Complete the demoFunction function below.
    # You should change the name accordinglly.
    def maxProfit(self, prices):
        if prices is None or len(prices) is 0:
            return 0
        priceLength = len(prices)
        buy = prices[0]
        sell = prices[0]
        maxProf = 0
        i = 1
        while i < priceLength:
            if buy > prices[i]:
                buy = prices[i]
                sell = prices[i]
            elif prices[i] > sell:
                sell = prices[i]
            
            maxProf = max(maxProf, abs(sell - buy))
            i += 1
        return maxProf


if __name__ == "__main__":
    stocks = [7,1,5,3,6,4]
    instance = Solution()
    profit = instance.maxProfit(stocks)
    print(profit)
