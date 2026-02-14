class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0 for j in range(row+1)] for row in range(query_row+2)]
        dp[0][0] = poured

        for i in range(query_row+1) :
            # if i == query_row :
            #     return 1 if dp[i][query_glass] > 1 else   dp[i][query_glass]

            for j in range(i+1) :
                if dp[i][j] > 1 :
                    dp[i+1][j] += (dp[i][j] - 1)/2
                    dp[i+1][j+1] += (dp[i][j] - 1)/2
        return 1 if dp[query_row][query_glass] > 1 else dp[query_row][query_glass]
        