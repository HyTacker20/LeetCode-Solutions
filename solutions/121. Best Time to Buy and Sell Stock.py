from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy_price = prices[0]

        for i in range(1, len(prices)):
            if prices[i] < buy_price:
                buy_price = prices[i]

            profit = prices[i] - buy_price
            if profit > max_profit:
                max_profit = profit

        return max_profit



if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProfit([7,1,5,3,6,4]))
    print(solution.maxProfit([7,6,4,3,1]))
    print(solution.maxProfit([5,10,1,7]))
