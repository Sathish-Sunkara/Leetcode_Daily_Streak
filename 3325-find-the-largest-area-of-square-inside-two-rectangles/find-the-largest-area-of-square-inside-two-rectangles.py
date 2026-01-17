class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)
        ans = 0

        # we inspect each overlap area between every pair of rectangle so we use double for loop
        for i in range(n) :
            for j in range(i+1 , n) :
                # first rectangle coordinates
                x1 , y1 = bottomLeft[i]
                x2 , y2 = topRight[i]     

                # second rectangle coordinates
                x3 , y3 = bottomLeft[j]
                x4 , y4 = topRight[j]     

                # finding left  ,  right , bottom , top boundary coordinates of overlapping area of above 2 rectangles
                x_start = max(x1 , x3)
                x_end = min(x2 , x4)

                #handling both are not overlapping ( they are far away)
                if x_start > x_end :
                    continue

                y_start = max(y1 , y3)
                y_end = min(y2 , y4)

                #handling both are not overlapping ( they are far away)
                if y_start > y_end :
                    continue

                # these are  length of sides overlapping rectangle
                vertical = abs(y_start - y_end)
                horizental = abs(x_start - x_end)

                # we need square
                side = min(vertical , horizental)

                # for each over lapping area we do like above now we update max area
                ans = max(ans , side*side)
        return ans

                