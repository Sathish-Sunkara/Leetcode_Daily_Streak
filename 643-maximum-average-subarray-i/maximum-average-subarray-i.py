class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        ans = -float("inf")
        avg = 0
        n = len(nums)
        l = 0

        if k > n :
            return sum(nums)/len(nums)

        if n ==1 :
            return float(nums[0])


        for r in range(n) :
            avg += nums[r]/k

            if(r-l+1) == k :
                ans = max(ans , avg)

            if (r-l+1) > k :
                avg -= (nums[l]/k)
                l += 1
                ans = max(ans , avg)

        print(avg)
        if r-l+1 == k :
            ans = max(ans , avg)
            

        return ans
            

            

             

        