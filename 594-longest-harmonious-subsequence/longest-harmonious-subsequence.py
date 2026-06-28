class Solution:
    def findLHS(self, nums: List[int]) -> int:

        # using swt
        nums.sort()

        print(nums)

        l , r = 0 , 0
        ans = 0
        mini , maxi = nums[0] , nums[0]
        for r in range(len(nums)) :
            mini = min(mini , nums[r])
            maxi = max(maxi , nums[r])
            

            while abs(maxi-mini) > 1 :
                maxi = max(maxi , nums[r])
                l += 1
                mini = nums[l]
                

            if abs(maxi - mini) == 1 :
                ans = max(ans , r-l+1)

        return ans







        