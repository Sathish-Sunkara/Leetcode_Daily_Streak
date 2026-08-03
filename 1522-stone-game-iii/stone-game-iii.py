class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        memo = {}
        n = len(stoneValue)
        def get_max(s,e) :
            if (s,e) in memo :
                return memo[(s,e)]
            if s == e :
                return stoneValue[s]

            if s-1 == e :
                return 0


            pick1 = stoneValue[s] - get_max(s+1,e)
            pick2 = stoneValue[s] + stoneValue[s+1] - get_max(s+2,e)
            if s == n-2 :
                pick3 = 0
            else :
                pick3 = stoneValue[s] + stoneValue[s+1] + stoneValue[s+2] - get_max(s+3,e)

            memo[(s,e)] = max(pick1,pick2,pick3)

            return memo[(s,e)]

        alice_profit = get_max(0,len(stoneValue)-1)
        if alice_profit > 0 :
            return "Alice"

        elif alice_profit < 0 :
            return 'Bob'
        else :
            return "Tie"
        