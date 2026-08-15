class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        total = False
        pos = False
        n = len(nums)

        for num in nums :
            total ^= num
            if num > 0 :
                pos = True

        if total > 0:
            return len(nums)

        return n-1 if  pos != False else 0
        