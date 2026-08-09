class Solution:
    def stoneGameII(self, piles: List[int]) -> int:

        def get_max(i , M) :
            if i >= n :
                return 0
            if (i,M) in memo :
                return memo[(i,M)]

            best = 0


            for x in range(1,2*M + 1) :
                if i+x > n :
                    break
                opponent = get_max(i+x , max(M,x))

                current = suffix[i] - opponent

                best = max(best , current)

            memo[(i,M)] = best
            return best

        n = len(piles)
        memo = {}

        # creating suffix
        suffix = [0] * (n+1)
        for i in range(n-1,-1,-1) :
            suffix[i] = suffix[i+1] + piles[i]
        print(suffix)

        return get_max(0,1)
        