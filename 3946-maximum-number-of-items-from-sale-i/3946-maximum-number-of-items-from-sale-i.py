class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        cheapest = float('inf')
        free = [0] * n
        for i in range(n):
            cheapest = min(cheapest, items[i][1])
            for j in range(n):
                if i != j and items[j][0] % items[i][0] == 0:
                    free[i] += 1

        dp = [0] * (budget + 1)

        for i in range(n):
            price = items[i][1]
            profit = free[i] + 1

            for b in range(budget, price - 1, -1):
                dp[b] = max(dp[b], dp[b - price] + profit)

        ans = 0
        for b in range(budget + 1):
            total = dp[b] + (budget - b) // cheapest
            ans = max(ans, total)

        return ans

        