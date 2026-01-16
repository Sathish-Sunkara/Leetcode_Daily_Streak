class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        hFences.extend([1,m])
        vFences.extend([1,n])
        ans = 0
        dist = set()
        mod = 10 ** 9 + 7

        for i in range(len(hFences)) :
            for j in range(i+1 , len(hFences)) :
                dist.add(abs(hFences[i] - hFences[j]))

        for i in range(len(vFences)) :
                for j in range(i+1 , len(vFences)) :
                    val = abs(vFences[i] - vFences[j])
                    if val in dist :
                        ans = max(ans , val**2)
        if ans == 0 :
            return -1
        return ans % mod
        


            
        