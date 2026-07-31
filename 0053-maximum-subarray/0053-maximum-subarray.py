class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        csum = nums[0]
        msum = nums[0]
        for x in range(1,len(nums)):
            csum = max(nums[x], csum + nums[x])
            msum = max(msum,csum)
        return msum