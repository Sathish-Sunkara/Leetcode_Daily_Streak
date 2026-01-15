class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:

        def consecutive(bars) :
            streak = 1
            ans = 1
            bars = sorted(bars)

            for i in range(len(bars)-1) :
                if bars[i] + 1 == bars[i+1] :
                    streak += 1
                else :
                    ans = max(ans , streak)
                    streak = 1
            ans = max(ans , streak)
            return ans + 1

        return min(consecutive(hBars) , consecutive(vBars)) ** 2

        