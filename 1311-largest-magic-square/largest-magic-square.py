class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:

        # rows = deepcopy(grid)
        # cols = deepcopy(grid)      
        # diag1 = deepcopy(grid)
        # diag2 = deepcopy(grid)

        n , m = len(grid) , len(grid[0])

        # for i in range(n) :
        #     for j in range(m) :
        #         if j == 0 :
        #             continue
        #         rows[i][j] = rows[i][j] + rows[i][j-1]
        # # print(rows)

        # for i in range(n) :
        #     for j in range(m) :
        #         if i == 0 :
        #             continue
        #         cols[i][j] = cols[i][j] + cols[i-1][j]
        # # print(cols)

        # for i in range(n) :
        #     for j in range(m) :
        #         if i == 0 or j == 0:
        #             continue
        #         diag1[i][j] = diag1[i][j] + diag1[i-1][j-1]
        # # print(diag1)

        # for i in range(n) :
        #     for j in range(m) :
        #         if i == 0 or j == 0:
        #             continue
        #         diag1[i][j] = diag1[i][j] + diag1[i-1][j-1]
        # # print(diag1)



        def is_valid(i , j , k) :
            # cheking each row 
            s = None
            for x in range(i,i+k) :
                if s is None :
                    s = sum(grid[x][j:j+k])
                if s != sum(grid[x][j:j+k]) :
                    return False

            # checkingeach column
            for x in range(j ,j+k) :
                sum1 = 0
                for r in range(i , i+k) :
                    sum1 += grid[r][x]
                if sum1 != s :
                    return False

            # checking diagonal 1 
            sum1 = 0
            for x in range(k) :
                sum1 += grid[i+x][j+x]
            if s != sum1 :
                return False
            sum1 = 0

            #check diag2
            for x in range(k) :
                sum1 += grid[i+x][j+k-1-x]
            if sum1 != s :
                return False

            return True









        ans  = 1
        maxi = min(m,n)
        for k in range(2,maxi + 1) :
            for i in range(n-k + 1) :
                for j in range(m - k + 1) :
                    if is_valid(i,j,k) :
                        ans = max(ans , k)
        return ans



        