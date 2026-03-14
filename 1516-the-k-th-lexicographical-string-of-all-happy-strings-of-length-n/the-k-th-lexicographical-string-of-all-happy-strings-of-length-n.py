class Solution:
    def getHappyString(self, n: int, k: int) -> str:


        
        length = 3 * 2**(n-1)
        if length < k :
            return "" 
        fact = (length // 3)
        k -= 1
        ans = ""
        prev = ""
        for i in range(n) :
            q = k // fact 
            rem = k % fact
            
            st = [ch for ch in "abc" if ch != prev]
            ans += st[q]
            k = rem
            fact = fact//2
            prev = st[q]
        return ans
        
        
            

        