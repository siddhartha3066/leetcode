class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        low = min(nums)
        high = max(nums)
        s = set(nums)
        ans = []
        for n in range(low,high+1):
            if n not in s:
                ans.append(n)
        
        return ans
            