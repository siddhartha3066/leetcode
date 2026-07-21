class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp  = prices[0]
        maxp = 0
        for p in prices:
            minp = min(minp,p)
            prof = p - minp
            maxp = max(maxp,prof)
        return maxp 