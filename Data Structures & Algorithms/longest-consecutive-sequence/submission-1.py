class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for num in nums:
            l=0
            while num+l in numSet:
                l+=1
                longest=max(longest,l)
        return longest