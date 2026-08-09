class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set(nums)
        for i in range(len(nums)):
            my_set.add(nums[i])
        
        longest = 0
        for num in my_set:
            if num - 1 not in my_set:
                u = num 
                count = 1
                while u+1 in my_set:
                    count += 1
                    u +=1
                longest = max(longest,count)
            
        return longest