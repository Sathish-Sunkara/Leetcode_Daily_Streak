class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:

        def dfs(path) :
            if len(path) == n :
                if path not in nums :
                    ans.append(path) 
                    return
                else :
                    return 


            dfs(path + "0")
            if ans :
                return
            dfs(path + "1")
            if ans :
                return
        ans = []
        n = len(nums)
        dfs("")

        return ans[0]

         