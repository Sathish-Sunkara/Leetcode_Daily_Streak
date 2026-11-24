class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a,b,c = nums
        if (a == 0 or b == 0 or c == 0) or (a+b <= c or b+c <= a or c+a <= b) :
            return 'none'
        
        if a == b == c :
            return "equilateral"
        if a==b or b ==c or c == a :
            return "isosceles"  
        if a != b != c :
            return "scalene"      