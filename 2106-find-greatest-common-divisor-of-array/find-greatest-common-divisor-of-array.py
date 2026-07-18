class Solution:
    def findGCD(self, nums: List[int]) -> int:

        from math import gcd 

        nums.sort()
        a , b = nums[0] , nums[-1]
        return gcd(a,b)
        