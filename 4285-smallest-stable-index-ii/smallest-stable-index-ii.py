class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        mini = [0] * n
        maxi = [0] * n

        maxi[0] = nums[0]
        mini[-1] = nums[-1]


        for i in range(1,n) :
            maxi[i] = max(maxi[i-1] , nums[i])

        for i in range(n-2,-1,-1) :
            mini[i] = min(mini[i+1] , nums[i])

        # print(maxi)
        # print(mini)
        cnt = -99

        for i in range(n) :
            if maxi[i] - mini[i] <= k :
                cnt = i
                break
                

        return cnt if cnt != -99 else -1

        
        