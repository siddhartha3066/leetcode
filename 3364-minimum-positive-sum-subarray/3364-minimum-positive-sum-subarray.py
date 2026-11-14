class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        ans = float('inf')

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                total = sum(nums[i:j+1])
                length = j - i + 1

                if length >= l and length <= r and total > 0:
                    ans = min(ans, total)

        if ans == float('inf'):
            return -1

        return ans

        