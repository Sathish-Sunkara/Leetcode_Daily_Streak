class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:

        def count_devices(floor) :
            cnt = 0 
            for ch in floor :
                if ch == "1" :
                    cnt += 1
            return cnt

        ans  = 0
        prev = None
        n = len(bank)
        for i in range(n) :
            floor = bank[i]
            total_devices = count_devices(floor)
            if total_devices == 0 :
                continue
            if prev is None :
                prev = total_devices
            else :
                ans += prev*total_devices
                prev = total_devices
        return ans

        