class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        memo = {}
        def get_max(s,e) :
            if s == e :
                return nums[s]
            if (s,e) in memo :
                return memo[(s,e)]

            start = nums[s] - get_max(s+1 , e)
            end  = nums[e] - get_max(s,e-1)

            memo[(s,e)] = max(start , end)
            return memo[(s,e)]

        return get_max(0, len(nums) - 1) >= 0 