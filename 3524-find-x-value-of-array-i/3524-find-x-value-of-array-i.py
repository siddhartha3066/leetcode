class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        result = [0] * k
        prev = [0] * k

        for num in nums:
            curr = [0] * k
            curr[num % k] += 1
            for r in range(k):
                if prev[r]:
                    new_r = (r * (num % k)) % k
                    curr[new_r] += prev[r]

            for r in range(k):
                result[r] += curr[r]

            prev = curr

        return result